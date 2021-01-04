'''Función con un argumento para crear un diccionario que defina como clave 
el nip de una persona y como valor el nombre de pila de esta. La función 
retorna dicho diccionario con dichos datos.'''
def usuario(datos_usuarios):
    numero_usuarios = int(input('Número de usuarios que quieres agregar: '))

    for _ in range(numero_usuarios):
        nip = int(input('Ingrese un NIP: '))
        nombre = str(input('Ingrese el nombre: '))
        datos_usuarios[nip] = nombre

    return datos_usuarios

'''Función con un argumento para imprimir los datos del diccionario completo 
(nip, nombre)'''
def imprimir_datos(datos_usuarios):
    print(f'Datos NIP/Personas: \n{datos_usuarios}')

'''Función con dos argumentos para buscar o consultar el nombre de una persona, 
introduciendo su nip, si este no está registrado nos manda un mensaje de “Error, 
no existe el nip”'''
def buscar_consultar(nip_usuario, datos_usuarios):
    print(datos_usuarios.get(nip_usuario, 'Error, no existe el NIP'))

'''En la función principal sin argumentos (main()), crea del diccionario vacío 
y empieza a cargar los datos de 4 personas, los imprime, busca a la persona, 
mandando llamar a las funciones anteriores como sean requeridas.'''
def main():
    datos_usuarios = {}
    usuario(datos_usuarios)

    imprimir = int(input('Para imprimir los datos presiona 1, para salir presiona 2: \n'))
    if imprimir == 1:
        imprimir_datos(datos_usuarios)
    else:
        print('Datos guardados')

    opcion_buscar = int(input('Para buscar a una persona presiona 1, para salir presiona 2: \n'))   
    if opcion_buscar == 1:
        nip_usuario = int(input('Dame el NIP: '))
        buscar_consultar(nip_usuario, datos_usuarios)
    else:
        print('Fin del programa')

if __name__ == '__main__':
    main()