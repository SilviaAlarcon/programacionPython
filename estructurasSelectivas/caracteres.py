letra = str(input("Dame un caracter: "))

if letra == 's' or 'S' or 'n' or 'N':
    print("{} es correcto".format(letra))
else:
    print("{} es incorrecto".format(letra))