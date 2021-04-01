const handler = ePayco.checkout.configure({
    key: '11fa8d8829f452cc97328471b12f2a6a',
    test: true
})

const payment = document.getElementById('payment')
payment.addEventListener('click', () => {
    const data = {
        //Parametros compra (obligatorio)
        name: "Vestido Mujer Primavera",
        description: "Vestido Mujer Primavera",
        invoice: "1234",
        currency: "cop",
        amount: "12000",
        tax_base: "0",
        tax: "0",
        country: "co",
        lang: "en",

        //Onpage="false" - Standard="true"
        external: "true",


        //Atributos opcionales
        extra1: "extra1",
        extra2: "extra2",
        extra3: "extra3",
        confirmation: "http://secure2.payco.co/prueba_curl.php",
        response: "http://secure2.payco.co/prueba_curl.php",

        //Atributos cliente
        name_billing: "Andres Perez",
        address_billing: "Carrera 19 numero 14 91",
        type_doc_billing: "cc",
        number_doc_billing: "100000000",
        mobilephone_billing: "3050000000",

        //atributo deshabilitación metodo de pago
        methodsDisable: []
    }

    handler.open(data)
})
