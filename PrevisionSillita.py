import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import arff
from sklearn import preprocessing




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
# # visualizar_info(DF_sillitas,"T")


print("Numero de clases")
print("==========================")
print(DF_sillitas["Ventas_altas"].value_counts())


#ACCIONES RESULTADOS DEL ANALISI PREVIO

#DF_sillitas=DF_sillitas.drop("ID")
DF_sillitas.drop("ID",axis=1,inplace=True)
DF_sillitas.drop("Sales",axis=1,inplace=True)
# # visualizar_info(DF_sillitas,"I")

# Creo CSV
#DF_sillitas.to_csv(DIRECTORIO_TRABAJO+"datos_sillitas_clase.csv",index=False)



# Aqui cambiamos el tipo object por category
DF_sillitas["ShelveLoc"] = DF_sillitas["ShelveLoc"].astype("category")
DF_sillitas["Urban"] = DF_sillitas["Urban"].astype("category")
DF_sillitas["US"] = DF_sillitas["US"].astype("category")
DF_sillitas["Ventas_altas"] = DF_sillitas["Ventas_altas"].astype("category")
DF_sillitas["Education"] = DF_sillitas["Education"].astype("category")
visualizar_info(DF_sillitas,"T")
#pasamos a string los "binary string"(UNICODE) SÓLO EN EL CASO QUE SEAN BINARY
# DF_sillitas["ShelveLoc"] = DF_sillitas["ShelveLoc"].str.decode("utf-8")
# DF_sillitas["Urban"] = DF_sillitas["Urban"].str.decode("utf-8")
# DF_sillitas["US"] = DF_sillitas["US"].str.decode("utf-8")
# DF_sillitas["Ventas_altas"] = DF_sillitas["Ventas_altas"].str.decode("utf-8")

# # visualizar_info(DF_sillitas,"I")

##################
# Tratar NULOS   #
##################
#revisamos si hay valores nulos en el dataframe
valores_nulos=DF_sillitas.isnull().sum().sum()
print("valores nulos: [%d]" % valores_nulos)
# hemos decidio que los valos a eliminar (sólo hemos visto 4...)
if valores_nulos>0:
    DF_sillitas= DF_sillitas.dropna()

#Lo grabamos para poder empezar a probar en WEKA las diferentes soluciones
#NO ES OBLIGATORIO HACERLO
DF_sillitas.to_csv(DIRECTORIO_TRABAJO+"datos_sillitas_clase.csv",index=False)

visualizar_info(DF_sillitas,"I")

##################
# Tratar OUTLIERS#
##################
# # plt.ion()
# # plt.figure(figsize=(6,6))
columnas_numericas=DF_sillitas.select_dtypes(include=['number']).columns
i=1
coef_outlier=1.5
for columna in columnas_numericas:
    # print(columnas)
    # # plt.subplot(2,3,i)
    # # plt.boxplot(DF_sillitas[columna], sym = 'ko', whis = coef_outlier)
    # # plt.title(columna)
    i=i+1
    Q1=DF_sillitas[columna].quantile(0.25)
    Q3=DF_sillitas[columna].quantile(0.75)
    RIQ=Q3-Q1
    LimInf=Q1 - (coef_outlier * RIQ)
    LimSup=Q3 + (coef_outlier * RIQ)
    # # print(f"Para [{columna}]: Q1=[{Q1}] Q3=[{Q3}] RIQ[{RIQ}] Liminf[{LimInf}] LimSup[{LimSup}]")
    consulta_outliers=f"{columna} < {LimInf} | {columna} > {LimSup}"
    # # print(consulta_outliers)
    df_outliers=DF_sillitas.query(consulta_outliers)
    # # print(f"En la columna [{columna}] hay [{df_outliers.shape[0]}] outliers")
    DF_sillitas.drop(DF_sillitas[(DF_sillitas[columna] < LimInf) | (DF_sillitas[columna] > LimSup)].index, inplace=True)
    df_outliers=DF_sillitas.query(consulta_outliers)
    # # print(f"COMPROBACIÓN: En la columna [{columna}] hay [{df_outliers.shape[0]}] outliers")


