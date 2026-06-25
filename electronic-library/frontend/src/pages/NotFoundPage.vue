<template>
  <section class="not-found">
    <div class="layout-card">
      <p class="eyebrow dark">404</p>
      <h1>Страница не найдена</h1>
      <p class="home-text">
        Такой страницы нет. Вернитесь на главную или откройте электронный каталог.
      </p>

      <RouterLink class="primary-link" :to="{ name: 'home' }">
        На главную
      </RouterLink>
    </div>
  </section>
</template>