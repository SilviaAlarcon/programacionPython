'''Una función sin argumentos que solicite (usuario) la carga del día (entero), 
mes (cadena en minúsculas) y año (entero) y devuelva una tupla con los valores.'''

def fecha():
    dia = int(input('Ingrese el día: '))
    mes = str(input('Ingrese el mes: '))
    anio = int(input('Ingrese el año: '))
    tupla = (str(dia).zfill(2), mes.upper(), anio)
    imprimir_datos(tupla)

'''Una función con argumentos que reciba la tupla generada e imprima sus datos con 
la siguiente salida.'''

def imprimir_datos(tupla):
    print(f'{tupla[0]} - {tupla[1]} - {tupla[2]}')

#Llamar a las funciones anteriores desde el bloque principal (función main()).
def main():
    fecha()

if __name__ == "__main__":
    main()

'''Nota. Tomar en cuenta el caso del día el usuario ingresa solo un número y 
lo “rellena con un cero”. En el caso del mes el usuario lo ingresa en minúsculas, 
pero la “salida la imprime en mayúsculas”, como se muestra en la salida anterior. 
Además de utilizar funciones como se piden.'''