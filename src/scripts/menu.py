from . import calculo 


def calculo_ponderado():
    while True:
        print("Sistema de ponderado")
        print("1. Perteneces a un colegio Humanista-Cientifico")
        option_menu = int(input("INGRESE LA OPCIÓN\n #: "))
        
        if option_menu == 1:
            calculo.calculo_ponderacion()
            break
        if option_menu == 2:
            break
        if option_menu == 3:
            break
    
if __name__ == '__main__':
    calculo_ponderado()