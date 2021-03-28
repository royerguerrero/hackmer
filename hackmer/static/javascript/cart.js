const cartButton = document.getElementById('cart')
const cartCloseButton = document.getElementById('close-cart')
const cartContainer = document.getElementById('cart-container')

const toggleCartButtons = [cartCloseButton, cartButton]

toggleCartButtons.forEach(i => i.addEventListener('click', () => {
    cartContainer.classList.toggle('cart--show')
}))

const cartProductsCounter = document.getElementById('cart-products-count')
const cartProductsWrapper = document.getElementById('cart-products-wrapper')

const addToCartItem = document.getElementById('add-to-cart-button')

function Cart() {
    this.products = []
    if (this.getProducts()) {
        this.products = this.getProducts()
    }
}

Cart.prototype.getProducts = function () {
    return JSON.parse(localStorage.getItem('products'))
}

Cart.prototype.render = function () {
    const products = this.products

    if (products.length > 0) {
        cartProductsCounter.innerText = products.length
        let content = ''
        for (let product in products) {
            content += `
            <div class="cart__product" id="product-number${products[product].id}-in-cart">
                <div class="cart__product-content">
                    <img class="cart__product-picture" src="${products[product].picture}" alt="Imagen del producto">
                    <div>
                        <h4 class="cart__product-name">${products[product].name}</h4>
                        <span class="cart__product-price">$ ${products[product].price} COP</span>
                    </div>
                </div>
                <div class="cart__product-options">
                    <div class="cart__product-counter">
                        <button class="cart__product-add-or-subtract">-</button>
                        <span class="cart__product-n-products">${products[product].quantity}</span>
                        <button class="cart__product-add-or-subtract">+</button>
                    </div>
                    <span class="cart__product-delete"></span>
                </div>
            </div>
            `
        }
        cartProductsWrapper.innerHTML = content
    } else {
        cartProductsWrapper.innerHTML = 'Aun no has añadido ningun producto 🙃'
    }
}

Cart.prototype.addProduct = function (product) {
    this.products.push(product)

    const message = product.quantity === '1' ? `Has añadido un ${product.name} al carrito.` : `Has añadido ${product.quantity} unidades de ${product.name} al carrito.`

    new Noty({
        text: message,
        layout: 'bottomLeft',
    }).show()
}

Cart.prototype.save = function () {
    localStorage.setItem('products', JSON.stringify(this.products))
    this.render()
}

function Product(id, name, price, picture, quantity) {
    this.id = id
    this.name = name
    this.price = price
    this.picture = picture
    this.quantity = quantity
}

const myCart = new Cart()
myCart.render()

addToCartItem.addEventListener('click', () => {
    const product = document.getElementById('product-detail')
    const quantity = document.getElementById('product-quantity')
    const picture = document.getElementsByClassName('product-detail__main-picture')[0]
    const newProduct = new Product(
        product.dataset.id, product.dataset.name, product.dataset.price,
        picture.src, quantity.value
    )
    myCart.addProduct(newProduct)
    myCart.save()
})