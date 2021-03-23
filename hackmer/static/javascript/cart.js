const cartButton = document.getElementById('cart')
const cartCloseButton = document.getElementById('close-cart')
const cartContainer = document.getElementById('cart-container')

const toggleCartButtons = [cartCloseButton, cartButton]

toggleCartButtons.forEach(i => i.addEventListener('click', () => {
    cartContainer.classList.toggle('cart--show')
}))