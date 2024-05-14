import pandas as pd

circuito = pd.read_csv("DS_circuito_2.csv", delimiter=";")

# print(circuito.head(10))
# print(circuito.tail(10))
print(circuito.info())
print(circuito.describe())