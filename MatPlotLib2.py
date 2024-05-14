import matplotlib.pyplot as plt
import numpy as np
 
plt.ion()  # Ponemos la sesión como interactiva si no está como tal
plt.axes()  # Coloca un área de gráfico con los valores por defecto
plt.plot(np.exp(np.linspace(0,10,100)))  # Dibuja una exponencial de 0 a 10
plt.axes([0.2,0.55,0.3,0.3], facecolor='red')  
# Dibuja una nueva área de gráfica colocada y con ancho y largo
# definido por [0.2,0.55,0.3,0.3] y con gris como color de fondo
plt.plot(np.sin(np.linspace(0,5,100)), 'b-o', linewidth=1, label = "fig 1")
plt.axes([0.52,0.55,0.3,0.3], facecolor='yellow')  
plt.plot(np.sin(np.linspace(5,2,100)), 'b-o', linewidth=4, label = "fig 2")
plt.axes([0.2,0.2,0.3,0.3], facecolor='green')  
plt.plot(np.sin(np.linspace(7,3,100)), 'b-o', linewidth=15 , label = "fig 3")


plt.show(block=True)
exit()