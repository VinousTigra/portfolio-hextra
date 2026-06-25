<script setup>
import { reactive, ref, watch } from 'vue'

const props = defineProps({
  initialBook: {
    type: Object,
    default: null,
  },
  submitText: {
    type: String,
    default: 'Сохранить',
  },
})

const emit = defineEmits(['submit'])

const form = reactive({
  title: '',
  author: '',
  year: new Date().getFullYear(),
  publisher: 'АСТ',
  status: 'available',
  category: '12+',
  description: '',
  favorite: false,
  cover_filename: '',
})

const coverFile = ref(null)

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

function handleSubmit() {
  if (!form.title.trim() || !form.author.trim()) {
    alert('Заполните название и автора книги')
    return
  }

  if (form.cover_filename && !/\.(jpg|jpeg)$/i.test(form.cover_filename)) {
    alert('Обложка должна быть файлом формата JPG или JPEG')
    return
  }

  emit('submit', {
    title: form.title.trim(),
    author: form.author.trim(),
    year: Number(form.year),
    publisher: form.publisher,
    status: form.status,
    category: form.category,
    description: form.description.trim(),
    favorite: form.favorite,
    cover_filename: form.cover_filename,
    cover_file: coverFile.value,
  })
}

function handleCoverChange(event) {
  const file = event.target.files[0]

  if (!file) {
    coverFile.value = null
    form.cover_filename = ''
    return
  }

  if (!/\.(jpg|jpeg)$/i.test(file.name)) {
    alert('Можно выбрать только файл JPG или JPEG')
    event.target.value = ''
    coverFile.value = null
    form.cover_filename = ''
    return
  }

  coverFile.value = file
  form.cover_filename = file.name
}

</script>

<template>
  <form class="book-form" @submit.prevent="handleSubmit">
    <label>
      Заголовок
      <input v-model.trim="form.title" type="text">
    </label>

    <label>
      Автор
      <input v-model.trim="form.author" type="text">
    </label>

    <label>
      Описание
      <textarea v-model.trim="form.description"></textarea>
    </label>

	<label>
 	 Обложка книги JPG
	  <input
  	  type="file"
 	   accept=".jpg,.jpeg,image/jpeg"
 	   @change="handleCoverChange"
 	 >
	  <span v-if="form.cover_filename" class="file-name">
 	   Выбран файл: {{ form.cover_filename }}
 	 </span>
	</label>

    <label>
      Год издания
      <input v-model.number="form.year" type="number" min="0">
    </label>

    <label>
      Издательство
      <select v-model="form.publisher">
        <option value="АСТ">АСТ</option>
        <option value="Эксмо">Эксмо</option>
        <option value="Азбука">Азбука</option>
        <option value="Росмэн">Росмэн</option>
      </select>
    </label>

    <fieldset class="radio-group">
      <legend>Категория / возрастной рейтинг</legend>

      <label>
        <input v-model="form.category" type="radio" value="0+">
        0+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="6+">
        6+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="12+">
        12+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="16+">
        16+
      </label>
    </fieldset>

    <label>
      Статус
      <select v-model="form.status">
        <option value="available">В наличии</option>
        <option value="reserved">Забронирована</option>
      </select>
    </label>

    <button type="submit" class="submit-button">
      {{ submitText }}
    </button>
  </form>
</template>