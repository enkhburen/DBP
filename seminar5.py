import numpy as np 


#1  for loop

n = int(input('Input: '))

for i in range (n):
    for s in range (i+1):
        print('*', end='')
    print('\r')

#2

x = int(input('Input 2: '))

loopArray = []

for i in range (x):
    loopArray.append('*')
    print(loopArray)


#3 key of max min

students = {
 'Bat': 18,
 'Oyun': 22,
 'Dulam': 21,
 'Suren': 20
}

keys = list(students.keys())

maxVal = students[keys[0]]
minVal = students[keys[0]]
maxKey = ''
minKey = ''

for i in keys:
    if ( students[i] > maxVal ):
        maxVal = students[i]
        maxKey = i
    
    if ( students[i] <= minVal ):
        minVal = students[i]
        minKey = i

print(maxKey, minKey)

#4 sum

array = np.arange(1,1000)

sumOfNumber = 0

for i in array: 
    if ((i % 3 == 0) or (i % 7 == 0)):
        sumOfNumber += i

print(sumOfNumber)