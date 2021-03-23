const burgerButton = document.getElementById('burger')
const headerMenu = document.getElementById('menu')


burgerButton.addEventListener('click', () => {
    console.log(1)
    headerMenu.classList.toggle("header__menu--show")
})