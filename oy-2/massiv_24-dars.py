#   append(item) - qiymat qo'shish
#   insert(index, item) - index buyicha element qushish
#   len(uzgaruvchi) - massiv uzunligini chiqaradi
#   index(uzgaruvchi ichidagi item) - indexini chiqaradi
#   extend(uzgaruvchi) - bir massivni 2-massvga qo'shadi.
#   a=b.copy() - 1-massivdan 2-massivga kopiya
#   sort() - tartiblash
#   reverse() - massiv elementlarini teskari tartibga o'giradi
#   remove(item) - biror elementni olib tashlash.  1-uchraganini olib tashlaydi
#   pop(index) - index buyicha uchiradi
#   count(item) -
#   clear() -
#   iter()
#
#

# a= [random.randint(1, 10) for i in range(1, 6) ]      taxminiy 1 dan 10 gacha tanlab, 5 marta sikl ishlaydi
# b= [int(input("a= :)) for i in range(3) ]             necha marta son chiqarish kerak bulsa

#    1-misol.
n = 18
toq = [i for i in range(1, n+1, 2)]
print("toq:  ", toq)

juft = []
for i in range(2, n+1, 2):
    juft.append(i)
print("juft: ", juft)


#    2-misol.
for i in range(n+1):
    a = []
    a.append(2**i)
    print(a)


#    3-misol.                                                   #  ??????????????????????????????????????????
n = 4
A = 4; D = 2
for i in range(1, n+1):
    M = []
    A = A-i + D
    M.append(A)
    print(M)

#    4-misol.                                                       #???????????????????????????????????????????????


#    5-misol.                                   n ta hadli  FIBONACHCHI  sonlari
def Fibonachi(n):
    Fib = [0, 1]
    for i in range(1, n):
        Fib.append(Fib[i-1] + Fib[i])
    return Fib
print(Fibonachi(8))


#    6-misol.                   o'zidan oldingi sonlar yig'indisini chiqarish                  ????????????????????????
n = 7
S= 0
M = [2, 5]          # A=2, B=5
for i in range(0, n+1):
    M.append(sum(M))
print(M)


#    7-misol.                       # elementlrni teskari chiqarish
a = [3,5,44,8,13,5,4,6,2,5,4,64,48,7,9,65]
print(a[-1::-1])

#    8-misol.                           toqlarni chiqarish va nechta toq son borligini aniqlash
a = [2,3,4,5,6,9,10,12,13,15,19]
toq = []
s = 0
for i in a:
    if i%2 != 0:
        toq.append(int(i))
        s += 1
print(toq, "  jami elementlar: %s ta" %(s))


#    9-misol.                          juftlarni kamayish tartibida chiqarish va nechta juft son borligini aniqlash
a = [2,3,4,5,6,9,10,12,13,15,19]
a = a[-1::-1]
toq = []
s = 0
for i in a:
    if i%2 == 0:
        toq.append(int(i))
        s += 1
print(toq, "  jami elementlar: %s ta" %(s))


#    10-misol.                  juftlar usish, toqlar kamayish tartibida chiqarish
a = [2,3,4,5,6,9,10,12,17, 14, 13,8, 15,19, 21, 22]

juft = [];  toq = []
for i in a:
    if i%2 == 0:
        juft.append(int(i))
    if i%2 != 0:
        toq.append(int(i))

print(juft + toq[-1::-1])



#    11-misol.                                  K ga bo'linadigan indexlardagi sonni chiqarish
a = [2,3,4,5,6,9,10,12,17, 14, 13,8, 15,19, 21, 22]
b = []
K = 3; N = 15
for i in range(1, N+1):
    if i%K == 0:
        b.append(a[i])
print(b)


#    12-misol.
a = [2,3,4,5,6,9,10,12,17, 14, 13,8, 15,19, 21, 22]
b = []
n = 15
for i in range(0, n+1, 2):
    b.append(a[i])
print(b)


#    13-misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.












########                                                     FIBONACHI  SONLARI hadigacha son topish
f = [0, 1]
n = 4 #int(input("n= "))
for i in range(1, n-1):
    f.append(f[i-1] + f[i])
print(*f)                       #     * belgisi qavs va vergullarni olib beradi
