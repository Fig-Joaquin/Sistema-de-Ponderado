def obtener_porcentaje(nombre):
    """
    Solicita al usuario el porcentaje para un aspecto específico de la carrera y valida la entrada.
    Solo acepta números enteros positivos.
    
    Args:
    nombre (str): El nombre del aspecto para el cual se solicita el porcentaje (ej. 'NEM', 'Ranking', etc.).
    
    Returns:
    int: El porcentaje ingresado por el usuario.
    """
    while True:
        try:
            # Solicita al usuario el porcentaje para el aspecto dado.
            porcentaje = int(input(f"Ingrese el porcentaje de {nombre} de la Carrera: \n #: "))
            # Verifica que el porcentaje no sea negativo.
            if porcentaje < 0:
                print("El porcentaje no puede ser negativo. Intente nuevamente.")
            else:
                return porcentaje
        except ValueError:
            # Maneja el caso donde la entrada no puede ser convertida a entero.
            print("Por favor, ingrese un número entero válido.")

def porcentajes_uni():
    """
    Solicita al usuario los porcentajes para diferentes aspectos de la ponderación de la carrera.
    Valida que la suma total de los porcentajes sea exactamente 100%.
    Ajusta la lista de porcentajes según las opciones requeridas por la carrera.
    
    Returns:
    list: Lista de porcentajes validados para cada aspecto de la ponderación.
    """
    # Solicita los porcentajes obligatorios.
    nem_porcentaje_universidad = obtener_porcentaje("NEM")
    ranking_porcentaje_universidad = obtener_porcentaje("Ranking")
    lenguaje_porcentaje_universidad = obtener_porcentaje("Lenguaje")
    matematicas_m1_porcentaje_universidad = obtener_porcentaje("Matematicas M1")
    
    # Inicializa una lista para los porcentajes.
    porcentajes_universidad = [
        nem_porcentaje_universidad,
        ranking_porcentaje_universidad,
        lenguaje_porcentaje_universidad,
        matematicas_m1_porcentaje_universidad
    ]
    
    # Solicita porcentajes opcionales basados en la respuesta del usuario.
    option_m2 = input("La carrera requiere de Matematicas M2: si/no \n #:").lower()
    if option_m2 == 'si':
        porcentajes_universidad.append(obtener_porcentaje("Matematicas M2"))
    
    option_ciencias = input("La carrera requiere de Ciencias: si/no \n #:").lower()
    if option_ciencias == 'si':
        porcentajes_universidad.append(obtener_porcentaje("Ciencias"))
    
    option_historia = input("La carrera requiere de Historia: si/no \n #:").lower()
    if option_historia == 'si':
        porcentajes_universidad.append(obtener_porcentaje("Historia"))

    # Validar que la suma total de los porcentajes sea exactamente 100.
    while sum(porcentajes_universidad) != 100:
        print("La suma total de los porcentajes debe ser exactamente 100%.")
        porcentajes_universidad = [
            obtener_porcentaje("NEM"),
            obtener_porcentaje("Ranking"),
            obtener_porcentaje("Lenguaje"),
            obtener_porcentaje("Matematicas M1")
        ]

        # Solicita nuevamente los porcentajes para los aspectos opcionales si la suma es incorrecta.
        if option_m2 == 'si':
            porcentajes_universidad.append(obtener_porcentaje("Matematicas M2"))
        if option_ciencias == 'si':
            porcentajes_universidad.append(obtener_porcentaje("Ciencias"))
        if option_historia == 'si':
            porcentajes_universidad.append(obtener_porcentaje("Historia"))

    # Imprime y retorna los porcentajes validados.
    print(f"Porcentajes válidos de la universidad: {porcentajes_universidad}")
    return porcentajes_universidad

# Ejecuta la función si el archivo es ejecutado directamente.
if __name__ == '__main__':
    porcentajes_uni()
