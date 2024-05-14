import pandas as pd


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
ventas_por_grupo={'a1':345,'a2':240,'a3':442,'a4':500,'a5':323,'a6':327,'a7':274,'a8':301,'a9':405,'a10':443,'a11':474,'a12':323,'a13':22,'a14':666}
comerciales_por_grupo={'a1':35,'a2':24,'a3':24,'a4':40,'a5':32,'a6':38,'a7':37,'a8':39,'a9':40,'a10':41,'a11':42,'a12':42,'a13':39}
ventas_potenciales_grupos={'a1':450,'a2':404,'a3':1080,'a4':900,'a5':310,'a6':342,'a7':327,'a8':530,'a9':740,'a10':420,'a11':647,'a12':532,'a13':1022}

# =============================================================================
# #Creación de las Series
# =============================================================================
s_ventas        = pd.Series(ventas_por_grupo, name="Ventas por agrupación")
s_comerciales   = pd.Series(comerciales_por_grupo, name="Comerciales por agrupación")
sv_potenciales  = pd.Series(ventas_potenciales_grupos, name="Ventas potenciales por agrupación")



# =============================================================================
# #Creación de mi primer Dataframe
# =============================================================================
#R_com_ventas=s_comerciales/s_ventas
#R_ventas_MP=s_ventas/sv_potenciales
# DF_empresa=pd.DataFrame({'Ventas':s_ventas,'Comerciales' :s_comerciales, 'Mercado_Potencial' : sv_potenciales,'R - ventas':R_com_ventas  ,'R-merc_pot': R_ventas_MP})
DF_empresa=pd.DataFrame({'ventas':s_ventas,"num_comerciales":s_comerciales,"mercado_potencial":sv_potenciales})
print(" \n \n  \t   ****************************  \t  DataFrame Empresa \t  ****************************  \n")
print(DF_empresa, "\n \n \n \n")

print("  \t   ****************************  \t  print(type(DF_empresa)) \t  ****************************  \n")
print(type(DF_empresa), "\n \n  \n  \n")

print("  \t   ****************************  \t  print(DF_empresa.info()) \t  ****************************  \n")
print(DF_empresa.info(), "\n \n \n  \n")



#######
#Vamos a borrar un registro haciendo una búsqueda por valor
#Buscar el registro que tenga Ventas = 666
print("  \t   ****************************  \t  elimino la venta con registro 666 , se elimina el registro A14  \t  ****************************  \n")
indice=DF_empresa[DF_empresa["ventas"] == 666].index
DF_empresa.drop(indice,inplace=True)
print(DF_empresa, "\n \n \n \n")
# DF_empresa_nueva=DF_empresa.drop(indice)
    #Eliminar registros NaN
    # DF_empresa.drop("a14", inplace=True)
    # print(DF_empresa)
    # print("DATAFRAME ORIGINAL")
# print(DF_empresa)
# print("DATAFRAME MODIFICADO")
# print(DF_empresa_nueva)
#######
# DF_empresa_modificado=DF_empresa.drop("a14")
######
# Si volvemos a intentar borrar un índice que no existe, da un Key_error.
# DF_empresa.drop("a14",inplace=True)
print("  \t   ****************************  \t  Añadimos index \t  ****************************  \n")
DF_empresa.reset_index(inplace=True)
print(DF_empresa, "\n \n \n \n")

print("  \t   ****************************  \t CON INDEX  -- Añadimos columna con aumento empleados, R_ventas y R-merc_pot \t  ****************************  \n")
DF_empresa["R-ventas"]=DF_empresa.apply(R_com_ventas,axis=1)
DF_empresa["R-merc_pot"]=DF_empresa.apply(R_ventas_MP,axis=1)
DF_empresa["A_empl"]=DF_empresa.apply(aumento_empleados,axis=1)
print(DF_empresa, "\n \n \n \n")



print("  \t   ****************************  \t SIN INDEX  -- Añadimos columna con aumento empleados, R_ventas y R-merc_pot \t  ****************************  \n")
DF_empresa=DF_empresa.reindex(columns=['ventas',"num_comerciales","A_empl","mercado_potencial","R-ventas","R-merc_pot"])
print(DF_empresa, "\n \n \n \n")














