#Calcular la fórmula de Pitágoras
import math

cateto_A = float(input("Ingresa cateto A: "))
cateto_B = float(input("Ingresa cateto B: "))

hipotenusa = math.sqrt((cateto_A*cateto_A)+(cateto_B*cateto_B))
cateto_A2 = 3.2
cateto_B2 = 7.8
hipotenusa2 =  math.sqrt((cateto_A2*cateto_A2)+(cateto_B2*cateto_B2))

print('La hipotenusa con los datos del usuario es: {}'.format(hipotenusa))
print('La hipotenusa con los datos asignados es: {}'.format(hipotenusa2))