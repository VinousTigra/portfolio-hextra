<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import BookForm from '../components/BookForm.vue'
import LayoutCard from '../components/LayoutCard.vue'
import { getBookById, updateBook } from '../services/booksApi'

const props = defineProps({
  id: {
    type: String,
    required: true,
  },
})

const router = useRouter()
const book = ref(null)
const isLoading = ref(false)
const errorMessage = ref('')

async function loadBook() {
  isLoading.value = true
  errorMessage.value = ''

  try {
    book.value = await getBookById(props.id)
  } catch (error) {
    errorMessage.value = 'Книга не найдена'
  } finally {
    isLoading.value = false
  }
}

async function handleUpdate(updatedBook) {
  errorMessage.value = ''

  try {
    await updateBook(props.id, updatedBook)
    router.push({ name: 'books' })
  } catch (error) {
    errorMessage.value = 'Не удалось сохранить изменения'
  }
}

onMounted(() => {
  loadBook()
})
</script>

<template>
  <section class="form-page">
    <LayoutCard>
      <template #header>
        <h1>Редактировать книгу</h1>
      </template>

      <p v-if="isLoading" class="empty">
        Загрузка книги...
      </p>

      <p v-if="errorMessage" class="error">
        {{ errorMessage }}
      </p>

      <BookForm
        v-if="book"
        :initial-book="book"
        submit-text="Сохранить изменения"
        @submit="handleUpdate"
      />
    </LayoutCard>
  </section>
</template>