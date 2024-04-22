"""
    Archivo ponderado.py que contiene la función ponderado
"""
# Archivo humanista_cientifico.py
import humanista_cientifico

def validacion_decimal(nota_str):
        try:
            # Si contiene un punto decimal, convertir a float y verificar el rango
            nota_float = float(nota_str)
            if 4 <= nota_float <= 7:
                return nota_str  # Devolver como está si está en el rango
            else:
                return None
        except ValueError:
            return None  # Si hay error en la conversión, devolver None
def validacion_string(nota_str):
            # Si el input es todo dígitos (sin puntos), manejar según la longitud
        if len(nota_str) == 1:
            # Un solo dígito, convertir a float para verificar rango
            if 4 <= float(nota_str) <= 7:
                return nota_str
        elif len(nota_str) == 2:
            # Dos dígitos, formatear como "X.Y"
            nota_convertida = nota_str[0] + '.' + nota_str[1]
            if 4 <= float(nota_convertida) <= 7:
                return nota_convertida
        elif len(nota_str) == 3:
            # Tres dígitos, formatear como "X.YY"
            nota_convertida = nota_str[0] + '.' + nota_str[1:]
            if 4 <= float(nota_convertida) <= 7:
                return nota_convertida
        
def validacion_nota(nota_promedio_alumno):
    nota_str = str(nota_promedio_alumno).strip()  # Asegurarse de eliminar espacios en blanco
    # Verificar si el input contiene un punto decimal
    if '.' in nota_str:
        nota_str = validacion_decimal(nota_str)
        return nota_str
    if nota_str.isdigit():
        nota_str = validacion_string(nota_str)
        return nota_str

    return None  # Devolver None si no cumple ninguna de las condiciones anteriores

def puntajes_humanista_cientifico():
        print("Cálculo de NEM")
        nota_promedio_alumno = input("Ingrese su nota promedio de los 4 años: \n #: ")
        nota_final = validacion_nota(nota_promedio_alumno)
        puntaje = humanista_cientifico.main(nota_final)
        print(f"\nEl puntaje NEM para la nota {nota_final} es: {puntaje}")

        ranking_alumnos = input("Ingrese el ranking de alumno: \n #: ")
        print(f"\nEl ranking de alumnos: {ranking_alumnos}")

        # Puntaje de matematicas del alumno
        puntaje_matematica_m1 = input("Ingrese su puntaje de matematicas M1: \n #: ")
        print(f"\nEl puntaje matematica: {puntaje_matematica_m1}")
        # Puntaje de lenguaje del alumno
        puntaje_lenguaje = input("Ingrese su puntaje de lenguaje: \n #: ")
        print(f"\nEl puntaje matematica: {puntaje_lenguaje}")
        # Puntaje de matematicas M2
        opcion_m2 = input("El alumno rindió la prueba de matemáticas M2? si/no\n #: ").lower()
        if opcion_m2 == "si":
            puntaje_matematica_m2 = input("Ingrese su puntaje de matemáticas M2: \n #: ")
            print(f"\nEl puntaje matematica M2: {puntaje_matematica_m2}")
        # Puntaje de prueba de Ciencias
        opcion_ciencias = input("El alumno rindió la prueba de ciencias? si/no\n #: ").lower()
        if opcion_ciencias == "si":
            puntaje_ciencias = input("Ingrese su puntaje de ciencias: \n #: ")
            print(f"\nEl puntaje ciencias: {puntaje_ciencias}")
        # Puntaje de prueba de Historia y Cs. Sociales
        option_historia = input("El alumno rindió la prueba de historia? si/no\n #: ").lower()
        if option_historia == "si":
            puntaje_historia = input("Ingrese su puntaje de historia: \n #: ")
            print(f"\nEl puntaje historia: {puntaje_historia}")


def ponderado():
    while True:
        print("Sistema de ponderado")
        print("1. Perteneces a un colegio Humanista-Cientifico")
        option_menu = int(input("INGRESE LA OPCIÓN\n #: "))
        
        if option_menu == 1:
            puntajes_humanista_cientifico()
        if option_menu == 2:
            break
        if option_menu == 3:
            break


if __name__ == "__main__":
    ponderado()