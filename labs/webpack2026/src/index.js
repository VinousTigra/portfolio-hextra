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