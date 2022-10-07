import numpy as np

#1 50-100 1 hemjeest massiv

print(np.arange(50,100))

#2

print(np.ones(10))
print(np.zeros(10))
print(np.array([6,6,6,6,6,6,6,6,6,6]))

#3

print(np.arange(20,32).reshape(3,4))

#4 

print(np.array([[1,0,0],[0,1,0],[0,0,1]]))

#5

print(np.array([[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]]))

#6

array = np.arange(4).reshape(2,2)
array1 = np.arange(4).reshape(2,2)

print((array+array1).sum())
print(array.sum(axis=0) + array1.sum(axis=0))
print(array.sum(axis=1) + array1.sum(axis=1))

#7

Cody = [24000000,14,124]
Joey = [8200000,6,0.2]
Ibrahim = [16600000,12,10]
Xavi = [1600000,4,7]
Yorbe = [4100000, 2, 2]
Armando = [2800000, 7, 3]
Andre = [3400000, 18, 5]
Jordan = [5500000, 9, 1]
Anwar = [9500000, 17, 50]
Philip = [8300000, 2, 0 ]

print(np.array([Cody, Joey, Ibrahim, Xavi, Yorbe, Armando, Andre, Jordan, Anwar, Philip]))
