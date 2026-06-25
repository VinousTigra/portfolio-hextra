<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import BookForm from '../components/BookForm.vue'
import LayoutCard from '../components/LayoutCard.vue'
import { createBook } from '../services/booksApi'

const router = useRouter()
const errorMessage = ref('')

async function handleCreate(book) {
  errorMessage.value = ''

  try {
    await createBook(book)
    router.push({ name: 'books' })
  } catch (error) {
    errorMessage.value = 'Не удалось создать книгу'
  }
}
</script>

<template>
  <section class="form-page">
    <LayoutCard>
      <template #header>
        <h1>Добавить книгу</h1>
      </template>

      <p v-if="errorMessage" class="error">
        {{ errorMessage }}
      </p>

      <BookForm submit-text="Добавить книгу" @submit="handleCreate" />
    </LayoutCard>
  </section>
</template>