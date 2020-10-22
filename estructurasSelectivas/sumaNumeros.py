numero1 = float(input("Dame un numero: "))
numero2 = float(input("Dame un numero: "))
numero3 = float(input("Dame un numero: "))

suma = numero1 + numero2

if suma == numero3:
    print('{} es la suma de {} + {}'.format(numero3, numero1, numero2))
else:
    print('{} no es la suma de {} + {}'.format(numero3, numero1, numero2))