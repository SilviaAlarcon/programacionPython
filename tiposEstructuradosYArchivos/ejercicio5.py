'''Función con argumentos que pida al usuario los nombres de pila de los alumnos de nivel Superior, 
finalizando al ingresar “x”. A continuación, solicita que ingrese los nombres de alumnos de nivel Posgrado, 
finalizando al ingresar “x”.'''

def nombres(alumnos_superior, alumnos_posgrado):    
    while True:
        alumno_nivel_superior = str(input('Ingresa el nombre de pila del alumno de nivel superior: '))
        if alumno_nivel_superior != 'x':
            alumnos_superior.add(alumno_nivel_superior)
        else:           
            while True:
                alumno_nivel_posgrado = str(input('Ingresa el nombre de pila del alumno de nivel posgrado: '))
                if alumno_nivel_posgrado != 'x':
                    alumnos_posgrado.add(alumno_nivel_posgrado)
                else:
                    break
            break

    return alumnos_superior, alumnos_posgrado

'''Función principal sin argumentos realiza:
a) Informa los nombres de todos los alumnos de nivel Superior y los de nivel Posgrado, sin repeticiones.
b) Informa qué nombres se repiten entre los alumnos de nivel Superior y los de nivel Posgrado
c) Informa que nombres de nivel Superior no se repiten en los de nivel Posgrado
d) Informa que nombres de nivel Posgrado no se repiten en los de nivel Superior'''

def main():
    alumnos_superior = set()
    alumnos_posgrado = set()
    nombres(alumnos_superior, alumnos_posgrado)
    a_union = alumnos_superior | alumnos_posgrado
    b_interseccion = alumnos_superior & alumnos_posgrado
    c_diferencia = alumnos_superior - alumnos_posgrado
    d_diferencia = alumnos_posgrado - alumnos_superior
    print(f'Nombre de todos los alumnos: {a_union}')
    print(f'Nombres comunes: {b_interseccion}')
    print(f'Nombres de superior que no se repiten en posgrados: {c_diferencia}')
    print(f'Nombres de posgrado que no se repiten en superior: {d_diferencia}')   

if __name__ == "__main__":
    main()