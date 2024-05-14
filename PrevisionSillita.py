import pandas as pd

# =============================================================================
# FUNCIONES
# =============================================================================

def visualizar_info(df_a_revisar,opcion):
    #Damos un vistazo a los datos para ver "como pintan" ;-)
    if (opcion=="T"):
        print(" \n \n  \t   ****************************  \t  VISUALIZAR DATOS \t  ****************************  \n")
        print(" \n \n  \t   ****************************  \t  HEAD \t  ****************************  \n")
        print(DF_sillitas.head())
        print(" \n \n  \t   ****************************  \t  TAIL \t  ****************************  \n")
        print(DF_sillitas.tail())
        print(" \n \n  \t   ****************************  \t  INFO \t  ****************************  \n")
        print(DF_sillitas.info())
        print(" \n \n  \t   ****************************  \t  DESCRIBE \t  ****************************  \n")
        print(DF_sillitas.describe())
    elif (opcion=="I"):
        print(" \n \n  \t   ****************************  \t  INFO \t  ****************************  \n")
        print(df_a_revisar.info())

def comprobacion_ventas_altas(fila):
    ventas= fila['Sales']
    if (ventas >= 7.5):
        return "Yes"
    else:
        return "No"

# =============================================================================
# PROGRAMA
# =============================================================================

DIRECTORIO_TRABAJO = '/Users/sandyrodriguezaponte/Documents/Programación/BigData/Python/DataScience/Python-DataFrame/datasets_WEKA/'

archivo = DIRECTORIO_TRABAJO+"datos_sillitas_sales.csv"

#Leemos el archivo, cambiando el delimitador de registros
DF_sillitas=pd.read_csv(archivo,delimiter=";")

#Damos un vistazo a los datos para ver "como pintan" ;-)
visualizar_info(DF_sillitas,"T")

#Como vemos que no tenemos la clase que tenemos que predecir
#creando una fucnión que aplicaremos al dataframe a tal efecto
DF_sillitas["Ventas_altas"]=DF_sillitas.apply(comprobacion_ventas_altas,axis=1)
visualizar_info(DF_sillitas,"T")
print("Numero de clases")
print("==========================")
print(DF_sillitas["Ventas_altas"].value_counts())

#DF_sillitas=DF_sillitas.drop("ID")
DF_sillitas.drop("ID",axis=1,inplace=True)
DF_sillitas.drop("Sales",axis=1,inplace=True)
visualizar_info(DF_sillitas,"I")

# Creo CSV
DF_sillitas.to_csv(DIRECTORIO_TRABAJO+"datos_sillitas_clase.csv",index=False)


