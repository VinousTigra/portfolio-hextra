<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import BookList from '../components/BookList.vue'
import LayoutCard from '../components/LayoutCard.vue'
import { deleteBook, getBooks, updateBook } from '../services/booksApi'

const router = useRouter()

const books = ref([])
const searchQuery = ref('')
const selectedStatus = ref('all')
const sortMode = ref('createdAt')
const isLoading = ref(false)
const errorMessage = ref('')

const filteredBooks = computed(() => {
  let result = [...books.value]

  if (selectedStatus.value !== 'all') {
    result = result.filter((book) => book.status === selectedStatus.value)
  }

  if (searchQuery.value.trim()) {
    const query = searchQuery.value.trim().toLowerCase()

    result = result.filter((book) =>
      book.title.toLowerCase().includes(query) ||
      book.author.toLowerCase().includes(query)
    )
  }

  if (sortMode.value === 'title') {
    result.sort((a, b) => a.title.localeCompare(b.title))
  }

  if (sortMode.value === 'createdAt') {
    result.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
  }

  return result
})

async function loadBooks() {
  isLoading.value = true
  errorMessage.value = ''

  try {
    books.value = await getBooks()
  } catch (error) {
    errorMessage.value = 'Не удалось загрузить книги с сервера'
  } finally {
    isLoading.value = false
  }
}

function editBook(book) {
  router.push({ name: 'book-edit', params: { id: book.id } })
}

async function removeBook(book) {
  const confirmed = confirm(`Удалить книгу "${book.title}"?`)

  if (!confirmed) {
    return
  }

  try {
    await deleteBook(book.id)
    books.value = books.value.filter((item) => item.id !== book.id)
  } catch (error) {
    errorMessage.value = 'Не удалось удалить книгу'
  }
}

async function toggleStatus(book) {
  const updatedBook = {
    ...book,
    status: book.status === 'available' ? 'reserved' : 'available',
  }

  try {
    const savedBook = await updateBook(book.id, updatedBook)
    books.value = books.value.map((item) =>
      item.id === savedBook.id ? savedBook : item
    )
  } catch (error) {
    errorMessage.value = 'Не удалось изменить статус книги'
  }
}

async function toggleFavorite(book) {
  const updatedBook = {
    ...book,
    favorite: !book.favorite,
  }

  try {
    const savedBook = await updateBook(book.id, updatedBook)
    books.value = books.value.map((item) =>
      item.id === savedBook.id ? savedBook : item
    )
  } catch (error) {
    errorMessage.value = 'Не удалось изменить избранное'
  }
}

onMounted(() => {
  loadBooks()
})
</script>

<template>
  <section class="catalog-page">
    <aside class="sidebar">
      <LayoutCard>
        <template #header>
          <h2>Фильтры</h2>
        </template>

        <label>
          Поиск по названию или автору
          <input
            v-model.trim="searchQuery"
            type="text"
            placeholder="Например: Булгаков"
          >
        </label>

        <label>
          Статус
          <select v-model="selectedStatus">
            <option value="all">Все книги</option>
            <option value="available">В наличии</option>
            <option value="reserved">Забронированы</option>
          </select>
        </label>

        <label>
          Сортировка
          <select v-model="sortMode">
            <option value="createdAt">По дате добавления</option>
            <option value="title">По алфавиту</option>
          </select>
        </label>
      </LayoutCard>

      <RouterLink class="primary-link full-width" :to="{ name: 'book-create' }">
        Добавить книгу
      </RouterLink>
    </aside>

    <section class="content">
      <div class="content-header">
        <h2>Каталог книг</h2>
        <span>Найдено: {{ filteredBooks.length }}</span>
      </div>

      <p v-if="isLoading" class="empty">
        Загрузка книг с сервера...
      </p>

      <p v-if="errorMessage" class="error">
        {{ errorMessage }}
      </p>

      <BookList
        v-if="!isLoading"
        :books="filteredBooks"
        @delete="removeBook"
        @toggle-favorite="toggleFavorite"
        @toggle-status="toggleStatus"
        @edit="editBook"
      />
    </section>
  </section>
</template>