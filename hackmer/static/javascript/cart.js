const cartButton = document.getElementById('cart')
const cartCloseButton = document.getElementById('close-cart')
const cartContainer = document.getElementById('cart-container')

const toggleCartButtons = [cartCloseButton, cartButton]

toggleCartButtons.forEach(i => i.addEventListener('click', () => {
    cartContainer.classList.toggle('cart--show')
}))

const cartProductsCounter = document.getElementById('cart-products-count')
const cartProductsWrapper = document.getElementById('cart-products-wrapper')

function Cart() {
    this.products = localStorage.getItem('products')
}

Cart.prototype.getProducts = function () {
    return this.products.split(',')
}

Cart.prototype.render = function () {
    if (this.products === true) {
        let products = this.getProducts()
        cartProductsCounter.innerHTML = `${products.length}`
        for (let i in products) {
            console.log(products[i])
        }
    }
}

Cart.prototype.addProduct = function (product) {

}

function Product(id, name, price, picture) {
    this.id = id
    this.name = name
    this.price = price
    this.picture = picture
}

let myProduct = new Product(1, 'Hyper Razer', '$ 150.000', '/media/')

const myCart = new Cart()
myCart.render()