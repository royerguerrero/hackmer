const mainProductPicture = document.querySelector('#product-detail-main-image > img')
const productPictures = document.querySelectorAll('.product-detail__thumbnail > img')

mainProductPicture.src = productPictures[0].src

for (let i = 0; i < productPictures.length; i++) {
    productPictures[i].addEventListener('click', () => {
        mainProductPicture.src = productPictures[i].src
    })
}