header = document.querySelector('header');

button = document.querySelector('#red_header');
button.addEventListener('click', headerRed);

function headerRed(){
    header.style.color = "#ff0000";
}