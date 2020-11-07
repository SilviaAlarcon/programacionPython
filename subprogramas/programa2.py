import math

'''Función sin argumentos para imprimir el siguiente menú:
    MENU
    1 - Suma
    2 - Raíz
    3 - Potencia
    4 - Salir
'''
def menu():
    print('MENÚ \n 1 - Suma \n 2 - Raíz \n 3 - Potencia \n 4 - Salir')

#Función con dos argumentos que devuelva la operación de la suma de dos valores
def suma(numero1, numero2):
    return numero1 + numero2

'''Función sin argumentos que pida dos números enteros e imprima la suma de estos
(llamando a la función anterior 2).'''
def suma_usuario():
    numero1 = int(input('Dame un entero: '))
    numero2 = int(input('Dame otro entero: '))
    print(f'La suma de {numero1} + {numero2} es: {suma(numero1, numero2)}')

#Función con un argumento que retorne la operación de la raíz de un valor 
def obtener_raiz(numero):
    return math.sqrt(numero)

'''Función sin argumentos que pida un número entero e imprima la raíz de este
(llamando a la función anterior 4)'''
def obtener_raiz_usuario():
    numero = int(input('Dame un entero: '))
    print(f'La raíz de {numero} es: {round(obtener_raiz(numero), 4)}')

#Función con dos argumentos que devuelva la operación de la potencia de dos valores 
def potencia(numero1, numero2):
    return math.pow(numero1, numero2)

'''Función sin argumentos que pida dos números enteros e imprima la potencia de
estos (llamando a la función anterior 6)'''
def potencia_usuario():
    numero1 = int(input('Dame un entero: '))
    numero2 = int(input('Dame otro entero: '))
    print(f'La potencia de {numero1} ^ {numero2} es: {potencia(numero1, numero2)}')

'''Función principal sin argumentos donde el programa se queda en ciclo mientras
se elija una opción válida, de lo contrario manda un mensaje de “Opción inválida” y
vuelve a pedir una opción válida. La única forma de salir es con la opción 4- Salir.
En cada opción solo se hace la llamada a una función (3, 5 y 7 ), NO se realiza
ninguna operación. Además, se ocupan las funciones de la biblioteca math (raíz y
potencia).'''
def main():
    while True:
        menu()
        opcion = int(input('Selecciona una opción: '))

        if opcion == 1:
            suma_usuario()
            break
        elif opcion == 2:
            obtener_raiz_usuario()
            break
        elif opcion == 3:
            potencia_usuario()
            break
        elif opcion == 4:
            break
        else:
            print('Opción inválida \n')

if __name__ == '__main__':
    #Al final solo se invoca a la función principal. 
    main()