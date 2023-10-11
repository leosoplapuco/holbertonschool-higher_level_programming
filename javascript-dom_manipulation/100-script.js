list = document.querySelector(".my_list");
add = document.querySelector("#add_item");
remove = document.querySelector("#remove_item");
clear = document.querySelector("#clear_list");

add.addEventListener("click", () => {
  newItem = document.createElement("li");
  newItem.textContent = "Item";

  list.appendChild(newItem);
});

remove.addEventListener("click", () => {
  list.removeChild(list.lastChild);
});

clear.addEventListener("click", () => {
  list.innerHTML = "";
});
