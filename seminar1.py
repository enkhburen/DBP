#1
list=["python","php","java"]
for i in list:
    print(i)

#2
too=[1,2,3,4,5,6,7,8,9,10]
print(sum(too))

#3
too=[1,2,3,4,5]
urjver = 1
for i in too:
    urjver*=i
print(urjver)

#4
input_string = input()
print("\n")
user_list = input_string.split()

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print(user_list[2]*user_list[-1])

#5
index_of_max = 0
index_of_min = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
print('max utga','=',a[index_of_max])
print('min utga','=',a[index_of_min])

#6
def scount(x):
    y = 0
    for i in x:
        if len(i) > 1:
            if i[0] == i[-1]:
                y = y + 1
    print(y)
x = ['abdba', 'abcd', '121']
scount(x)

#7
x = ['abdba', 'abcd', '121', '121', 'abcd' ]

print(list[set(x)])

#8
def empty(x):
    if len(x) == 0:
        print('Hooson baina')
    else:
        print('Hooson bish baina')

x = [0]
empty(x)

#9
x = [1,2,3,4,5,6,7,8,9,10]
x.pop(4)
x.pop(5)
x.pop(6)
print(x)

#10
x = [1,2,3,4,5,6,7,8,9]
print(x)


#11
x = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
y = list(x)
y.append('pear')
x = tuple(y)
print(x)


#12
x = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
y = list(x)
print(x[2])
print(x[-2])

#13
x = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
a = input()
y = 0
for i in x:
    if a == i:
        y = y + 1
if y == 0:
    print('baihgui')
else:
    print('baina')

#14
x = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
y = list(x)
for i in y:
    print(i)

#15
set_1 = {'orange', 'apple', 'pear','banana'}
set_2 = {'kiwi', 'apple', 'banana','pineapple'}
Newset = set_1.union(set_2)
print(Newset)

#16
set_1 = {'orange', 'apple', 'pear','banana'}
set_2 = {'kiwi', 'apple', 'banana','pineapple'}
Newset = set_1.intersection(set_2)
print(Newset)

#17
x = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
print(len(x))

#18
x = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
a = input()
x.discard(a)
print(x)

#19
x = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
x.clear()
print(x)


#20
x = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
del x
print(x)