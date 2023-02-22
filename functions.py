from data import Productos, Precios, Stock, numero_productos_creados


def mostrar_productos():
    print('========================================')
    print('Lista de productos')
    print('========================================')

    for key, value in Productos.items():
        print('{:<7}{:11}{:<12}{}'.format(
            key,
            value,
            Precios[key],
            Stock[key])
        )

    print('========================================')
    print('[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir')

    opcion = input('Elige opción: ')

    match opcion:
        case '1':
            agregar_producto()
        case '2':
            eliminar_producto()
        case '3':
            actualizar_producto()
        case '4':
            salir()
        case _:
            print('---> No existe esa opción')
            mostrar_productos()


def agregar_producto():
    global numero_productos_creados

    print()
    nombre_producto = input('Escriba nombre del producto: ')
    precio_producto = validacion_flotantes('Ingrese precio del producto')
    stock_producto = validacion_enteros('Ingrese stock del producto')

    numero_productos_creados += 1
    id_producto = numero_productos_creados
    Productos[id_producto] = nombre_producto
    Precios[id_producto] = precio_producto
    Stock[id_producto] = stock_producto

    print('---> Se agregó producto satisfactoriamente')
    print()
    mostrar_productos()


def eliminar_producto():
    print()

    id_producto = validacion_enteros('Escriba id del producto')

    if id_producto in Productos:
        del Productos[id_producto]
        print('---> Producto eliminado satisfactoriamente')
    else:
        print('¡No existe el producto!')

    print()
    mostrar_productos()


def actualizar_producto():
    print()

    id_producto = validacion_enteros('Escriba id del producto')

    if id_producto in Productos:
        print('----------------------------------------')
        print('Nombre del producto: {}'.format(Productos[id_producto]))
        print('Precio del producto: {}'.format(Precios[id_producto]))
        print('Stock del producto: {}'.format(Stock[id_producto]))
        print('----------------------------------------')

        nuevo_nombre_producto = input('Escriba nuevo nombre del producto: ')
        nuevo_precio_producto = validacion_flotantes(
            'Escriba nuevo precio del producto')
        nuevo_stock_producto = validacion_enteros(
            'Escriba nuevo stock del producto')

        Productos[id_producto] = nuevo_nombre_producto
        Precios[id_producto] = float(nuevo_precio_producto)
        Stock[id_producto] = nuevo_stock_producto

        print('---> Se actualizó el producto satisfactoriamente')
    else:
        print('¡No existe el producto!')

    print()
    mostrar_productos()


def salir():
    pass


def validacion_enteros(texto):
    while True:
        try:
            var = int(input('{}: '.format(texto)))
            return var
        except ValueError:
            print('¡¡¡Ingrese un numero entero!!!')


def validacion_flotantes(texto):
    while True:
        try:
            var = float(input('{}: '.format(texto)))
            return var
        except ValueError:
            print('¡¡¡Ingrese un numero!!!')