#Generamos nuestro dataframe para escalar, sacando los categóricos,
#para usarlo posteriomente
DF_sillitas_ESC=DF_sillitas.drop(["ShelveLoc","Education","Urban","US","Ventas_altas"],axis=1)
visualizar_info(DF_sillitas_ESC,"I")


#####################
# Tratar CATEGORICOS#
#####################

vector=pd.get_dummies(DF_sillitas["ShelveLoc"],prefix="ShelveLoc")
DF_sillitas=pd.concat ((DF_sillitas,vector), axis=1)
DF_sillitas=DF_sillitas.drop(["ShelveLoc"],axis=1)

vector=pd.get_dummies(DF_sillitas["Urban"],prefix="Urban")
DF_sillitas=pd.concat ((DF_sillitas,vector), axis=1)
DF_sillitas=DF_sillitas.drop(["Urban"],axis=1)

vector=pd.get_dummies(DF_sillitas["US"],prefix="US")
DF_sillitas=pd.concat ((DF_sillitas,vector), axis=1)
DF_sillitas=DF_sillitas.drop(["US"],axis=1)

#Hemos decidio sacar el campo Education por dos razones
# 1.Hemos probado dos algoritmos de selección de atributos, y vemos que
#   En ambos casos sale de los últimos en realción a la clase
# 2.No estaba aumentado mucho la dimensionalidad de nuestra futura capa de entrada en la red neuronal.
DF_sillitas=DF_sillitas.drop(["Education"],axis=1)
# # vector=pd.get_dummies(DF_sillitas["Education"],prefix="Edu")
# # DF_sillitas=pd.concat ((DF_sillitas,vector), axis=1)
# # DF_sillitas=DF_sillitas.drop(["Education"],axis=1)


visualizar_info(DF_sillitas,"T")

#####################
# ESC, NORM o STAND #
##################### 
plt.ion()
fig =plt.figure()
ax1 =fig.add_subplot(2,4,1)
ax2 =fig.add_subplot(2,4,2)
ax3 =fig.add_subplot(2,4,3)
ax4 =fig.add_subplot(2,4,4)
ax5 =fig.add_subplot(2,4,5)
ax6 =fig.add_subplot(2,4,6)
ax7 =fig.add_subplot(2,4,7)

ax1.set_title("Todos juntos")
ax1.plot(DF_sillitas_ESC)
ax2.set_title("CompPtice")
ax2.plot(DF_sillitas_ESC["CompPrice"], linewidth=0, marker="o", color="blue", markersize=6)
ax3.set_title("Income")
ax3.plot(DF_sillitas_ESC["Income"], linewidth=0, marker="+", color="orange", markersize=16)
ax4.set_title("Advertising")
ax4.plot(DF_sillitas_ESC["Advertising"], linewidth=0, marker="*", color="orange", markersize=16)

ax5.set_title("Population")
ax5.plot(DF_sillitas_ESC["Population"], linewidth=0, marker="o", color="blue", markersize=6)
ax6.set_title("Price")
ax6.plot(DF_sillitas_ESC["Price"], linewidth=0, marker="+", color="orange", markersize=16)
ax7.set_title("Age")
ax7.plot(DF_sillitas_ESC["Age"], linewidth=0, marker="*", color="orange", markersize=16)

datos_min_max = preprocessing.MinMaxScaler().fit_transform(DF_sillitas_ESC)
datos_normalizer = preprocessing.Normalizer().transform(DF_sillitas_ESC.T)
datos_normalizer = datos_normalizer.T
datos_standard_scaler = preprocessing.StandardScaler().fit_transform(DF_sillitas_ESC)
datos_robust_scaler = preprocessing.RobustScaler().fit_transform(DF_sillitas_ESC)

