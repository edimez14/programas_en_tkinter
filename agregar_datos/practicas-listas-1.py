import os

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0
frutas = []


def imprimir_menu():
    # os.system('cls')
    print(f'''          frutas
		{AGREGAR}) agregar
		{INSERTAR}) insertar
		{MOSTRAR}) mostrar
		{BUSCAR}) buscar
		{ELIMINAR}) eliminar
		{ORDENAR}) ordenar
		{LIMPIAR}) limpiar lista
		{SALIR}) salir
		''')


def agregar_registro():
	print('               agregar')
    nombre = input('nombre: ')
    frutas.append(nombre)
    print('registro agregado con exito')


def insertar_registro():
    print('               insertar')
    nombre = input('nombre: ')
    pos = int(input('posicion: '))
    frutas.insert(pos, nombre)
    print('registro insertado con exito')


def mostrar_registros():
    print('                mostrar')
    if len(frutas) > 0:
        for fruta in frutas:
            print(fruta)
    else:
        print('no se han agregado frutas a la lista')


def buscar_registros():
    print('                 buscar')
    if len(frutas) > 0:
        nombre = input('nombre a buscar: ')
        if nombre in frutas:
            cantidad = frutas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre, inicio)
                print(f'{nombre} se en cuentra en la posicion {pos+1}')
                inicio = pos + 1
        else:
            print(f'{nombre} no a sido agregado a la lista')

    else:
        print('no se han agregado frutas a la lista')


def eliminar_registros():
    print('              eliminar')
    if len(frutas) > 0:
        for i in range(len(frutas)):
            print(f'{i+1}. {frutas[i]}')
        print('0. cancelar')
        pos = int(input(f'posicon a eliminar (1- {len(frutas)})'))
        if 0 < pos <= len(frutas):
            frutas.pop(pos - 1)
            print('registro eliminado con exito')
        else:
            print('no se eliminara ningun registro')
    else:
        print('no se han agregado frutas a la lista')


def ordenar_registros():
    print('               ordenar')
    if len(frutas) > 0:
        frutas.sort()
        print('registros ordenados alfabeticamente')
    else:
        print('no se han frutas a la lista')


def limpiar_registros():
    print('                limpiar')
    frutas.clear()
    print('los registros fueron limpiados con exito')


def main():
    continuar = True
    while continuar:
        imprimir_menu()
        opc = int(input('selecciona un opcion: '))
        # os.system('cls')
        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif opc == MOSTRAR:
            mostrar_registros()
        elif opc == BUSCAR:
            buscar_registros()
        elif opc == ELIMINAR:
            eliminar_registros()
        elif opc == ORDENAR:
            ordenar_registros()
        elif opc == LIMPIAR:
            limpiar_registros()
        elif opc == SALIR:
            print('nos vemos pronto')
            continuar = False
        else:
            print('opcion no valida')
            input('enter para continuar...')


if __name__ == '__main__':
    main()
