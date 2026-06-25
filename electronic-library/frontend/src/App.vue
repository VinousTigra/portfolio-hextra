<script setup>
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
</script>

<template>
  <div class="app">
    <AppHeader />

    <main class="page">
      <RouterView />
    </main>

    <AppFooter />
  </div>
</template>