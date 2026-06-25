from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from database import Base


class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    publisher = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False, default="available")
    category = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    favorite = Column(Boolean, nullable=False, default=False)
    cover_filename = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())