const handler = ePayco.checkout.configure({
    key: '232a768bddccd59f9b91e448915f82ce',
    test: true
})

let orderDetail = 'Tu compra incluye '

for (let i = 0; i < orderDetailsData.products.length; i++) {
    const product = orderDetailsData.products[i]
    orderDetail += `${product.quantity} ${product.name} por el valor de ${formatToCOP(product.price * product.quantity)}`

    if (i !== orderDetailsData.products.length - 1) {
        orderDetail += ', '
    }
}


const data = {
    name: `Compra en hackmer por ${orderDetailsData.customer.name} N° ${orderDetailsData.id}`,
    description: orderDetail,
    invoice: orderDetailsData.id,
    currency: "cop",
    amount: `${orderDetailsData.products.map(product => parseInt(product.price * product.quantity)).reduce((total, i) => total + i)}`,
    tax_base: "0",
    tax: "0",
    country: "co",
    lang: "en",

    external: "true",


    extra1: "extra1",
    extra2: "extra2",
    extra3: "extra3",
    response: `${window.location.origin}/order/${orderDetailsData.id}/`,

    name_billing: orderDetailsData.customer.name,
    address_billing: orderDetailsData.customer.address,
    type_doc_billing: "cc",
    mobilephone_billing: orderDetailsData.customer.phone,

    methodsDisable: ["SP", "DP"]
}

handler.open(data)
myCart.clean()
myCart.save()