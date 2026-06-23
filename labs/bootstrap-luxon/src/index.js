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