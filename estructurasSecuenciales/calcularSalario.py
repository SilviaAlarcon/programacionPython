#Calcular salario bruto y neto

nombre = str(input("Ingrese nombre: "))
horas = float(input("Ingrese horas: "))
precio = float(input("Ingrese precio: "))

salarioBruto = horas *precio
tasa = salarioBruto * 0.25
salarioNeto = salarioBruto - tasa

print("Hola, {}, tu salario bruto es de {}, con una tasa de {}, dando un salario neto de {}".format(nombre, salarioBruto, tasa, salarioNeto))