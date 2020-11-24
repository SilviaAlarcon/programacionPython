
def par(numero):
    if numero % 2 == 0:
        print('El número es par')
    else:
        print('El número es impar')

def impar(numero):
    for i in range(1, numero + 1, 2):
        print(i, end = ',')

def recursiva(numero):
    contador = 1
    factorial = 1

    for i in range(contador, numero + 1):
        print (f'Valor inicial -> {numero}')
        numero -= 1
    for _ in range (contador, i + 1):
        factorial *= contador
        contador += 1
        print(f'Valor final -> {factorial}')

    