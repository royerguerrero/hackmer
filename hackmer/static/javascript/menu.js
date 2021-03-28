const burgerButton = document.getElementById('burger')
const headerMenu = document.getElementById('menu')


burgerButton.addEventListener('click', () => {
    headerMenu.classList.toggle('header__menu--show')
    burgerButton.classList.toggle('header__cart--close')
})