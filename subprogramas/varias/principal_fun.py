from funciones import *

def menu():
    print('MENU: \n 1- Contraseña \n 2- Tria_Rec \n 3- MCD')

def main():

    while True:
        menu()
        opcion = int(input('¿Qué cálculo quieres realizar? '))

        if opcion == 1:
            contrasenia()
            break
        elif opcion == 2:
            tri_rec()
            break
        elif opcion == 3:
            numero1 = int(input('Ingresa un número: '))
            numero2 = int(input('Ingresa otro número: '))
            mcd(numero1, numero2)
            break
        else:
            print('Opción inválida \n')
        
if __name__ == '__main__':
    main()