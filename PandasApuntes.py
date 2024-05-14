import pandas as pd

primera_serie=pd.Series([1,2,3,4,5])
print (primera_serie)

mi_dict= {'Apple': 147000,
'Samsung': 267937,
'Google': 135301,
'Microsoft': 163000,
'Huawei': 197000,
'Dell': 158000,
'Facebook': 58604,
'Foxconn': 878429,
'Sony': 109700}

empleados=pd.Series(mi_dict, name="Empleados")

print(f"Serie empleados \n{empleados}")
print(f"Índices empleados {empleados.index}")
print(f"Valores empleados {empleados.values}")
for indice, valor in empleados.items():
    print (f"Índice [{indice}] valor [{valor}]")

# empresa=input("Que empresa quieres consultar ? ")

# try:
#     print(empleados[empresa])
# except:
#     print("Esta empresa no existe")

kk=empleados[empleados > 200000]
print(type(kk))
print(empleados[empleados > 200000])

temperaturas=pd.Series([36.9, 37.5, 39.9, 40.0,40.0,36.8, 37.3, 36])
print(temperaturas.value_counts())

# mi_dict_2={'Apple': 274515,
# 'Samsung': 200734,
# 'Google' : 182527,
# 'Microsoft' : 143015,
# 'Huawei' :129184,
# 'Dell' :92224,
# 'Facebook' :85965,
# 'Foxconn' :181945,
# 'Sony' :84893}

# facturacion=pd.Series(mi_dict_2, name="Facturación")







