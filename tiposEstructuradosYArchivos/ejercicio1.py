'''1. Realizar un programa que contenga una lista con 10 valores enteros. 
Imprimir cuántos de ellos son superiores a 100.
La salida deberá de ser la siguiente:
La lista de elementos son:
[203, 44, 528, 123, 100, 56, 78, 1000, 2345, 18] 
Total de valores mayores a 100 es:
5
'''

def main():
    valores = [203, 44, 528, 123, 100, 56, 78, 1000, 2345, 18]
    total = []

    for i in valores:
        if i > 100:
            total.append(i)

    print(f'La lista de elementos son: \n{valores}')
    print(f'Total de valores mayores a 100 es: \n{len(total)}')

if __name__ == '__main__':
    main()