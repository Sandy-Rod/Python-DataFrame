import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def conversor_c_f(grados):
	F = (grados *1.8) +32
	return F

# datos de entrenamiento
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

celsius_2=np.arange(-217, 217.1, 0.1, dtype=float)
fahrenheit_2 = ((celsius_2 * 1.8) + 32).astype(float)

# datos_entrada = np.arange(-100, 100, 0.1, dtype=float)
# datos_resultados = (datos_entrada ** 2).astype(float)



#definimos nuestras capas
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
capa_2 = tf.keras.layers.Dense(units=1, input_shape=[1])

#hacemos la estructura del modelo
modelo_100 = tf.keras.Sequential([capa])
modelo_500 = tf.keras.Sequential([capa_2])

# creamos el modelo con la compilación
modelo_100.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)
modelo_500.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial_100 = modelo_100.fit(celsius, fahrenheit, epochs=1000, verbose=True)
historial_500 = modelo_500.fit(celsius_2, fahrenheit_2, epochs=40, verbose=True)
print("Modelo entrenado!")

# vamos a ver como se ha entrenado, ploteando la mágnitud de la pérdida
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial_100.history["loss"],label="100 epochs")
plt.plot(historial_500.history["loss"],label="500 epochs")
plt.legend(loc=0)
plt.show(block=True)

celsius=float(input("Entra los grados Celsius: "))
resultado_100 = modelo_100.predict([celsius])
resultado_500 = modelo_500.predict([celsius])
print(f"Resultado con nuestra fórmula [{conversor_c_f(celsius)}]")
print(f"REsultado de la red neuronal [100]=[{resultado_100}]--[500]=[{resultado_500}]")
