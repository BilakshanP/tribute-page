const menu = document.getElementById("menu");
const menuBG = document.getElementById("menu-bg");

Array
    .from(document.getElementsByClassName("menu-item"))
    .forEach(
        (item, index) => {
            item.onmouseover = () => {
                menu.dataset.activeIndex = index;
            }
        }
    );