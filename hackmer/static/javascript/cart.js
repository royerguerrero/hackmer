const cartButton = document.getElementById('cart')
const cartCloseButton = document.getElementById('close-cart')
const cartContainer = document.getElementById('cart-container')
const orderEdit = document.getElementById('order-detail-open-cart')

const toggleCartButtons = [cartCloseButton, cartButton]

if (orderEdit) {
    toggleCartButtons.push(orderEdit)
}

toggleCartButtons.map(i => i.addEventListener('click', () => {
    cartContainer.classList.toggle('cart--show')
}))

const cartProductsCounter = document.getElementById('cart-products-count')
const cartProductsWrapper = document.getElementById('cart-products-wrapper')

const addToCartItem = document.getElementById('add-to-cart-button')

const completePurchase = document.getElementById('complete-the-purchase')
const totalPurchase = document.getElementById('total-purchase')

const formatToCOP = value => {
    return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
        minimumFractionDigits: 0
    }).format(value)
}

function Cart() {
    this.products = {}
    if (this.getProducts()) {
        this.products = this.getProducts()
    }
}

Cart.prototype.calculateTotalPurchase = function () {
    let total = 0
    const products = this.products
    for (i in products) {
        total += parseFloat(products[i].price) * parseFloat(products[i].quantity)
    }

    return formatToCOP(total)
}

Cart.prototype.getProducts = function () {
    return JSON.parse(localStorage.getItem('products'))
}

Cart.prototype.getProduct = function (productId) {
    return this.products[productId]
}

Cart.prototype.addProduct = function (product) {
    if (product.quantity > 10) {
        product.quantity = 10
    } else if (product.quantity < 1) {
        product.quantity = 1
    }

    this.products[product.id] = product
    const message = product.quantity === '1' ? `Has añadido un ${product.name} al carrito.` : `Has añadido ${product.quantity} unidades de ${product.name} al carrito.`

    new Noty({
        text: message,
        layout: 'bottomLeft',
    }).show()
}

Cart.prototype.updateProductQuantity = function (productId, quantity) {
    this.products[productId].quantity = quantity
}

Cart.prototype.deleteProduct = function (productId) {
    delete this.products[productId]
}

Cart.prototype.render = function () {
    const products = this.products
    cartProductsCounter.innerText = `${Object.keys(products).length}`

    if (Object.keys(products).length > 0) {
        let content = ''
        for (let product in products) {
            content += `
            <div class="cart__product" data-id="${products[product].id}">
                <div class="cart__product-content">
                    <img class="cart__product-picture" src="${products[product].picture}" alt="Imagen del producto">
                    <div>
                        <h4 class="cart__product-name">${products[product].name}</h4>
                        <span class="cart__product-price">${formatToCOP(products[product].price * products[product].quantity)} COP</span>
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

        completePurchase.classList.remove('cart__complete-purchase--hide')
        totalPurchase.innerHTML = `Total: ${this.calculateTotalPurchase()} COP`
    } else {
        cartProductsWrapper.innerHTML = 'Aun no has añadido ningun producto 🙃'
        completePurchase.classList.add('cart__complete-purchase--hide')
    }

    const cartProducts = document.querySelectorAll('.cart__product')

    for (let i = 0; i < cartProducts.length; i++) {
        const deleteButton = cartProducts[i].querySelector('.cart__product-delete')
        deleteButton.addEventListener('click', () => {
            this.deleteProduct(cartProducts[i].dataset.id)
            this.save()
        })

        const counterItem = cartProducts[i].querySelector('.cart__product-n-products')
        const counterButtonToAdd = cartProducts[i].querySelector('.cart__product-add-or-subtract:last-child')
        const counterButtonToSubtract = cartProducts[i].querySelector('.cart__product-add-or-subtract:first-child')

        counterButtonToAdd.addEventListener('click', () => {
            if (parseInt(counterItem.textContent) < 10) {
                const newCount = parseInt(counterItem.textContent) + 1
                counterItem.innerHTML = `${newCount}`
                this.updateProductQuantity(cartProducts[i].dataset.id, newCount)
                this.save()
            }
        })

        counterButtonToSubtract.addEventListener('click', () => {
            if (parseInt(counterItem.textContent) > 1) {
                const newCount = parseInt(counterItem.textContent) - 1
                counterItem.innerHTML = `${newCount}`
                this.updateProductQuantity(cartProducts[i].dataset.id, newCount)
                this.save()
            }
        })
    }
    try {
        renderOrder(this)
    } catch (e) {}
}

Cart.prototype.save = function () {
    localStorage.setItem('products', JSON.stringify(this.products))
    this.render()
}

function Product(id, name, price, picture, quantity, discount, realPrice) {
    this.id = id
    this.name = name
    this.price = price
    this.picture = picture
    this.quantity = quantity
    this.discount = discount
    this.realPrice = realPrice
}

const myCart = new Cart()
myCart.render()

if (addToCartItem) {
    addToCartItem.addEventListener('click', () => {
        const product = document.getElementById('product-detail')
        const quantity = document.getElementById('product-quantity')
        const picture = document.getElementsByClassName('product-detail__main-picture')[0]

        const discountEl = document.getElementById('product-discount')
        const discount = discountEl ? discountEl.textContent : 0

        const realPriceEl = document.getElementById('product-real-price')
        const realPrice = realPriceEl ? realPriceEl.textContent : product.dataset.price

        const newProduct = new Product(
            product.dataset.id,
            product.dataset.name,
            product.dataset.price,
            picture.src,
            quantity.value,
            discount,
            realPrice
        )
        myCart.addProduct(newProduct)
        myCart.save()
    })
}