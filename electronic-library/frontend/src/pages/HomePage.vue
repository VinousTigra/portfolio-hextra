<script setup>
import LayoutCard from '../components/LayoutCard.vue'
</script>

<template>
  <section class="home">
    <LayoutCard>
      <template #header>
        <p class="eyebrow dark">Library</p>
        <h1>Электронная библиотека</h1>
      </template>

      <p class="home-text">
        Учебное SPA-приложение для управления каталогом книг. В приложении реализованы
        список книг, фильтрация, сортировка, добавление, редактирование, удаление,
        избранное и бронирование.
      </p>

      <RouterLink class="primary-link" :to="{ name: 'books' }">
        Открыть электронный каталог
      </RouterLink>

      <template #footer="{ createdBy }">
        <span>Выполнила: {{ createdBy }}</span>
      </template>
    </LayoutCard>
  </section>
</template>