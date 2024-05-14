
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#############
# FUNCIONES #
#############

def aumento_empleados(fila):
    num_comerciales = fila['num_comerciales']
    if (fila['R-merc_pot'] < 1.0):
        return round(num_comerciales * 1.1)
    return num_comerciales


def R_com_ventas(fila):
    num_comerciales = fila['num_comerciales']
    s_ventas = fila['ventas']
    return num_comerciales/s_ventas

def R_ventas_MP(fila):
    mercado_potencial = fila['mercado_potencial']
    s_ventas = fila['ventas']
    return s_ventas/mercado_potencial





#################
# FIN FUNCIONES #
#################


# =============================================================================
# #Diccionarios para crear las Series
# =============================================================================
ventas_por_grupo={'a1':345,'a2':240,'a3':442,'a4':500,'a5':323,'a6':327,'a7':274,'a8':301,'a9':405,'a10':443,'a11':474,'a12':323,'a13':22}
comerciales_por_grupo={'a1':35,'a2':24,'a3':24,'a4':40,'a5':32,'a6':38,'a7':37,'a8':39,'a9':40,'a10':41,'a11':42,'a12':42,'a13':39}
ventas_potenciales_grupos={'a1':450,'a2':404,'a3':1080,'a4':900,'a5':310,'a6':342,'a7':327,'a8':530,'a9':740,'a10':420,'a11':647,'a12':532,'a13':1022}

# =============================================================================
# #Creación de las Series
# =============================================================================
s_ventas        = pd.Series(ventas_por_grupo, name="Ventas por agrupación")
s_comerciales   = pd.Series(comerciales_por_grupo, name="Comerciales por agrupación")
sv_potenciales  = pd.Series(ventas_potenciales_grupos, name="Ventas potenciales por agrupación")


# =============================================================================∫
# #Creación matplotlib
# =============================================================================

ventas_labels = ventas_por_grupo.keys()
ventas_values = ventas_por_grupo.values()
plt.ion()
plt.title("Contribución de cada agrupación de comerciales a las ventas totales de la empresa")
# Definimos un vector con el % de ventas grupales
ventas = np.append(s_ventas, 100. - np.sum(s_ventas))

# Etiquetas para los quesitos
explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

plt.pie(ventas_values, labels = ventas_labels, autopct= '%1.1f%%', explode = explode)  #AUTOPCT -> para ver el porcentaje de casa quesito

# Dibuja un gráfico de quesitos



plt.show(block=True)
exit()