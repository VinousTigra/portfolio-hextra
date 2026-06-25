<script setup>
import BookItem from './BookItem.vue'

defineProps({
  books: {
    type: Array,
    required: true,
  },
})

defineEmits(['delete', 'toggleFavorite', 'toggleStatus', 'edit'])
</script>

<template>
  <div class="book-list">
    <p v-if="books.length === 0" class="empty">
      Книги не найдены.
    </p>

    <BookItem
      v-for="book in books"
      :key="book.id"
      :book="book"
      @delete="$emit('delete', $event)"
      @toggle-favorite="$emit('toggleFavorite', $event)"
      @toggle-status="$emit('toggleStatus', $event)"
      @edit="$emit('edit', $event)"
    />
  </div>
</template>