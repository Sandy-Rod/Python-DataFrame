import matplotlib.pyplot as plt
import numpy as np
plt.ion()



# plt.figure("scatter")
# plt.scatter(np.random.rand(100), np.random.rand(100))

# for i in range(1,51):
#     plt.subplot(10,5,i)
# plt.subplot(10,5,1)
# # plt.plot([10, 13, 14,15,18], [1,2,3,4,5])
# plt.plot([1,2,3,4,5])
# plt.subplot(10,5,28)
# plt.plot([5,4,3,2,1])


plt.figure("plot1")

#plt.subplot(2,2,1, projection='polar', facecolor='red')
plt.subplot(2,2,1)
plt.plot([1,2,3,4,5])

#plt.subplot(2,2,2, facecolor= 'green')
plt.subplot(2,2,2)
plt.plot([5,4,3,2,1])


# uniendo dos subplots
#plt.subplot(2,1,3)  #se digo que solo tiene una columna """
#plt.plot([1,2,3,4,5,5,4,3,2,1])

#otra solucion
plt.subplot(2, 2, (3, 4))  
plt.plot((0, 2), (0, 5))
plt.plot((5, 3), (0, 5))




plt.show(block=True)

