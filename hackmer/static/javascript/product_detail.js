const productDescription = document.querySelector('.product-detail__overview')
const longDescription = productDescription.textContent
const productDescriptionSplit = productDescription.textContent.split(' ')

if (productDescriptionSplit.length > 50) {
    const shortDescription = productDescriptionSplit.splice(0, 50).join(' ')
    productDescription.textContent = shortDescription

    const moreButton = document.querySelector('.product-detail__view-more')
    let isToggle = true
    moreButton.addEventListener('click',() => {
        if (!isToggle) {
            productDescription.textContent = shortDescription
            moreButton.textContent = 'Ver toda la descripción'
            isToggle = true
        } else {
            moreButton.textContent = 'Ver menos'
            productDescription.textContent = longDescription
            isToggle = false
        }
    })
}

