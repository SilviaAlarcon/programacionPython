#Calcular IMC

nombre = str(input("Ingrese nombre: "))
edad = float(input("Ingrese edad: "))
peso = float(input("Ingrese peso: "))
altura = float(input("Ingrese altura: "))

imc = peso/ altura * altura

print("{}, tu edad es {} y tu peso es de {}".format(nombre, edad, peso))
print("Altura= {}".format(altura))
print("IMC= {}".format(imc))