fig = plt.figure(figsize=(15, 30))
ax1 = fig.add_subplot(6, 5, 1)
ax2 = fig.add_subplot(6, 5, 2)
ax3 = fig.add_subplot(6, 5, 3)
ax4 = fig.add_subplot(6, 5, 4)
ax5 = fig.add_subplot(6, 5, 5)

ax6 = fig.add_subplot(6, 5, 6)
ax7 = fig.add_subplot(6, 5, 7)
ax8 = fig.add_subplot(6, 5, 8)
ax9 = fig.add_subplot(6, 5, 9)
ax10 = fig.add_subplot(6, 5, 10)

ax11 = fig.add_subplot(6, 5, 11)
ax12 = fig.add_subplot(6, 5, 12)
ax13 = fig.add_subplot(6, 5, 13)
ax14 = fig.add_subplot(6, 5, 14)
ax15 = fig.add_subplot(6, 5, 15)

ax16 = fig.add_subplot(6, 5, 16)
ax17 = fig.add_subplot(6, 5, 17)
ax18 = fig.add_subplot(6, 5, 18)
ax19 = fig.add_subplot(6, 5, 19)
ax20 = fig.add_subplot(6, 5, 20)

ax21 = fig.add_subplot(6, 5, 21)
ax22 = fig.add_subplot(6, 5, 22)
ax23 = fig.add_subplot(6, 5, 23)
ax24 = fig.add_subplot(6, 5, 24)
ax25 = fig.add_subplot(6, 5, 25)

ax26 = fig.add_subplot(6, 5, 26)
ax27 = fig.add_subplot(6, 5, 27)
ax28 = fig.add_subplot(6, 5, 28)
ax29 = fig.add_subplot(6, 5, 29)
ax30 = fig.add_subplot(6, 5, 30)
###
# datos_min_max = pd.DataFrame(datos_min_max, columns=["CompPrice_ESC","Income_ESC","Advertising_ESC","Population_ESC","Price_ESC","Age_ESC"])
# datos_normalizer = pd.DataFrame(datos_normalizer, columns=["CompPrice_ESC","Income_ESC","Advertising_ESC","Population_ESC","Price_ESC","Age_ESC"])
# datos_standard_scaler = pd.DataFrame(datos_standard_scaler, columns=["CompPrice_ESC","Income_ESC","Advertising_ESC","Population_ESC","Price_ESC","Age_ESC"])
# datos_robust_scaler = pd.DataFrame(datos_robust_scaler, columns=["CompPrice_ESC","Income_ESC","Advertising_ESC","Population_ESC","Price_ESC","Age_ESC"])

datos_min_max = pd.DataFrame(datos_min_max, columns=["CompPrice","Income","Advertising","Population","Price","Age"])
datos_normalizer = pd.DataFrame(datos_normalizer, columns=["CompPrice","Income","Advertising","Population","Price","Age"])
datos_standard_scaler = pd.DataFrame(datos_standard_scaler, columns=["CompPrice","Income","Advertising","Population","Price","Age"])
datos_robust_scaler = pd.DataFrame(datos_robust_scaler, columns=["CompPrice","Income","Advertising","Population","Price","Age"])


# crea y personaliza series de datos
ax1.set_title("CompPrice")
ax1.set_ylabel("CompPrice")
ax1.plot(DF_sillitas["CompPrice"], linewidth=0, marker="*", color="red", markersize=4)
ax2.set_title("Min Max")
ax2.plot(datos_min_max["CompPrice"], linewidth=0, marker="*", color="red", markersize=4)
ax3.set_title("Normalizer")
ax3.plot(datos_normalizer["CompPrice"], linewidth=0, marker="*", color="red", markersize=4)
ax3.set_ylim(0, 1)
ax4.set_title("Standard Scaler")
ax4.plot(datos_standard_scaler["CompPrice"], linewidth=0, marker="*", color="red", markersize=4)
ax5.set_title("Robust Scaler")
ax5.plot(datos_robust_scaler["CompPrice"], linewidth=0, marker="*", color="red", markersize=4)

