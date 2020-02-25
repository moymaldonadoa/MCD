import numpy as np

#Crear arreglo de 2x2
x = np.array([(2,2),(3,3)])
print('El arreglo es', x)

#Devolver dimension/forma del arreglo
x.shape
print('Las dimensiones son', x.shape)

#Crear un arreglo de 100x100x100 lleno de 0s
y = np.zeros((100,100,100))
print(y)

#Crear una matriz identidad de 5x5
b = np.identity(5)
print(b)

#Crear un arreglo de dimension 42x42 lleno de 42
c = np.ones ((42,42))
cmult = c * 42
print(cmult)

#Crear un arreglo de 3x3 con valores random
d = np.random.rand(3,3)
print(d)

#Crear arreglo de 5x4 con valores del 1-20

e = np.arange(20).reshape(5,4)
print (e)

#Llenar un arreglo de 3x3 de los valores q corresponden
#de la fila 3,4 y 5 y la de la columna 1,2,3
f = e[2:5,0:3]
print(f)

#Crear un arreglo con la misma forma q el anterior
g = np.array([[8,9,10],[12,13,14],[15,16,17]])
print(g)
