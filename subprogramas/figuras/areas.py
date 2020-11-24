'''En el archivo areas.py tendrá solo el código de cada una de las funciones que nos retornan
el área de un rectángulo, circulo, triangulo y cuadrado (una función con argumentos para
cada figura), así como pi (importar)'''

from math import pi

def rectangulo(base, altura):
    area = base * altura
    return area

def circulo(radio):
    area = pi * (radio ** 2)
    return area

def triangulo(base, altura):
    area = base * altura / 2 
    return area

def cuadrado(lado):
    area = lado * lado
    return area