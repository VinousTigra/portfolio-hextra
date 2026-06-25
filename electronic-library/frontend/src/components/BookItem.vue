<script setup>
defineProps({
  book: {
    type: Object,
    required: true,
  },
})

defineEmits(['delete', 'toggleFavorite', 'toggleStatus', 'edit'])
</script>

<template>
  <article class="book-card">
    <div class="book-cover-wrap">
      <img
        v-if="book.cover_url"
        class="book-cover"
        :src="book.cover_url"
        :alt="`Обложка книги ${book.title}`"
      >

      <div v-else class="book-cover-placeholder">
        Нет обложки
      </div>
    </div>

    <div class="book-info">
      <div class="book-card__top">
        <span
          class="status"
          :class="{ reserved: book.status === 'reserved' }"
        >
          {{ book.status === 'available' ? 'В наличии' : 'Забронирована' }}
        </span>

        <button
          type="button"
          class="favorite"
          :class="{ active: book.favorite }"
          @click="$emit('toggleFavorite', book)"
        >
          ♥
        </button>
      </div>

      <h3>{{ book.title }}</h3>

      <p class="author">
        {{ book.author }}
      </p>

      <p class="description">
        {{ book.description }}
      </p>

      <p v-if="book.cover_filename" class="cover-name">
        Файл обложки: {{ book.cover_filename }}
      </p>

      <dl>
        <div>
          <dt>Год</dt>
          <dd>{{ book.year }}</dd>
        </div>

        <div>
          <dt>Издательство</dt>
          <dd>{{ book.publisher }}</dd>
        </div>

        <div>
          <dt>Категория</dt>
          <dd>{{ book.category }}</dd>
        </div>
      </dl>
    </div>

    <div class="actions">
      <button type="button" @click="$emit('edit', book)">
        Редактировать
      </button>

      <button type="button" @click="$emit('toggleStatus', book)">
        Изменить статус
      </button>

      <button type="button" class="danger" @click="$emit('delete', book)">
        Удалить
      </button>
    </div>
  </article>
</template>