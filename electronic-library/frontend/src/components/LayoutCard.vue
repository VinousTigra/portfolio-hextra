<template>
  <section class="layout-card">
    <header v-if="$slots.header" class="layout-card__header">
      <slot name="header"></slot>
    </header>

    <div class="layout-card__body">
      <slot></slot>
    </div>

    <footer v-if="$slots.footer" class="layout-card__footer">
      <slot name="footer" :created-by="'Шулепова Виктория'"></slot>
    </footer>
  </section>
</template>