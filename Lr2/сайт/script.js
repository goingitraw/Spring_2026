console.log('script.js загружен');
function showTab(id, button) {
  document.querySelectorAll('section').forEach(section => {
    section.classList.remove('active');
  });

  document.querySelectorAll('nav button').forEach(btn => {
    btn.classList.remove('active');
  });

  document.getElementById(id).classList.add('active');
  button.classList.add('active');
}

let timer;

function showMessage() {
    alert("Подтвердите свою заинтересованность в материале");

    timer = setTimeout(showMessage, 5000);
}

function resetTimer() {
    clearTimeout(timer);
    timer = setTimeout(showMessage, 5000);
}

document.addEventListener("click", resetTimer);

resetTimer();