from . import calculo 


def calculo_ponderado():
    while True:
        print("Sistema de ponderado")
        print("1. Perteneces a un colegio Humanista-Cientifico")
        print("2. Perteneces a un colegio Tecnico-Profesional")
        print("# Solamente opción 1 disponible #")
        try:
            option_menu = int(input(" -> INGRESE LA OPCIÓN:\n #: "))
            while (option_menu != 1 and option_menu != 2 and option_menu != 3):
                print("--> ¡Por favor, ingrese una opción válida.!")
                option_menu = int(input(" -> INGRESE LA OPCIÓN:\n #: "))
            if option_menu == 1:
                calculo.calculo_ponderacion()
                break
            if option_menu == 2:
                break
            if option_menu == 3:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
if __name__ == '__main__':
    calculo_ponderado()