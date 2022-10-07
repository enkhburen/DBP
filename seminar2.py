#1. Өгөгдсөн утга нь палиндром эсэхийг шалгах функц бич.
def palindrome_checker(string):
    reversed_string = string[::-1]
    status=1
    if(string!=reversed_string):
        status=0
    return status

string = input("")
status= palindrome_checker(string)
if(status):
    print("Palindrome baina")
else:
    print("Palindrome bish")

#2. Өгөгдсөн жагсаалтаас том болон жижиг үсгүүдийг тоолох функц бич.
string = input("")

upper, lower = 0, 0
for i in string:
    if(i.is.lower()):
        lower = lower + 1
    elif(i.is.upper()):
        upper = upper + 1
        
print("Tom useg:", upper, "baina")
print("Jijig useg", lower, "baina")

# 4. Өгөгдсөн тооны бактерал олох функц бич.
N=int(input())
res=1
for i in range(1,N+1):
    res*=i
print(res)

#5. Өгөгдсөн жагсаалтыг урвуу болгох функц бич.
s = input("")
print(s[::-1])

#6. Жагсаалтын утгуудын нийлбэрийг олох функц бич.
input_string = input()
print("\n")
user_list = input_string.split()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print(sum(user_list))

#7. Жагсаалтын давхардсан утгуудыг арилгах функц бич.
def remove_same(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
             L1.remove(e)
    return L1

L1 = [1,2,3,4]
L2 = [1,2,5,6]
print(remove_same(L1, L2))

#8. 3 тооны хамгийн ихийг олдог функц бич.
a = int(input())
b = int(input())
c = int(input())
if a<b and c<b:
    print(b)
elif a<c and b<c:
    print(c)
else:
    print(a)