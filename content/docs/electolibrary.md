# ElectoLibrary — SPA-приложение на Vue 3 с сервером на Python

**Автор:** Шулепова Виктория
**Группа:** P3269
**Название работы:** Разработка SPA-приложения на Vue 3 с сервером на Python

**Репозиторий:** https://github.com/VinousTigra/portfolio-hextra/tree/main/electronic-library

---

## 1. Цель работы

Цель работы — разработать полноценное SPA-приложение на Vue 3 с серверной частью на Python, реализовать работу с компонентами, формами, слотами, маршрутизацией, REST API, базой данных PostgreSQL и запуском проекта через Docker Compose.

В ходе работы были отработаны:

* привязка данных во Vue 3;
* обработка событий;
* `computed`;
* `watch`;
* `ref`;
* жизненный цикл компонента через `onMounted`;
* формы и модификаторы `v-model`;
* условный рендеринг;
* вывод массивов через `v-for`;
* сортировка и фильтрация данных;
* компонентный подход;
* `props`;
* передача событий от дочернего компонента к родительскому;
* слоты;
* Vue Router;
* взаимодействие frontend с backend через REST API;
* работа с PostgreSQL;
* контейнеризация через Docker.

---

## 2. Описание приложения

Разработано мини-приложение **ElectoLibrary** — электронная библиотека для управления каталогом книг.

Приложение позволяет:

* просматривать список книг;
* добавлять новую книгу;
* редактировать данные книги;
* удалять книгу;
* фильтровать книги по статусу;
* сортировать книги по дате добавления и алфавиту;
* добавлять книгу в избранное;
* изменять статус книги: «В наличии» / «Забронирована»;
* загружать JPG-обложку книги;
* просматривать обложку в карточке книги;
* работать с несколькими страницами через Vue Router;
* сохранять данные на сервере в PostgreSQL;
* запускать проект через Docker Compose.

---

## 3. Структура проекта

