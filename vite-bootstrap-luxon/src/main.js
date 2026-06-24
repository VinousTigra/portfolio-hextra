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