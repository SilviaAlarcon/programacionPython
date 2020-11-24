'''En el archivo men_fig.py tendrá el resto del código, así como el archivo anterior
(importación).
En la función principal (main) sin argumentos, donde, el programa se queda en ciclo
mientras se elija una opción válida, de lo contrario manda un mensaje de “Opción inválida”
y vuelve a pedir una opción válida. La única forma de salir es con la opción 5- Salir.'''

from areas import *

def menu():
    return '¿Qué calculo quieres realizar? \n Figuras: \n 1. Rectángulo \n 2. Círculo \n 3. Triángulo \n 4. Cuadrado \n 5. Salir \n'

def main():
    while True:
        opcion = int(input(menu()))

        if opcion == 1:
            base = float(input('Ingresa base: '))
            altura = float(input('Ingresa altura: '))
            print(f'El área es {rectangulo(base, altura)} \n')
        elif opcion == 2:
            radio = float(input('Ingresa radio: '))
            print(f'El área es {round(circulo(radio), 4)} \n')
        elif opcion == 3:
            base = float(input('Ingresa base: '))
            altura = float(input('Ingresa altura: '))
            print(f'El área es {triangulo(base, altura)} \n')
        elif opcion == 4:
            lado = float(input('Ingresa lado: '))
            print(f'El área es {cuadrado(lado)} \n')
        elif opcion == 5:
            break
        else:
            print('Opción inválida \n')

if __name__ == '__main__':
    main()

