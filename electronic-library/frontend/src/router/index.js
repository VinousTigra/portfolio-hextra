import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../pages/HomePage.vue'
import BooksLayoutPage from '../pages/BooksLayoutPage.vue'
import BooksPage from '../pages/BooksPage.vue'
import BookCreatePage from '../pages/BookCreatePage.vue'
import BookEditPage from '../pages/BookEditPage.vue'
import NotFoundPage from '../pages/NotFoundPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/books',
      component: BooksLayoutPage,
      children: [
        {
          path: '',
          name: 'books',
          component: BooksPage,
        },
        {
          path: 'new',
          name: 'book-create',
          component: BookCreatePage,
        },
        {
          path: ':id/edit',
          name: 'book-edit',
          component: BookEditPage,
          props: true,
        },
      ],
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFoundPage,
    },
  ],
})

export default router