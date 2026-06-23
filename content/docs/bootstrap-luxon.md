---
title: "Bootstrap 5 с Luxon"
weight: 20
---

# Интеграция Bootstrap 5 в приложение с Luxon. Этап 2

## Цель работы

Цель работы — встроить приложение с библиотекой Luxon в шаблон Bootstrap 5. В результате должна получиться страница с сеткой из трёх колонок, большой красной кнопкой и модальным окном Bootstrap, в котором отображается дата и время, сформированные с помощью Luxon.

## Задание

Сначала была создана отдельная папка для второго этапа лабораторной работы:

```powershell
cd "C:\Users\Tigra\Documents\study\4 semester\front\portfolio-hextra"
mkdir labs\bootstrap-luxon
cd labs\bootstrap-luxon
```

Затем был инициализирован npm-проект:

```powershell
npm init -y
```

После этого была установлена библиотека Luxon:

```powershell
npm i luxon
```

Также были установлены webpack, webpack-cli и serve:

```powershell
npm i -D webpack webpack-cli serve
```

Далее была создана папка `src`:

```powershell
mkdir src
```

В проекте были созданы файлы:

```text
index.html
webpack.config.js
src/index.js
```

## HTML-код страницы

В файле `index.html` была создана страница с использованием Bootstrap 5. На странице реализована сетка из трёх колонок:

- левая колонка — `col-2`;
- центральная колонка — `col-8`;
- правая колонка — `col-2`.

В центральной колонке размещена большая красная кнопка `Показать время`. Для неё использованы классы Bootstrap `btn`, `btn-danger`, `btn-lg` и `w-100`.

Также на странице реализовано модальное окно Bootstrap. В заголовке окна указано имя выполнившего задание: `Шулепова Виктория`.

Скриншоты HTML-кода:

<p>
  <img src="/portfolio-hextra/images/bootstrap-luxon/html-code-1.png" alt="Первая часть HTML-кода" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</p>

<p>
  <img src="/portfolio-hextra/images/bootstrap-luxon/html-code-2.png" alt="Вторая часть HTML-кода" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</p>

## JavaScript-код приложения

В файле `src/index.js` была подключена библиотека Luxon. При нажатии на кнопку JavaScript получает текущую дату и время, форматирует их с помощью Luxon и выводит результат в модальное окно Bootstrap.

```js
import { DateTime } from 'luxon';

const showTimeButton = document.getElementById('showTimeButton');
const timeOutput = document.getElementById('timeOutput');
const timeModalElement = document.getElementById('timeModal');

const timeModal = new bootstrap.Modal(timeModalElement);

function getCurrentTime() {
  return DateTime
    .now()
    .setLocale('ru')
    .toFormat('dd.LL.yyyy HH:mm:ss');
}

showTimeButton.addEventListener('click', () => {
  timeOutput.textContent = getCurrentTime();
  timeModal.show();
});
```

## Конфигурация webpack

Для сборки проекта был создан файл `webpack.config.js`.

```js
const path = require('path');

module.exports = {
  mode: 'production',
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        type: 'javascript/esm',
      },
    ],
  },
};
```

## Сборка проекта

Сборка приложения была выполнена командой:

```powershell
npx webpack
```

В результате webpack создал файл:

```text
dist/main.js
```

Этот файл был подключён на HTML-странице:

```html
<script src="./dist/main.js"></script>
```

## Запуск приложения

Для локального запуска приложения была использована команда:

```powershell
npx serve . -l 3000
```

После этого приложение было открыто в браузере по адресу:

```text
http://localhost:3000/
```

## Результат работы

После нажатия на кнопку `Показать время` открывается модальное окно Bootstrap. В заголовке окна указано имя выполнившего задание — `Шулепова Виктория`.

В основной части модального окна отображается дата и время, сформированные с помощью библиотеки Luxon.

Закрыть окно можно двумя способами:

- с помощью крестика в правом верхнем углу;
- с помощью кнопки `Закрыть` в правом нижнем углу.

<p>
  <img src="/portfolio-hextra/images/bootstrap-luxon/bootstrap-result.png" alt="Внешний вид приложения с открытым модальным окном" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</p>

## Последовательность действий для запуска

Чтобы повторно запустить приложение, необходимо выполнить команды:

```powershell
cd "C:\Users\Tigra\Documents\study\4 semester\front\portfolio-hextra\labs\bootstrap-luxon"
npm install
npx webpack
npx serve . -l 3000
```

Затем открыть в браузере:

```text
http://localhost:3000/
```