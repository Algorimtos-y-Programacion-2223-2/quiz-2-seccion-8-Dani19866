'''
Problema 2

La Tienda Super Samancito de la Universidad Metropolitana te ha vuelto a contratar para digitalizar su negocio, 
pero esta vez utilizando una técnica que vieron en Instagram llamada Programación Orientada a Objetos (POO)🖥️, 
por lo que debes desarrollar un software que cumpla con los siguientes requerimientos: 

Módulo administrativo🗃️

-   Agregar productos: Tendrás una estructura de datos con la información del inventario actual de la tienda; 
    esta información debe modelarse como objetos y guardarse en una nueva estructura de datos, que será sobre la 
    que trabajarás el resto del programa. Esta acción debe ocurrir automáticamente apenas se inicia el programa, 
    y debe poder repetirse a partir del menú principal. Hay tres tipos de productos: hogar🏡, ropa👕 y gaming👾.

-   Ver productos: Mostrando por pantalla de forma ordenada cada uno de los productos del local con su detalle 
    (Se tomará en consideración si utilizan el __str__ de la clase❤️)


    ❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗

        Debes trabajar con funciones y con Programación Orientada a Objetos, recordando que cada clase debe definirse en un archivo diferente.

    ❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗
 

'''

products = [
{ "id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800 },
{ "id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600  },
{ "id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25 },
{ "id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5 },
{ "id": 5, "name": "Laptop Gamer", "type": "Gaming", "stock": 11, "price": 2500 },
{ "id": 6, "name": "Nintendo Switch OLED", "type": "Gaming", "stock": 25, "price": 400 },
]
