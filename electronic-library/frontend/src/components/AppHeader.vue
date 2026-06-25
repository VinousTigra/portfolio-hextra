<template>
  <header class="header">
    <RouterLink class="logo" :to="{ name: 'home' }">
      ElectoLibrary
    </RouterLink>

    <nav class="nav">
      <RouterLink :to="{ name: 'home' }">
        Главная
      </RouterLink>

      <RouterLink :to="{ name: 'books' }">
        Электронный каталог
      </RouterLink>

      <RouterLink :to="{ name: 'book-create' }">
        Добавить книгу
      </RouterLink>
    </nav>
  </header>
</template>