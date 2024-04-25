from . import ponderado
from . import porcentaje_universidad
"""
    VALORES QUE DEBEN RETORNAR DE PONDERADO Y PORCENTAJE DE UNIVERSIDAD
    ###########################################################
    NEM, RANKING, LENGUAJE, M1, M2, CIENCIAS, HISTORIA
"""


def calculo_ponderado():
    while True:
        print("Sistema de ponderado")
        print("1. Perteneces a un colegio Humanista-Cientifico")
        option_menu = int(input("INGRESE LA OPCIÓN\n #: "))
        
        if option_menu == 1:
            lista_ponderado=ponderado.puntajes()
            print('FUNCION CALCULO PONDERADO',lista_ponderado)
            lita_porcentajes = porcentaje_universidad.porcentajes_uni()
            print('FUNCION LISTA PORCENTAJE',lita_porcentajes)
        if option_menu == 2:
            break
        if option_menu == 3:
            break
    
if __name__ == '__main__':
    calculo_ponderado()