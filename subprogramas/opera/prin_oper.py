from oper import *

def menu():
    return 'Opciones de cálculo: \n A - Par \n B - Impar \n C - Factorial \n'

def main():
    while True:
        numero = int(input('Ingresa un número: '))
        opcion = str(input(menu()))

        if opcion.lower() == 'a':
            par(numero)
            break
        elif opcion.lower() == 'b':
            impar(numero)
            break
        elif opcion.lower() == 'c':
            recursiva(numero)
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    main()