ax6.set_ylabel("Income")
ax6.plot(DF_sillitas["Income"], linewidth=0, marker="*", color="red", markersize=4)
#ax7.set_title("Min Max")
ax7.plot(datos_min_max["Income"], linewidth=0, marker="*", color="red", markersize=4)
#ax8.set_title("Normalizer")
ax8.plot(datos_normalizer["Income"], linewidth=0, marker="*", color="red", markersize=4)
ax8.set_ylim(0, 1)
#ax9.set_title("Standard Scaler")
ax9.plot(datos_standard_scaler["Income"], linewidth=0, marker="*", color="red", markersize=4)
#ax10.set_title("Robust Scaler")
ax10.plot(datos_robust_scaler["Income"], linewidth=0, marker="*", color="red", markersize=4)

ax11.set_ylabel("Advertising")
ax11.plot(DF_sillitas["Advertising"], linewidth=0, marker="*", color="red", markersize=4)
#ax7.set_title("Min Max")
ax12.plot(datos_min_max["Advertising"], linewidth=0, marker="*", color="red", markersize=4)
#ax8.set_title("Normalizer")
ax13.plot(datos_normalizer["Advertising"], linewidth=0, marker="*", color="red", markersize=4)
ax13.set_ylim(0, 1)
#ax9.set_title("Standard Scaler")
ax14.plot(datos_standard_scaler["Advertising"], linewidth=0, marker="*", color="red", markersize=4)
#ax10.set_title("Robust Scaler")
ax15.plot(datos_robust_scaler["Advertising"], linewidth=0, marker="*", color="red", markersize=4)

ax16.set_ylabel("Population")
ax16.plot(DF_sillitas["Population"], linewidth=0, marker="*", color="red", markersize=4)
#ax7.set_title("Min Max")
ax17.plot(datos_min_max["Population"], linewidth=0, marker="*", color="red", markersize=4)
#ax8.set_title("Normalizer")
ax18.plot(datos_normalizer["Population"], linewidth=0, marker="*", color="red", markersize=4)
ax18.set_ylim(0, 1)
#ax9.set_title("Standard Scaler")
ax19.plot(datos_standard_scaler["Population"], linewidth=0, marker="*", color="red", markersize=4)
#ax10.set_title("Robust Scaler")
ax20.plot(datos_robust_scaler["Population"], linewidth=0, marker="*", color="red", markersize=4)

ax21.set_ylabel("Price")
ax21.plot(DF_sillitas["Price"], linewidth=0, marker="*", color="red", markersize=4)
#ax7.set_title("Min Max")
ax22.plot(datos_min_max["Price"], linewidth=0, marker="*", color="red", markersize=4)
#ax8.set_title("Normalizer")
ax23.plot(datos_normalizer["Price"], linewidth=0, marker="*", color="red", markersize=4)
ax23.set_ylim(0, 1)
#ax9.set_title("Standard Scaler")
ax24.plot(datos_standard_scaler["Price"], linewidth=0, marker="*", color="red", markersize=4)
#ax10.set_title("Robust Scaler")
ax25.plot(datos_robust_scaler["Price"], linewidth=0, marker="*", color="red", markersize=4)

ax26.set_ylabel("Age")
ax26.plot(DF_sillitas["Age"], linewidth=0, marker="*", color="red", markersize=4)
#ax7.set_title("Min Max")
ax27.plot(datos_min_max["Age"], linewidth=0, marker="*", color="red", markersize=4)
#ax8.set_title("Normalizer")
ax28.plot(datos_normalizer["Age"], linewidth=0, marker="*", color="red", markersize=4)
ax28.set_ylim(0, 1)
#ax9.set_title("Standard Scaler")
ax29.plot(datos_standard_scaler["Age"], linewidth=0, marker="*", color="red", markersize=4)
#ax10.set_title("Robust Scaler")
ax30.plot(datos_robust_scaler["Age"], linewidth=0, marker="*", color="red", markersize=4)




