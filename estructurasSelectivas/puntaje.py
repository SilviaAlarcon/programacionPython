'''Resolver un problema que pida al usuario un puntaje 
y acorde a lo ingresado imprima la 
nota correspondiente.'''

puntaje = int(input("Ingrese su puntaje 0 a 100: "))

if puntaje >= 90:
    print("Obtuviste una A")
elif puntaje >= 80:
    print("Obtuviste una B")
elif puntaje >= 70:
    print("Obtuviste una C")
elif puntaje >= 60:
    print("Obtuviste una D")
elif puntaje < 60:
    print("Obtuviste una F")