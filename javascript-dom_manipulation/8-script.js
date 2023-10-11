API = "https://hellosalut.stefanbohacek.dev/?lang=fr";

fetch(API).then((response) => response.json()).then((json) => {
    APIHello = json.hello;

    hello = document.querySelector('#hello');
    hello.textContent = APIHello;
});