import pandas as pd

ventas_por_grupo            = {'a1':345,'a2':240,'a3':442,'a4':500,'a5':323,'a6':327,'a7':274,'a8':301,'a9':405,'a10':443,'a11':474,'a12':323,'a13':22,'a14':666}
comerciales_por_grupo       = {'a1':35,'a2':24,'a3':24,'a4':40,'a5':32,'a6':38,'a7':37,'a8':39,'a9':40,'a10':41,'a11':42,'a12':42,'a13':39}
ventas_potenciales_grupos   = {'a1':450,'a2':404,'a3':1080,'a4':900,'a5':310,'a6':342,'a7':327,'a8':530,'a9':740,'a10':420,'a11':647,'a12':532,'a13':1022}


s_ventas      = pd.Series(ventas_por_grupo, name="ventaGrupo")
s_comercial  = pd.Series(comerciales_por_grupo, name="comercialGrupo")
sv_potenciales  = pd.Series(ventas_potenciales_grupos, name="ventaPotencial")

n1 = len(ventas_por_grupo)
n2 = len(comerciales_por_grupo)
n3 = len(ventas_potenciales_grupos)



ratioVentasPorAgrupacion = s_comercial / s_ventas
ratioVentas = s_ventas / sv_potenciales

# El ratio de ventas por comercial y agrupación comercial
for clave,valor in ratioVentasPorAgrupacion.items():
    print(f" La agrupación [{clave}] tiene un ratio por comeercial de [{valor}]")


# El ratio de ventas por agrupación frente a su potencial de ventas
for clave,valor in ratioVentas.items():
    print(f" La agrupación [{clave}] tiene un ratio sobre su mercado potencial de [{valor}]")




