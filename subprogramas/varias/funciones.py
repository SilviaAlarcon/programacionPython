def contrasenia():
    contrasenia_guardada = 'ISERI'
    contrasenia_usuario = str(input('Ingresa tu contraseña: '))
    if contrasenia_guardada == contrasenia_usuario.upper():
        print('Contraseña correcta')
    else:
        print('Contraseña incorrecta')

def tri_rec():
    numero = int(input('Dame un entero positivo: '))

    for i in range(1, numero +1, 2):
        j = 1
        for j in range(i, 0, -2):
            print(j, end=' ')
        print(' ')

def mcd(numero1, numero2):
    if numero1 < numero2:
        i = numero1
    else:
        i = numero2

    while not(numero1 % i == 0 and numero2 % i == 0):
        i -= 1
    else:
        print(f'El MCD de {numero1} y {numero2} es {i}')
    
            

