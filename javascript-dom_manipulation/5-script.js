header = document.querySelector('title')

button = document.querySelector('#update_header')
button.addEventListener('click', updateHeader)

function updateHeader(){
    header.innerHTML = "New Header!!!"
}