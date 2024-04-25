from . import ponderado
from . import porcentaje_universidad



"""
    VALORES QUE DEBEN RETORNAR DE PONDERADO Y PORCENTAJE DE UNIVERSIDAD
    ###########################################################
    NEM, RANKING, LENGUAJE, M1, M2, CIENCIAS, HISTORIA
"""


def calculo_ponderacion():
    lista_ponderado=ponderado.puntajes()
    print('FUNCION CALCULO PONDERADO',lista_ponderado)
    lista_porcentajes = porcentaje_universidad.porcentajes_uni()
    print('FUNCION LISTA PORCENTAJE',lista_porcentajes)

    # Calcular ponderación
    if len(lista_ponderado) == len(lista_porcentajes):
        ponderacion = [float(lista_ponderado[i]) * lista_porcentajes[i] for i in range(len(lista_ponderado))]
        print('PONDERACION',ponderacion)
        ponderacion_final = sum(ponderacion)
        print('PONDERACION FINAL',ponderacion_final)
        
if __name__ == '__main__':
    calculo_ponderacion()