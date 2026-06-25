const API_URL = 'http://localhost:8000/api/books'

function createBookFormData(book) {
  const formData = new FormData()

  formData.append('title', book.title)
  formData.append('author', book.author)
  formData.append('year', book.year)
  formData.append('publisher', book.publisher)
  formData.append('status', book.status)
  formData.append('category', book.category)
  formData.append('description', book.description)
  formData.append('favorite', book.favorite)

  if (book.cover_filename) {
    formData.append('cover_filename', book.cover_filename)
  }

  if (book.cover_file) {
    formData.append('cover_file', book.cover_file)
  }

  return formData
}

export async function getBooks() {
  const response = await fetch(API_URL)

  if (!response.ok) {
    throw new Error('Не удалось загрузить книги')
  }

  return response.json()
}

export async function getBookById(id) {
  const response = await fetch(`${API_URL}/${id}`)

  if (!response.ok) {
    throw new Error('Книга не найдена')
  }

  return response.json()
}

export async function createBook(book) {
  const response = await fetch(API_URL, {
    method: 'POST',
    body: createBookFormData(book),
  })

  if (!response.ok) {
    throw new Error('Не удалось создать книгу')
  }

  return response.json()
}

export async function updateBook(id, book) {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    body: createBookFormData(book),
  })

  if (!response.ok) {
    throw new Error('Не удалось обновить книгу')
  }

  return response.json()
}

export async function deleteBook(id) {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'DELETE',
  })

  if (!response.ok) {
    throw new Error('Не удалось удалить книгу')
  }

  return response.json()
}