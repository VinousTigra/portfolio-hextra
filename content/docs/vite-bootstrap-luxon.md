---

title: "Bootstrap 5 и Luxon через Vite"
weight: 40
----------

# Интеграция Bootstrap 5 в приложение с Luxon. Этап 3

## Цель работы

Цель работы — создать приложение с использованием Bootstrap 5 и Luxon, но в отличие от предыдущего этапа подключить зависимости не через CDN, а через npm и собрать проект с помощью Vite.

## Создание проекта

Новый проект был создан в отдельной папке:

```powershell
cd "C:\Users\Tigra\Documents\study\4 semester\front\portfolio-hextra"
mkdir vite-bootstrap-luxon
cd vite-bootstrap-luxon
```

Затем был инициализирован npm-проект:

```powershell
npm init -y
```

Были установлены зависимости:

```powershell
npm i bootstrap luxon
npm i -D vite
```

## Команды в package.json

В файл `package.json` были добавлены команды для запуска и сборки проекта:

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview --host 0.0.0.0"
}
```

Команда для построения проекта:

```powershell
npm run build
```

## Структура проекта

В проекте были созданы файлы:

```text
index.html
vite.config.js
src/main.js
src/style.css
```

После сборки Vite создаёт папку:

```text
dist
```

## HTML-разметка

В файле `index.html` была создана страница с Bootstrap-сеткой из трёх колонок. Используется соотношение `2-8-2`: левая колонка `col-2`, центральная колонка `col-8`, правая колонка `col-2`.

В центральной колонке расположена большая красная кнопка `Показать время`.

Также на странице размещена разметка модального окна Bootstrap. Окно можно закрыть с помощью крестика в правом верхнем углу и кнопки `Закрыть` в правом нижнем углу.

## JavaScript-код

В файле `src/main.js` были импортированы Bootstrap, Luxon и пользовательский CSS.

```js
import 'bootstrap/dist/css/bootstrap.min.css';
import Modal from 'bootstrap/js/dist/modal';
import { DateTime } from 'luxon';
import './style.css';

const showTimeButton = document.getElementById('showTimeButton');
const timeOutput = document.getElementById('timeOutput');
const timeModalElement = document.getElementById('timeModal');

const timeModal = new Modal(timeModalElement);

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

Для уменьшения размера бандла был импортирован не весь JavaScript Bootstrap, а только компонент `Modal`:

```js
import Modal from 'bootstrap/js/dist/modal';
```

## Конфигурация Vite

Для корректной публикации собранного приложения в подпапке статического сайта был создан файл `vite.config.js`.

```js
import { defineConfig } from 'vite';

export default defineConfig({
  base: './',
});
```

## Сборка проекта

Сборка проекта была выполнена командой:

```powershell
npm run build
```

Размер полученного бандла по результатам сборки:

```text
dist/index.html                  1.81 kB | gzip: 0.76 kB
dist/assets/index-D4l7to.css   230.16 kB | gzip: 30.78 kB
dist/assets/index-XHdb99ZA.js   93.90 kB | gzip: 29.36 kB
```

Скриншот результата сборки:

<p>
  <img src="/portfolio-hextra/images/vite-bootstrap-luxon/vite-build.png" alt="Результат сборки Vite" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</p>

## Публикация приложения на статическом сайте

После сборки содержимое папки `dist` было скопировано в папку статических файлов Hugo:

```powershell
cd "C:\Users\Tigra\Documents\study\4 semester\front\portfolio-hextra"

New-Item -ItemType Directory -Force static\vite-bootstrap-luxon

Remove-Item -Recurse -Force static\vite-bootstrap-luxon\* -ErrorAction SilentlyContinue

Copy-Item -Recurse vite-bootstrap-luxon\dist\* static\vite-bootstrap-luxon\
```

После этого приложение стало доступно на статическом сайте по адресу:

```text
/portfolio-hextra/vite-bootstrap-luxon/
```

## Результат работы

В результате было создано приложение с интерфейсом, аналогичным предыдущему этапу. На странице расположена большая красная кнопка `Показать время`. После нажатия открывается модальное окно Bootstrap, в котором отображается дата и время, сформированные с помощью Luxon.

<p>
  <img src="/portfolio-hextra/images/vite-bootstrap-luxon/ui-result.png" alt="Внешний вид приложения Vite Bootstrap Luxon" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</p>

## Последовательность действий для запуска

Для запуска проекта в режиме разработки нужно выполнить:

```powershell
cd "C:\Users\Tigra\Documents\study\4 semester\front\portfolio-hextra\vite-bootstrap-luxon"
npm install
npm run dev
```

Для построения проекта нужно выполнить:

```powershell
npm run build
```

Для просмотра собранной версии нужно выполнить:

```powershell
npm run preview
```
