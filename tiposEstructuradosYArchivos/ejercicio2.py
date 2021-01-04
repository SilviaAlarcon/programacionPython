'''2. Realizar un programa que permita crear una lista y almacenar 
los nombres de n países. Ordenar la lista e imprimirla de la siguiente forma:
Ingrese el total de países: 5
Ingrese el nombre del país: México
Ingrese el nombre del país: E.U
Ingrese el nombre del país: España
Ingrese el nombre del país: Alemania
Ingrese el nombre del país: Francia
Total, de países:
5
Países en orden ascendente:
['Alemania', 'E.U', 'España', 'Francia', 'México'] 
Países en orden descendente:
['México', 'Francia', 'España', 'E.U', 'Alemania']
'''

def main():
    paises = int(input('Ingrese el total de países: '))
    total_paises = []
    for _ in range(paises):
        pais = str(input('Ingrese el nombre del país: '))
        total_paises.append(pais)

    total_paises.sort()

    print(f'Total de países: \n{len(total_paises)}')
    print(f'Países en orden ascendentes: \n{total_paises}')

    total_paises.sort(reverse=True)
    print(f'Países en orden descendentes: \n{total_paises}')

if __name__ == '__main__':
    main()