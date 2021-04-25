const orderContainer = document.getElementById('order-container')
const termAndConditions = document.getElementsByName('terms')[0]
const purchaseButton = document.getElementById('purchase-btn')

const productsOrderContainer = document.getElementById('products-form')


termAndConditions.addEventListener('change', () => {
    if (termAndConditions.checked === true) {
        purchaseButton.classList.remove('button--disable')
        purchaseButton.type = 'submit'
    } else {
        purchaseButton.classList.add('button--disable')
        purchaseButton.type = 'button'
    }
})

const renderOrder = cart => {
    let productsElement = ''

    for (const product in cart.products) {
        const currentProduct = cart.products[product]
        let discountContent = ''

        if (currentProduct['realPrice'] !== currentProduct['price'] ) {
            discountContent = `
                <p class="order-detail__product-discount">
                    ${currentProduct['discount']}
                    <span class="order-detail__product-original-price">${currentProduct['realPrice']}</span>
                </p>
            `
        }

        productsElement += `
        <div class="order-detail__item">
            <div class="order-detail__product">
                <img class="order-detail__product-image" src="${currentProduct['picture']}" alt="${currentProduct['name']}">
                <div>
                    <h3 class="order-detail__product-name">${currentProduct['name']}</h3>
                    <div class="order-detail__product-price">
                        ${formatToCOP(currentProduct['price'])} COP
                        ${discountContent ? discountContent : ''}
                    </div>
                </div>
            </div>
            <p class="order-detail__item-quantity">X${currentProduct['quantity']}</p>
            <p class="order-detail__item-price">${formatToCOP(parseFloat(currentProduct['price']) * parseInt(currentProduct['quantity']))} COP</p>
         </div>
    `

        let productInput = document.createElement('input')
        productInput.setAttribute('type', 'hidden')
        productInput.setAttribute('name', 'products')
        productInput.setAttribute('value', `${currentProduct['id']}:${currentProduct['quantity']}`)

        productsOrderContainer.appendChild(productInput)
    }

    orderContainer.innerHTML = productsElement
}

renderOrder(myCart)