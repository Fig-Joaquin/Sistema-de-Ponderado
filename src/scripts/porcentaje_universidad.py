
def porcentajes_uni():
    print("Debe ingresar los porcentajes de Universidad")

    nem_porcentaje_universidad = input("Ingrese el porcentaje de NEM de la Carrera: \n #: ")
    ranking_porcentaje_universidad = input("Ingrese el porcentaje de Ranking de la Carrera: \n #: ")
    lenguaje_porcentaje_universidad = input("Ingrese el porcentaje de Lenguaje de la Carrera: \n #: ")
    matematicas_m1_porcentaje_universidad = input("Ingrese el porcentaje de Matematicas M1 de la Carrera: \n #: ")
    print(f'\nLos porcentajes de la Universidad son: \n NEM: {nem_porcentaje_universidad} \n Ranking: {ranking_porcentaje_universidad} \n Lenguaje: {lenguaje_porcentaje_universidad} \n Matematicas M1: {matematicas_m1_porcentaje_universidad}')
    
    # Opción si la persona desea ingresar porcentaje Matematicas M2
    option_m2 = input("La carrera requiere de Matematicas M2: si/no \n #:").lower()
    if option_m2 == 'si':
        matematicas_m2_porcentaje_universidad = input("Ingrese el porcentaje de Matematicas M2 de la Carrera: \n #: ")
        print(f'\nMatematicas M2: {matematicas_m2_porcentaje_universidad}')
    # Opción si la persona desea ingresar porcentaje  Ciencias 
    option_ciencias = input("La carrera requiere de Ciencias: si/no \n #:").lower()
    if option_ciencias == 'si':
        ciencias_porcentaje_universidad = input("Ingrese el porcentaje de Ciencias de la Carrera: \n #: ")
        print(f'\nCiencias: {ciencias_porcentaje_universidad}')
    # Opcion si la persona desea ingresar porcentaje de Historia
    option_historia = input("La carrera requiere de Historia: si/no \n #:").lower()
    if option_historia == 'si':
        historia_porcentaje_universidad = input("Ingrese el porcentaje de Historia de la Carrera: \n #: ")
        print(f'\nHistoria: {historia_porcentaje_universidad}')

if __name__ == '__main__':
    porcentajes_uni()