```text
electronic-library
├── backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── uploads
│
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppFooter.vue
│   │   │   ├── LayoutCard.vue
│   │   │   ├── BookList.vue
│   │   │   ├── BookItem.vue
│   │   │   └── BookForm.vue
│   │   │
│   │   ├── pages
│   │   │   ├── HomePage.vue
│   │   │   ├── BooksLayoutPage.vue
│   │   │   ├── BooksPage.vue
│   │   │   ├── BookCreatePage.vue
│   │   │   ├── BookEditPage.vue
│   │   │   └── NotFoundPage.vue
│   │   │
│   │   ├── router
│   │   │   └── index.js
│   │   │
│   │   ├── services
│   │   │   └── booksApi.js
│   │   │
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── style.css
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── nginx.conf
│   └── Dockerfile
│
├── docs
│   ├── imgs
│   └── electolibrary_dump.sql
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 4. Реализованные компоненты

В проекте реализованы обязательные компоненты:

### `AppHeader.vue`

Компонент верхнего меню. Содержит название приложения **ElectoLibrary** и навигационные ссылки:

* Главная;
* Электронный каталог;
* Добавить книгу.

### `AppFooter.vue`

Компонент нижней панели приложения.

### `BookList.vue`

Компонент списка книг. Получает массив книг через `props` и выводит карточки книг через `v-for`.

### `BookItem.vue`

Компонент одной книги. Получает объект книги через `props`.

В карточке отображаются:

* обложка;
* статус;
* название;
* автор;
* описание;
* год издания;
* издательство;
* категория;
* кнопка избранного;
* кнопки редактирования, изменения статуса и удаления.

Также компонент передаёт события родителю:

* `delete`;
* `toggleFavorite`;
* `toggleStatus`;
* `edit`.

### `BookForm.vue`

Компонент формы создания и редактирования книги.

Форма содержит:

* заголовок;
* автора;
* описание;
* обложку JPG;
* год издания;
* издательство;
* категорию;
* статус.

В форме используется `v-model` с модификаторами:

```vue
<input v-model.trim="form.title" type="text">
<input v-model.number="form.year" type="number">
```

Также реализована валидация:

* проверка заполнения названия;
* проверка заполнения автора;
* проверка формата обложки `.jpg` или `.jpeg`.

### `LayoutCard.vue`

Компонент-контейнер со слотами.

В нём используются:

* обычный слот;
* именованный слот `header`;
* именованный слот `footer`;
* scoped slot с передачей значения `createdBy`.

Пример:

```vue
<slot name="footer" :created-by="'Шулепова Виктория'"></slot>
```

---

## 5. Использование Vue 3

### `ref`

Используется для реактивных переменных:

```js
const books = ref([])
const searchQuery = ref('')
const selectedStatus = ref('all')
const isLoading = ref(false)
const errorMessage = ref('')
```

### `computed`

Используется для фильтрации и сортировки книг:

```js
const filteredBooks = computed(() => {
  let result = [...books.value]

  if (selectedStatus.value !== 'all') {
    result = result.filter((book) => book.status === selectedStatus.value)
  }

  if (searchQuery.value.trim()) {
    const query = searchQuery.value.trim().toLowerCase()

    result = result.filter((book) =>
      book.title.toLowerCase().includes(query) ||
      book.author.toLowerCase().includes(query)
    )
  }

  if (sortMode.value === 'title') {
    result.sort((a, b) => a.title.localeCompare(b.title))
  }

  if (sortMode.value === 'createdAt') {
    result.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
  }

  return result
})
```

### `watch`

Используется в форме книги для заполнения полей при редактировании:

```js
watch(
  () => props.initialBook,
  (book) => {
    if (book) {
      form.title = book.title
      form.author = book.author
      form.year = book.year
      form.publisher = book.publisher
      form.status = book.status
      form.category = book.category
      form.description = book.description
      form.favorite = Boolean(book.favorite)
      form.cover_filename = book.cover_filename || ''
    }
  },
  { immediate: true }
)
```

### `onMounted`

Используется для загрузки книг при открытии страницы каталога:

```js
onMounted(() => {
  loadBooks()
})
```

---

## 6. Маршрутизация

В проекте используется `vue-router`.

Реализованы маршруты:

```text
/                  — главная страница
/books             — электронный каталог
/books/new         — создание книги
/books/:id/edit    — редактирование книги
/:pathMatch(.*)*   — страница 404
```

Также реализованы:

* именованные маршруты;
* программная навигация;
* вложенные маршруты.

Пример вложенных маршрутов:

```js
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
}
```

Пример программной навигации:

```js
router.push({ name: 'books' })
```

---

## 7. Серверная часть

Серверная часть реализована на **FastAPI**.

Backend содержит REST API для работы с книгами.

### Реализованные API-методы

```text
GET    /api/books
GET    /api/books/{book_id}
POST   /api/books
PUT    /api/books/{book_id}
DELETE /api/books/{book_id}
```

### Назначение методов

| Метод                         | Назначение                  |
| ----------------------------- | --------------------------- |
| `GET /api/books`              | Получение списка книг       |
| `GET /api/books/{book_id}`    | Получение одной книги по id |
| `POST /api/books`             | Создание новой книги        |
| `PUT /api/books/{book_id}`    | Редактирование книги        |
| `DELETE /api/books/{book_id}` | Удаление книги              |

Также backend принимает JPG-обложки через `UploadFile`, сохраняет их в папку `uploads` и отдаёт по URL:

```text
http://localhost:8000/uploads/<filename>
```

---

## 8. База данных PostgreSQL

Для хранения данных используется **PostgreSQL**.

В базе данных хранится таблица `books`.

Поля книги:

* `id`;
* `title`;
* `author`;
* `year`;
* `publisher`;
* `status`;
* `category`;
* `description`;
* `favorite`;
* `cover_filename`;
* `created_at`.

Пример JSON-данных:

```json
[
  {
    "id": 1,
    "title": "Мастер и Маргарита",
    "author": "Михаил Булгаков",
    "year": 1967,
    "publisher": "Азбука",
    "status": "available",
    "category": "12+",
    "description": "Роман о добре, зле, любви и свободе выбора.",
    "favorite": false,
    "cover_filename": null,
    "cover_url": null,
    "created_at": "2026-06-25T10:00:00"
  }
]
```

### PostgreSQL dump

Для выгрузки данных используется команда:

```powershell
docker exec electolibrary-postgres pg_dump -U postgres electolibrary > docs\electolibrary_dump.sql
```

Для восстановления данных:

```powershell
docker exec -i electolibrary-postgres psql -U postgres electolibrary < docs\electolibrary_dump.sql
```

---

## 9. Docker

Проект запускается через Docker Compose.

В `docker-compose.yml` описаны три сервиса:

* `frontend`;
* `backend`;
* `postgres`.

Также используются volume:

* для хранения данных PostgreSQL;
* для хранения загруженных обложек.

### Запуск проекта

Из папки `electronic-library` выполнить:

```powershell
docker compose up --build
```

После запуска доступны адреса:

```text
Frontend: http://localhost:8080
Backend API: http://localhost:8000/api/books
Swagger UI: http://localhost:8000/docs
```

### Остановка проекта

```powershell
docker compose down
```

---
## Скриншоты интерфейса

### Главная страница

На главной странице находится приветственный блок приложения **ElectoLibrary** и ссылка для перехода в электронный каталог.

<img src="/portfolio-hextra/images/electolibrary/home-page.png" alt="Главная страница ElectoLibrary" width="900">

---

### Электронный каталог

На странице каталога отображается список книг. У каждой книги выводятся обложка, название, автор, описание, год издания, издательство, категория, статус, избранное и кнопки управления.

<img src="/portfolio-hextra/images/electolibrary/books-page.png" alt="Электронный каталог книг" width="900">

---

### Фильтрация и сортировка

На странице каталога реализованы поиск, фильтрация по статусу и сортировка по дате добавления или по алфавиту.

<img src="/portfolio-hextra/images/electolibrary/filter-sort-page.png" alt="Фильтрация и сортировка книг" width="900">

---

### Форма создания книги

Форма создания книги находится на маршруте `/books/new`. В ней используются поля ввода, `textarea`, `select`, `radio`-кнопки и загрузка JPG-обложки.

<img src="/portfolio-hextra/images/electolibrary/create-book-page-1.png" alt="Форма создания книги, часть 1" width="900">

<img src="/portfolio-hextra/images/electolibrary/create-book-page-2.png" alt="Форма создания книги, часть 2" width="900">

---

### Форма редактирования книги

Страница редактирования открывается по маршруту `/books/:id/edit`. Поля формы автоматически заполняются данными выбранной книги.

<img src="/portfolio-hextra/images/electolibrary/edit-book-page-1.png" alt="Форма редактирования книги, часть 1" width="900">

<img src="/portfolio-hextra/images/electolibrary/edit-book-page-2.png" alt="Форма редактирования книги, часть 2" width="900">

---

### Страница 404

Для несуществующих маршрутов реализована отдельная страница ошибки.

<img src="/portfolio-hextra/images/electolibrary/not-found-page.png" alt="Страница 404" width="900">

---

### Swagger UI

FastAPI автоматически предоставляет документацию API через Swagger UI. В ней отображаются все CRUD-маршруты для работы с книгами.

<img src="/portfolio-hextra/images/electolibrary/swagger-api.png" alt="Swagger UI FastAPI" width="900">

---

### Запуск через Docker Compose

Проект запускается одной командой `docker compose up --build`. В Docker Compose поднимаются три сервиса: frontend, backend и PostgreSQL.

<img src="/portfolio-hextra/images/electolibrary/docker-compose.png" alt="Запуск проекта через Docker Compose" width="900">

---

## 11. Инструкция по локальному запуску без Docker

### Backend

```powershell
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

Backend будет доступен по адресу:

```text
http://localhost:8000
```

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

Frontend будет доступен по адресу:

```text
http://localhost:5173
```

---

## 12. Инструкция по запуску через Docker

Из папки `electronic-library`:

```powershell
docker compose build
docker compose up
```

Или одной командой:

```powershell
docker compose up --build
```

Проверить работу:

```text
http://localhost:8080
http://localhost:8000/api/books
http://localhost:8000/docs
```

---

## 13. Выводы

В ходе выполнения работы было разработано SPA-приложение **ElectoLibrary** на Vue 3 с серверной частью на FastAPI.

Были изучены и применены:

* компонентный подход во Vue 3;
* работа с `props`;
* передача событий от дочернего компонента к родительскому;
* работа с формами;
* `v-model` и его модификаторы;
* `computed`;
* `watch`;
* `ref`;
* жизненный цикл компонента;
* условный рендеринг;
* вывод списков через `v-for`;
* Vue Router;
* именованные и вложенные маршруты;
* программная навигация;
* страница 404;
* REST API;
* работа с PostgreSQL;
* загрузка файлов на сервер;
* контейнеризация frontend, backend и базы данных через Docker Compose.

В результате получилось полноценное клиент-серверное приложение для управления электронной библиотекой.
