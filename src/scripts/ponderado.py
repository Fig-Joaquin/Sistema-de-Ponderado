# Archivo ponderado.py que contiene la función ponderado

from . import humanista_cientifico

def validacion_decimal(nota_str):
    """
    Valida y convierte una cadena con punto decimal a una nota válida.
    """
    try:
        nota_float = float(nota_str)
        if 4 <= nota_float <= 7:
            return nota_str
        else:
            return None
    except ValueError:
        return None

def validacion_string(nota_str):
    """
    Valida y convierte una cadena de dígitos en una nota válida, formateando según la longitud.
    """
    if len(nota_str) == 1:
        nota_convertida = nota_str + ".0"  # Convertir un solo dígito en "X.0"
        if 4 <= float(nota_convertida) <= 7:
            return nota_convertida

    elif len(nota_str) == 2:
        nota_convertida = nota_str[0] + '.' + nota_str[1]  # Formatear como "X.Y"
        if 4 <= float(nota_convertida) <= 7:
            return nota_convertida

    elif len(nota_str) == 3:
        nota_convertida = nota_str[0] + '.' + nota_str[1:]  # Formatear como "X.YY"
        if 4 <= float(nota_convertida) <= 7:
            return nota_convertida

    return None  # Devolver None si no cumple ninguna de las condiciones anteriores

def validacion_nota(nota_promedio_alumno):
    """
    Valida la nota promedio del alumno, devolviendo la nota formateada o None si es inválida.
    """
    nota_str = str(nota_promedio_alumno).strip()

    if '.' in nota_str:
        return validacion_decimal(nota_str)

    if nota_str.isdigit():
        return validacion_string(nota_str)

    return None  # Devolver None si no cumple ninguna de las condiciones anteriores

"""
    Variables de las pruebas
"""

# Ranking : ranking_alumnos
# Prueba de matemáticas M1: puntaje_matematicas_m1
# Prueba de lenguaje: puntaje_lenguaje
# Puntaje de matemáticas M2: puntaje_matematicas_m2
# Puntaje de ciencias: puntaje_ciencias
# Puntaje de historia: puntaje_historia
def puntajes():

        # Declarar variables para ciencias, historia y M2 como None (por si el alumno no rindió esas pruebas)
        puntaje_historia, puntaje_ciencias, puntaje_matematica_m2 = None, None, None

        print("Cálculo de NEM")
        # * NEM
        while True:
            nota_promedio_alumno_str = input("Ingrese su nota promedio de los 4 años: \n #: ")
            
            try:
                # Intentar convertir la entrada a float
                nota_promedio_alumno = float(nota_promedio_alumno_str)
                
                # Validar que la nota esté dentro del rango permitido
                if 4 <= nota_promedio_alumno <= 7:
                    break  # Salir del bucle si la nota es válida
                else:
                    print("La nota debe estar entre 4 y 7")
            
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        nota_final = validacion_nota(nota_promedio_alumno)
        puntaje_nem = humanista_cientifico.main(nota_final)
        
        print(f"\nEl puntaje NEM para la nota {nota_final} es: {puntaje_nem}")

        # * Ranking de alumnos
        while True:
            try:
                ranking_alumnos_str = input("Ingrese el ranking de alumno: \n #: ")
                ranking_alumnos = int(ranking_alumnos_str)
                if 100 <= ranking_alumnos <= 1000:
                    break
                else:
                    print("El ranking debe estar entre 100 y 1000.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        print(f"\nEl ranking de alumnos: {ranking_alumnos}")

        # * Puntaje de matemáticas del alumno (M1)
        while True:
            try:
                puntaje_matematica_m1_str = input("Ingrese su puntaje de matemáticas M1: \n #: ")
                puntaje_matematica_m1 = int(puntaje_matematica_m1_str)
                if 100 <= puntaje_matematica_m1 <= 1000:
                    break
                else:
                    print("El puntaje debe estar entre 100 y 1000.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        print(f"\nEl puntaje de matemáticas M1: {puntaje_matematica_m1}")
        
        # * Puntaje de lenguaje del alumno
        while True:
            try:
                puntaje_lenguaje_str = input("Ingrese su puntaje de lenguaje: \n #: ")
                puntaje_lenguaje = int(puntaje_lenguaje_str)
                if 100 <= puntaje_lenguaje <= 1000:
                    print(f"\nEl puntaje de lenguaje: {puntaje_lenguaje}")
                    break
                else:
                    print("El puntaje debe estar entre 100 y 1000.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            
        # * Puntaje de matemáticas M2
        opcion_m2 = input("¿El alumno rindió la prueba de matemáticas M2? si/no\n #: ").lower()
        while opcion_m2 not in ["si", "no"]:
            print("Por favor, ingrese una opción válida.")
            opcion_m2 = input("¿El alumno rindió la prueba de matemáticas M2? si/no\n #: ").lower()

        if opcion_m2 == "si":
            while True:
                try:
                    puntaje_matematica_m2_str = input("Ingrese su puntaje de matemáticas M2: \n #: ")
                    puntaje_matematica_m2 = int(puntaje_matematica_m2_str)
                    if 100 <= puntaje_matematica_m2 <= 1000:
                        print(f"\nEl puntaje de matemáticas M2: {puntaje_matematica_m2}")
                        break
                    else:
                        print("El puntaje debe estar entre 100 y 1000.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                
        # * Puntaje de prueba de Ciencias
        opcion_ciencias = input("¿El alumno rindió la prueba de ciencias? si/no\n #: ").lower()
        while opcion_ciencias not in ["si", "no"]:
            print("Por favor, ingrese una opción válida.")
            opcion_ciencias = input("¿El alumno rindió la prueba de ciencias? si/no\n #: ").lower()

        if opcion_ciencias == "si":
            while True: 
                try:
                    puntaje_ciencias_str = input("Ingrese su puntaje de ciencias: \n #: ")
                    puntaje_ciencias = int(puntaje_ciencias_str)
                    if 100 <= puntaje_ciencias <= 1000:
                        print(f"\nEl puntaje de ciencias: {puntaje_ciencias}")
                        break
                    else:
                        print("El puntaje debe estar entre 100 y 1000.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                        
        # * Puntaje de prueba de Historia y Cs. Sociales
        opcion_historia = input("¿El alumno rindió la prueba de historia? si/no\n #: ").lower()
        while opcion_historia not in ["si", "no"]:
            print("Por favor, ingrese una opción válida.")
            opcion_historia = input("¿El alumno rindió la prueba de historia? si/no\n #: ").lower()

        if opcion_historia == "si":
            while True:
                try:
                    puntaje_historia_str = input("Ingrese su puntaje de historia: \n #: ")
                    puntaje_historia = int(puntaje_historia_str)
                    if 100 <= puntaje_historia <= 1000:
                        print(f"\nEl puntaje de historia: {puntaje_historia}")
                        break  
                    else:
                        print("El puntaje debe estar entre 100 y 1000.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        # Crear lista para retornar los datos. Se inicializan con los puntajes de NEM, Ranking, Lenguaje y M1
        puntajes_usuario = [puntaje_nem, ranking_alumnos, puntaje_lenguaje, puntaje_matematica_m1, puntaje_matematica_m2, puntaje_ciencias, puntaje_historia]

        # Si la prueba no se realizó, se elimina la variable correspondiente de la lista
        if puntaje_historia is None:
            puntajes_usuario.pop()
        if puntaje_matematica_m2 is None:
            puntajes_usuario.pop(5)
        if puntaje_ciencias is None:
            puntajes_usuario.pop(4)

        return puntajes_usuario
