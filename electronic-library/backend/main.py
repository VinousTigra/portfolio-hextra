import os
import shutil
from pathlib import Path
from time import sleep
from typing import Optional
from uuid import uuid4

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import BookModel

def create_tables_with_retry():
    for attempt in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            return
        except OperationalError:
            sleep(2)

    Base.metadata.create_all(bind=engine)


create_tables_with_retry()

app = FastAPI(title="ElectoLibrary API")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def serialize_book(book: BookModel):
    cover_url = None

    if book.cover_filename:
        cover_url = f"http://localhost:8000/uploads/{book.cover_filename}"

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "publisher": book.publisher,
        "status": book.status,
        "category": book.category,
        "description": book.description,
        "favorite": book.favorite,
        "cover_filename": book.cover_filename,
        "cover_url": cover_url,
        "created_at": book.created_at.isoformat() if book.created_at else None,
    }


def seed_books(db: Session):
    existing_count = db.query(BookModel).count()

    if existing_count > 0:
        return

    initial_books = [
        BookModel(
            title="Мастер и Маргарита",
            author="Михаил Булгаков",
            year=1967,
            publisher="Азбука",
            status="available",
            category="12+",
            description="Роман о добре, зле, любви и свободе выбора.",
            favorite=False,
        ),
        BookModel(
            title="Преступление и наказание",
            author="Фёдор Достоевский",
            year=1866,
            publisher="Эксмо",
            status="reserved",
            category="16+",
            description="Психологический роман о преступлении, совести и наказании.",
            favorite=True,
        ),
        BookModel(
            title="451 градус по Фаренгейту",
            author="Рэй Брэдбери",
            year=1953,
            publisher="АСТ",
            status="available",
            category="12+",
            description="История общества, в котором книги находятся под запретом.",
            favorite=False,
        ),
    ]

    db.add_all(initial_books)
    db.commit()


@app.on_event("startup")
def on_startup():
    db = next(get_db())

    try:
        seed_books(db)
    finally:
        db.close()

def save_cover_file(cover_file: Optional[UploadFile]):
    if not cover_file or not cover_file.filename:
        return None

    original_name = cover_file.filename
    extension = os.path.splitext(original_name)[1].lower()

    if extension not in [".jpg", ".jpeg"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cover must be a JPG or JPEG file",
        )

    safe_filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / safe_filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(cover_file.file, buffer)

    return safe_filename

@app.get("/")
def read_root():
    return {"message": "ElectoLibrary API"}


@app.get("/api/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).order_by(BookModel.created_at.desc()).all()
    return [serialize_book(book) for book in books]


@app.get("/api/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return serialize_book(book)


@app.post("/api/books", status_code=status.HTTP_201_CREATED)
@app.post("/api/books", status_code=status.HTTP_201_CREATED)
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    publisher: str = Form(...),
    status_value: str = Form("available", alias="status"),
    category: str = Form(...),
    description: str = Form(...),
    favorite: bool = Form(False),
    cover_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    cover_filename = save_cover_file(cover_file)

    new_book = BookModel(
        title=title,
        author=author,
        year=year,
        publisher=publisher,
        status=status_value,
        category=category,
        description=description,
        favorite=favorite,
        cover_filename=cover_filename,
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return serialize_book(new_book)

@app.put("/api/books/{book_id}")
def update_book(
    book_id: int,
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    publisher: str = Form(...),
    status_value: str = Form("available", alias="status"),
    category: str = Form(...),
    description: str = Form(...),
    favorite: bool = Form(False),
    cover_filename: Optional[str] = Form(None),
    cover_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    new_cover_filename = save_cover_file(cover_file)

    book.title = title
    book.author = author
    book.year = year
    book.publisher = publisher
    book.status = status_value
    book.category = category
    book.description = description
    book.favorite = favorite
    book.cover_filename = new_cover_filename or cover_filename or book.cover_filename

    db.commit()
    db.refresh(book)

    return serialize_book(book)


@app.delete("/api/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    db.delete(book)
    db.commit()

    return {"message": "Book deleted"}