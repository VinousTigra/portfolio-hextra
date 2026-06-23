---
title: "Webpack"
----------------

# Базовая сборка с помощью webpack и Docker

## Цель работы

Цель работы — установить Node.js, создать JavaScript-проект, подключить библиотеку Luxon, выполнить сборку проекта с помощью webpack, оформить страницу с использованием Bootstrap CDN, а затем запустить приложение внутри Docker-контейнера.


## Создание проекта

Сначала была создана отдельная папка:

```powershell
mkdir labs\webpack2026
cd labs\webpack2026
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

## JavaScript-код приложения

В папке `src` был создан файл `index.js`.

```js
import { DateTime } from 'luxon';

function updateTime() {
  const element = document.getElementById('hh');

  element.textContent = DateTime
    .now()
    .setLocale('ru')
    .toFormat('dd.LL.yyyy HH:mm:ss');
}

updateTime();
setInterval(updateTime, 1000);
```


## HTML-страница с Bootstrap CDN

Для отображения результата была создана страница `index.html`. Bootstrap подключён через CDN.

```html
<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Webpack + Luxon</title>

  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    rel="stylesheet"
  >
</head>
<body class="bg-light">
  <main class="container py-5">
    <section class="card shadow-sm">
      <div class="card-body text-center">
        <h1 class="display-4 mb-4">Базовая сборка с помощью webpack</h1>

        <p class="lead">
          Текущее время, сформированное библиотекой Luxon:
        </p>

        <h2 id="hh" class="display-1 fw-bold text-primary my-5"></h2>

        <p class="text-muted">
          JavaScript-код собран webpack в файл <code>dist/main.js</code>.
        </p>
      </div>
    </section>
  </main>

  <script src="./dist/main.js"></script>
</body>
</html>
```

На странице крупно выводится содержимое, сформированное библиотекой Luxon. Для оформления используется Bootstrap CDN.

## Конфигурация webpack

Для корректной сборки проекта был создан файл `webpack.config.js`.

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

## Сборка проекта webpack

Сборка проекта была выполнена командой:

```powershell
npx webpack
```

В результате webpack создал файл `dist/main.js`.

 <img src="/portfolio-hextra/images/webpack2026/webpack-build.png" alt="Результат сборки webpack" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">

## Внешний вид страницы

Для проверки страницы был запущен локальный сервер:

```powershell
npx serve . -l 3000
```

Страница была открыта в браузере по адресу:

```text
http://localhost:3000/
```

На странице отображается крупное текущее время, сформированное библиотекой Luxon.

  <img src="/portfolio-hextra/images/webpack2026/browser-bootstrap.png" alt="Внешний вид страницы с Bootstrap и Luxon" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">


## Dockerfile

Для запуска приложения внутри Docker-контейнера был создан файл `Dockerfile`.

```dockerfile
FROM node:24-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npx webpack

EXPOSE 3000

CMD ["npx", "serve", ".", "-l", "tcp://0.0.0.0:3000"]
```

В Dockerfile используется образ `node:24-alpine`, так как это облегчённая версия Node.js-образа.

## Файл .dockerignore

Чтобы не копировать лишние файлы внутрь Docker-образа, был создан файл `.dockerignore`.

```text
node_modules
dist
.git
.gitignore
.dockerignore
```

## Сборка и запуск Docker-контейнера

Docker-образ был собран командой:

```powershell
docker build -t webpack2026-lab .
```

После сборки образа приложение было запущено внутри контейнера:

```powershell
docker run --rm -p 3000:3000 webpack2026-lab
```

Скриншот ниже показывает сборку Docker-образа и запуск приложения через Docker.

  <img src="/portfolio-hextra/images/webpack2026/docker-run.png" alt="Сборка и запуск приложения через Docker" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">


После запуска контейнера приложение доступно в браузере по адресу:

```text
http://localhost:3000/
```

  <img src="/portfolio-hextra/images/webpack2026/docker-browser.png" alt="Страница приложения, запущенного через Docker" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">


## Последовательность действий для запуска

Для локального запуска без Docker нужно выполнить:

```powershell
cd labs\webpack2026
npm install
npx webpack
npx serve . -l 3000
```

После этого открыть в браузере:

```text
http://localhost:3000/
```

Для запуска через Docker нужно выполнить:

```powershell
cd labs\webpack2026
docker build -t webpack2026-lab .
docker run --rm -p 3000:3000 webpack2026-lab
```

После этого открыть в браузере:

```text
http://localhost:3000/
```