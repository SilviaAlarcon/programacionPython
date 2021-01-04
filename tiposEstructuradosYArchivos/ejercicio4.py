'''Una función sin argumentos para solicitar (usuario) el nombre de un empleado y su
sueldo, retornar una tupla con los datos.'''

def usuario():
    nombre = str(input('Ingrese nombre: '))
    sueldo = float(input('Ingrese sueldo: '))
    tupla = (nombre.upper(), sueldo)
    return tupla

'''Una función con argumentos que reciba como parámetro dos tuplas con los datos de dos 
trabajadores, imprimiendo el nombre del empleado con el sueldo mayor como se muestra en 
la siguiente salida (según sea el escenario).'''

def usuario_mayor_sueldo(usuario1, usuario2):
    if usuario1[1] > usuario2[1]:
        print(f'El usuario con nombre {usuario1[0]} tiene un sueldo mayor')
    else: 
        print(f'El usuario con nombre {usuario2[0]} tiene un sueldo mayor')

#Llamar a las funciones desde el bloque principal (función main()).
def main():
    usuario1 = usuario()
    usuario2 = usuario()
    usuario_mayor_sueldo(usuario1, usuario2)

if __name__ == '__main__':
    main()