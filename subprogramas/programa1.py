import math

'''Función sin argumentos para imprimir el siguiente menú:
    MENU
    1 - PI
    2 - ABSOLUTO
    3 - Salir
'''
def menu():
    print('MENÚ \n 1 - PI \n 2 - ABSOLUTO \n 3 - Salir')

#Función con un argumento que devuelva la operación del valor de pi por un valor dado
def multiplicar_por_pi(numero):
    return numero * math.pi

'''Función sin argumentos que pida un número entero e imprima la operación 
anterior (llamando a la función anterior 2).'''
def imprimir_multiplicar_por_pi():
    numero = int(input('Dame un entero: '))
    print(f'El valor de {round(math.pi, 5)} * {numero} es: {round(multiplicar_por_pi(numero), 5)}')

#Función con un argumento que retorne el valor absoluto de un número negativo
def valor_absoluto(numero_negativo):
    return numero_negativo * -1

'''Función sin argumentos que pida un número entero e imprima el valor absoluto
(llamando a la función anterior 4)'''
def imprimir_valor_absoluto():
    numero = int(input('Dame un entero: '))
    if numero < 0 and isinstance(numero, int):
        print(f'El valor absoluto de {numero} es {valor_absoluto(numero)}')
    else:
        print('Ingresa un número entero negativo')

'''Función principal sin argumentos donde el programa se queda en ciclo mientras
se elija una opción válida, de lo contrario manda un mensaje de “Opción inválida” y
vuelve a pedir una opción válida. La única forma de salir es con la opción 3- Salir.
En cada opción solo se hace la llamada a una función (3 y 5), NO se realiza ninguna
operación. Además, se ocupa la función de la biblioteca math (pi).'''
def main():
    
    while True:
        menu()
        opciones = int(input('Selecciona una opción= '))
        if opciones == 1:
            imprimir_multiplicar_por_pi()
            break
        elif opciones == 2:
            imprimir_valor_absoluto()
            break
        elif opciones == 3:
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    #Al final solo se invoca a la función principal. 
    main()