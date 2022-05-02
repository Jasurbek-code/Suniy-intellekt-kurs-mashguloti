#   append(item) - qiymat qo'shish
#   insert(index, item) - index buyicha element qushish
#   len(uzgaruvchi) - massiv uzunligini chiqaradi
#   index(uzgaruvchi ichidagi item) - indexini chiqaradi
#   extend(uzgaruvchi) - bir massivni 2-massivga qo'shadi.
#   a=b.copy() - 1-massivdan 2-massivga kopiya
#   sort() - tartiblash
#   reverse() - massiv elementlarini teskari tartibga o'giradi
#   remove(item) - biror elementni olib tashlash.  1-uchraganini olib tashlaydi
#   pop(index) - index buyicha uchiradi
#   count(item) - item necha marta ishlanganini aniqlab sonini chiqaradi
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
a = []
for i in range(n+1):
    a.append(2**i)
print("A=  ", a)

b = [2**i for i in range(n+1)]
print("B=  ", b)


#    3-misol.                                                   Arifmetik progressiya N-hadigacha sonlar
A = 3;  D = 4
N = 5
a = []
for i in range(1, N+1):
    a.append(A)
    A += D
print(a)


#    4-misol.                                                       geometrik funksiya hadi
A = 3;  D = 2
N = 5
a = []
for i in range(1, N+1):
    a.append(A)
    A *= D
print(a)


#    5-misol.                                   n ta hadli  FIBONACHCHI  sonlari
def Fibonachi(n):
    Fib = [0, 1]
    for i in range(1, n):
        Fib.append(Fib[i-1] + Fib[i])
    return Fib
print(Fibonachi(8))


#    6-misol.                   o'zidan oldingi sonlar yig'indisini chiqarish
A = 2; B = 3
n = 5
a = [A, B]
for i in range(n):
    a += [sum(a)]
print(a)



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

b = [i for i in a if i%2 == 1]
print(b, " toq sonlar.")


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
n = 14
for i in range(0, n+1, 2):
    b.append(a[i])
print(b)


#    13-misol.
a = [2,3,4,5,6,9,10,12,17, 14, 13,8, 15,19, 21, 22]
b = []
n = 11
for i in range(1, n+1, 2):
    b.append(a[i])
print(b)



#    14-misol.                                      # indexlari jufti keyin indexi toqlarini chiqarish
a = [2,3,4,5,6,9,10,12,17, 14, 13,8, 15,19, 21, 22]
n = 16
juft = a[::2];  toq = a[1::2]      # juft index va toq indexni alohida qilib olamiz

juft.extend(toq)                   # uzgaruvchilarni birlashtiramiz
print(juft)



#    15-misol.                                      # indexlari toqlari usish tartibida keyin indexi juftlari kamayish tartibida chiqarish
a = [2,3,4,5,6,9,10,12,17, 14, 13,8, 15,19, 21, 22]
n = 16
juft = a[::2][-1::-1];  toq = a[1::2]      # juft index va toq indexni alohida qilib olamiz
#juft = juft[-1::-1]                       # buni ishlatish ham mumkin

toq.extend(juft)                   # uzgaruvchilarni birlashtiramiz
print(toq)


#    17-misol.                                                                                  !!!!!!!!????????
#a = [random.randint(1, 10) for i in range(14)]
a = [6, 1, 10, 6, 1, 9, 2, 3, 1, 10, 7, 10, 9, 1]
print(a)

i = 0; b = []
k = len(a) -1
while i < k:
    b.append(a[i])
    i += 1
    if i == k+1:
        break
    b.append(a[i])
    i += 1
    if i == k+1:
        break
    b.append(a[k])
    k -= 1
    if i == k+1:
        break
    b.append(a[k])
    k -= 1
    if i == k+1:
        break
print(b)



#    18-misol.                                                  # oxirgi raqamdan kichik bulgan birinchi sonni chiqarish
a = [21, 15, 52,4,22,6,9,10,12,17, 14, 13,8, 15,19, 5, 8]

for i in a:
    if a[-1] > i:
        print(i)
        break
else:
        print(0)


#    19-misol.                                      1-elementdan katta oxirgi elementdan kichik bulgam max oxirgi son
a = [10, 15, 52,4,22,6,9,10,12,17, 14, 13,8, 15,19]
c = 0
for i in a:
    if a[-1] > i >= a[0]:
        c = i
if c:
    print(c)
else:
        print(0)


#    20-misol.                                              # K va l oraliqdagi sonlar summasi
a = [10, 15, 52,4,22,6,9,10,12,17, 14, 13,8, 15,19]
summa = 0                               # global uzgaruvchi uchun yaratamiz
def Summa(K, L):
    global summa                        # global uzgaruvchini chaqiramiz
    for i in a[K:L+1]:
        summa += i
    return summa

print(Summa(2, 5))      # 52, 4, 22, 6 = 84


#    21-misol.
a = [10, 15, 52,4,22,6,9,10,12,17, 14, 13,8, 15]
summa = 0
def Summa(K, L):
    global summa
    sanoq = 0
    for i in a[K:L+1]:
        summa += i
        sanoq += 1
    return summa/sanoq, sanoq

print(Summa(2, 5))      # 52, 4, 22, 6 = 84


#    22-misol.                                      # K va L elementlaridan tashqari sonlarni yig'indisi
a = [10, 15, 52,4,22,6,9,10,12,17, 14, 13,8, 15]
K = 3;  L = 11
print((sum(a[:K] + sum(a[L+1:]))))


#    23-misol.
a = [10, 15, 52,4,22,6,9,10,12,17, 14, 13,8, 15]
K = 3;  L = 11
print( (sum(a[:K]) + sum(a[L+1:])) / (len(a[:K] + len(a[L+1:]))))


#    24-misol.                                      Arifmetik progressiya bulsa, ayirmasi, aks holda nolni chiqaruvchi
A = 3;  D = 2
N = 5
a = [3, 5, 7, 9, 11]
for i in range(1, N):
    if a[i] - a[i-1] == D:
        print("D=", D)
    else:
        print(0)
        break


#    25-misol.                                  Geometrik progressiya bulsa, maxraji, aks holda nolni chiqaruvchi
A = 3;  D = 2
N = 5
a = [3, 5, 7, 9, 11]
for i in range(1, N):
    if int(a[i]/a[i-1]) == D:
        print("D=", D)
    else:
        print(0)
        break

#    26-misol.                      ketma ket juft yoki toq son kelsa dasturni tuxtatish
a = [2, 5, 4, 3, 8, 7, 4, 5, 2, 1, 4, 7, 8, 9, 6]
tek = (a[0]%2)                  # 0-indexni anilab olamiz
for i in range(int(len(a))):
    if a[i]%2 == 0:             # juftligini tekshsriadi, birinchi tekshirganda  1 oladi, 2-tekshirganda toq son kelish kerak va
        tek += 1               #                         toq sonda 1 ayriladi
    if a[i]%2 == 1:             # toqligini tekshiradi
        tek -= 1

    if tek == 2 or tek == -1:         # agar ketma-ket juft yoki toq son kelsa 0 va 1 oraliqdan siljiydi va tuxtaydi
        print("natija tuxtadi:", i)
        break

if tek == 0 or tek == 1:
    print("Yakunlandi:", 0)


#    27-misol. 1                     ketma ket musbat va manfiy sonlar kelsa tuxtatish
a = [-2, 5, -4, 3, -8, 4, -5, 2, -1, 4, -7, 8, -9, 6]
tek = (a[0] < 0) + 0                    # musbat yoki manfiyligini tekshirib olamiz

for i in range(int(len(a))):
    if a[i] > 0:
        tek += 1
    if a[i] < 0:
        tek -= 1

    if tek == 2 or tek == -1:           # ketma ketlik buzilsa tartib ortadi yoli kamayadi. shunda dastur tuxtaydi
        print("natija tuxtadi:", i)
        break

if tek == 0 or tek == 1:
    print("Yakunlandi:", 0)

#    27-misol. 2                     ketma ket musbat va manfiy sonlar kelsa tuxtatish.  optimalroq
for i in range(len(a)):
    if a[i]*a[i+1] >= 0:
        print(i, end=" Tugadi")
        break
else:
    print(0)



#    28-29-misol.                          juft indexlilardan eng kichigi, toq indexlilardan eng kattasi
import random
a = [random.randint(1, 20) for i in range(12)]
print("a:", a)
x = True
if x:
    min = a[0];  max = a[1]
    juft = [i for i in a[::2]]
    toq = [i for i in a[::2]]
    x = False
for i in juft:
    if min > i:
        min = i
for i in toq:
    if max < i:
        max = i
print("min=", min, "max=", max)



#    30-misol.                                              o'ng indexidan katta sonlar
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 9, 1]
print("O'ng indexidan katta sonlar: ", end=" ")
for i in range(int(len(a))-1):
    if a[i] > a[i+1]:
        print(a[i], end=", ")


#    31-misol.                                              chap indexidan katta sonlar
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 9, 12]
print("Chap indexidan katta sonlar: ", end=" ")
for i in range(1, int(len(a))):
    if a[i-1] < a[i]:
        print(a[i], end=", ")



#    32-misol.                          local minimum - o'ng va chap qoshnisidan kichik son
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 9, 1]

for i in range(1, int(len(a))-1):
    if a[i-1] > a[i] < a[i+1]:
        print("Local minimum:", a[i], "   index:", i)
        break


#    33-misol.                          local maximum - o'ng va chap qo'shnilardan kattasi
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 12, 2]

for i in range(1, int(len(a))-1):
    if a[i-1] < a[i] > a[i+1]:
        print("Local maximum:", a[i], "   index:", i)


#    34-misol.                              local minim ichidan kattasi
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 9, 11]
maxi = 0
for i in range(1, int(len(a))-1):
    if a[i-1] > a[i] < a[i+1] and maxi < a[i]:
        maxi = a[i]
print("Local minimum ichidan kattasi:", maxi)


#    35-misol.                              local minim ichidan kichigi
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 9, 11]
mini = a[1]
for i in range(1, int(len(a))-1):
    if a[i-1] > a[i] < a[i+1] and mini > a[i]:
        mini = a[i]
print("Local minimum ichidan kichigi:", mini)


#    36-misol.                                      # local max va min bulmaganlarini kattasi
a = [6, 7, 10, 6, 3, 9, 2, 3, 1, 10, 7, 10, 9, 11]      #  7 va 6 - local min va max emas
maxi = 0
for i in range(1, int(len(a))-1):
    if not ((a[i-1] > a[i] < a[i+1] or a[i-1] < a[i] > a[i+1])) and maxi < a[i] :
        maxi = a[i]
print(maxi)




#    37-misol.                          # monoton o'suvchi - ozidan oldingi sondan katta
a = [6, 7, 10, 16, 23, 29, 32, 3, 1, 10, 7, 10, 9, 11]

for i in range(len(a)):
    if a[i-1] < a[i]:
        print(a[i])


#    39-misol.                                                          ???????????????????????????
print('39-misol')

#    40-misol.         uzun yul bn chiqadi                     ??????????


#    41-misol.                                  # qushni hadlarni yig'indisi kattasi
a = [6, 7, 10, 1, 16, 23, 29, 32, 3, 10, 7, 4, 10, 9, 11]
b = lambda x, y: x + y
max = a[0] + a[1]
for i in range(len(a)-1):
    if max < b(a[i], a[i+1]):
        max = b(a[i], a[i+1])
print(max)


#    44-misol.                                  # bir xil sonli element indexini chiqarish
a = [6, 7, 7, 10, 11, 29, 32, 6, 11, 16, 7, 10, 9, 11]
k = 0
for i in range(len(a)):
    k = a.count(a[i])
    if k >= 2:
        print(f"{a[i]} soni {i}-indexda {k} ta.")


#    45-misol.                                      qo'shni hadlar orasida bir-biriga yaqini indexi, modullar ayirmasi kichigini indexi
a = [6, 17, 10, 12, 29, 32, 6, 8, 16, 27, 19, 9, 11]

min = abs(a[0] - a[1])
tartib = 0
for i in range(len(a)-1):
    if min > abs(a[i] - a[i+1]):
        min = abs(a[i] - a[i + 1])
        tartib = i
print(tartib)


#    46-misol.
a = [6, 17, 10, 12, 29, 32, 6, 8, 16, 27, 19, 9, 11]


#    47-misol.                                              bir xil sonlarni chiqaruvchi
import random
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

for i in range(len(a)):
    if a.count(a[i]) > 1:
        print(a[i], a.count(a[i]), "ta")
        break



#    48-misol.                                          bir xil qiymatli element eng ko'p qatnashgani
a = [6, 7, 7, 10, 11, 29, 32, 6, 11, 16, 7, 10, 9, 11]

k = 0; maxi = 0
for i in range(len(a)):
    k = a.count(a[i])
    if k >= 2 and maxi < k:
        maxi = k
print(f"{a[i]} soni {i}-indexda {k} ta.")


#    49-misol.
n = 10  #int(input("n= "))
a = [random.randint(-2*n, 2*n) for i in range(n)]
print("a:  ", a)
for i in range(len(a)):
    if a[i] < 1 or a[i] > n:
        print(i, a[i])
        break
else:
    print(0)


#    50-misol.
a = [6, 7, 10, 16, 23, 29, 32, 3, 1, 10, 7, 10, 9, 11]

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        print(a[i], end=" ")


#    51-misol.                              a va b massivlar sonini almashtirish
a = [6, 7, 10, 12, 17]
b = [72, 54,38,64]
uzunlik_b = len(b); uzunlik_a = len(a)
a = a + b
b = a.copy()

for i in range(uzunlik_a):
    a.remove(a[0])
for i in range(uzunlik_b):
    b.remove(b[-1])

print(" a =  ", a)
print(" b =  ", b)


#    52-misol.                          shart operatorlari
a = [6, 7, 10, 2, 17]
b = []

for i in range(len(a)):
    if a[i] < 5:
        b.insert(i, 2*a[i])
    else:
        b.insert(i, a[i]/2)
print("b= ", *b)


#    53-misol.                        c massiv a va b ni maximalini oladi
a = [6, 7, 10, 2, 17]
b = [21,14,8,4,36]

c = [max(a[i], b[i]) for i in range(len(a))]
print(c)


#    54-misol.                                          a element juftlari b massivda chiqarish
a = [6, 7, 10,21,14,8,4,36, 2, 17, 5]
b = a[::2]

print(len(b))
print(b)



#    55-misol.                                          a element toqlari b massivda chiqarish
a = [6, 7, 10,21,14,8,4,36, 2, 17, 5]
b = a[1::2]

print(len(b))
print(b)

#    56-misol.                                          a element juftlari keyin toqlari b massivda chiqarish
a = [6, 7, 10, 21, 14, 8, 4, 36, 2, 17, 5]
b = [i for i in a if not i%2] + [i for i in a if i%2]
print(b)

#    56-misol.                                          a element toqlari keyin juftlari b massivda chiqarish
a = [6, 7, 10, 21, 14, 8, 4, 36, 2, 17, 5]
b = a[1::2] + a[::2]
print(b)

#    58-misol.
a = [6, 7, 10,21,14,8,4,36, 2, 17, 5]
b = [sum(a)]
print("Yig'indi.  b=", b)

#    59-misol.
a = [6, 7, 10,21,14,8,4,36, 2, 17, 5]
b = [sum(a)/len(a)]

print("Yig'indi.  b=", b)


#    60-misol.
import random
n = 10  #int(input("n= "))
k = 6
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

b = [sum(a[i:]) for i in range(n)]
print(b[0])


#    61-misol.
n = 10  #int(input("n= "))
k = 5
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

b = [sum(a[n-i-1:k:-1]) for i in range(n)]
print(b)


#    64-misol.
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11]

d = a + b + c
print(d)

#    65-misol.
a = [6, 7, 10,21,14,8,4,36, 2, 17, 5]
k = 3
b = [a[i]*k for i in range(len(a))]
print(b)

#    66-misol.                                      1-uchragan juft sonni boshqa juft sonlarga ko'paytirish
a = [7, 10,21,14,8,4,36, 2, 17, 5, 9]
k = 1
for i in range(0, len(a)+1, 2):
    if i%2 == 0 and a[i]%2 == 0:
        k = a[i]
        break
print("k= ", k)

b = [a[i]*k for i in range(0, len(a)+1, 2)]
print(b)


#    67-misol.                                      1-uchragan toq sonni boshqa toq sonlarga ko'paytirish
a = [7, 10,21,11,8,4,35, 2, 17, 5, 9]
k = 1
for i in range(1, len(a), 2):
    if i%2 == 1 and a[i]%2 == 1:
        k = a[i]
print("k= ", k)

a = [a[i]*k for i in range(0, len(a)+1, 2)]
print(a)


#    68-misol.                                          min va maxi sonlarini o'rnini almashtirish
a = [7, 10,21,11,8,43,35, 20, 17, 5, 9]
print(a)
mini = a.index(min(a)); maxi = a.index(max(a))
replace = a[mini]
a[mini] = a[maxi]
a[maxi] = replace
print(a)


#    69-misol.
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

for i in range(0, n, 2):
    a[i], a[i+1] = a[i+1], a[i]
print(a)



#    70-misol.                                  k dan h gacha elementlarni almashtirish
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

k = 3; h = 6
a = a[:k+1] +a[h-1: k:-1] + a[h:]



#    71-misol.                                              teskari tartibda chiqarish
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

for i in range(1, int(len(a))+1):
    b = a[int(len(a)) - i]
    print(b, end=" ")



#    72-misol.                                  k dan h gacha elementlarni almashtirish
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

k = 3; h = 6
a = a[:k+1] +a[h-1: k:-1] + a[h:]


#    73-misol.                                          k va h sonlarini orasidagilarni almashtirish
a = [0,1,2,3,4,5,6,7,8,9,10,11]
print(a)
k = 4; h = 9
a = a[:k] + a[h - len(a) -1 : k : -1 ] + a[h:]
print(a)



#    74-misol.                                      eng katta va eng kichik elementlari orasidagilar 0 ga aylantirlsin
n = 10  #int(input("n= "))
a = [random.randint(-10, n) for i in range(n)]
print("a:  ", a)

mini, maxi = a[0], a[0]

for i in a:
    if i > maxi:
        maxi = a.index(i)
    elif i < mini:
        mini = a.index(i)
b = a[:mini] + a[mini:maxi+1] + a[maxi:]
print(mini, maxi,  b)


#    75-misol.
n = 10  #int(input("n= "))
a = [random.randint(-10, n) for i in range(n)]
print("a:  ", a)
b = a.copy();  b[0] = 0

for i in range(1, len(a)-1):
    if a[i-1] < a[i] > a[i+1]:
        continue
    else:
        b[i] = 0
del a
print(b)


#    76-misol.                                  lokal maximumlarni 0 ga aylantiruvchi
n = 10  #int(input("n= "))
a = [random.randint(-10, n) for i in range(n)]
print("a:  ", a)
b = a.copy();  b[0] = 0

for i in range(1, len(a)-1):
    if a[i-1] < a[i] > a[i+1]:
        b[i] = 0
del a
print(b)


#    77-misol.                                  local minimumni kvadratga oshiruvchi
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)
b = a.copy();  b[0] = 0

for i in range(1, len(a)-1):
    if a[i-1] > a[i] < a[i+1]:
        b[i] = a[i]**2
del a
print(b)


#    78-misol.
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

for i in range(len(a)-1):
    a[i] = (a[i] + a[i+1])/2
print(a)


#    79-misol.                                          yonidagi element bn almashadi. a[0] -> a[1] ga a[1] -> a[2] ga
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

for i in range(len(a)-1):
    a[i] = a[i+1]
else:
    a.remove(a[i])
print("    ", a)


#    80-misol.                                          yonidagi element bn almashadi. a[n] -> a[n-1] ga a[n-1] -> a[n-2] ga
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

b = a[1:] + a[:1]
print(b)


#    81-misol.                                          k ta o'ngga surish
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

k = 6
b = a[k:] + a[:k]
print(b)



#    83-misol.
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

b = a[-1:-2:-1] + a[:len(a)-1]
print("    ", b)


#    84-misol.
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

b = a[1:len(a)] + a[0:1]
print("    ", b)



#    85-misol.
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

k = 6
b = a[len(a) -k:] + a[:len(a) - k]      # b = a[k:] + a[:k]
print("    ", b)



#    89-misol.                              # sortlash algoritmi
n = 10  #int(input("n= "))
a = [i for i in range(n)]
a[random.randint(0, n)] = int(input("a= "))
print(a)

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        t = a[i+1]
        a.pop(i+1)
        break
for i in range(len(a)-1):
    if t > a[i]:
        pass
    else:
        a.insert(i, t)
        break
print(a)



#    90-misol.
a = [5,4,8,9,3,21,5,4,8,7,9,3]
k = 6
a.pop(3)
print("    ", a)


#    91-misol.
k = 3;  m = 6
for i in range(k, m+1):
    a.pop(k)
print("    ", a)

#    92-misol.                                      toq sonlarni uchirish
#a = [a.remove(i) for i in a if i%2 == 0]
a = [5,4,8,9,3,21,5,4,8,7,9,3]
print(a)

while i < len(a):
    if a[i]%2 == 1:
        a.pop(i)
        i -= 1
    i += 1
print(a)


#    93-misol.                                      juftlarni uchirish
a = [3,15,8,4,89,6,3,1,5,45,6,3]
print(a)

while i < len(a):
    if a[i]%2 == 0:
        a.pop(i)
        i -= 1
    i += 1
print(a)


#    94-misol.                                  toq indexlilarni uchirish
n = 10  #int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

n = 10  # int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)
i = 0
while i < len(a):
    if i % 2 == 0:
        a.pop(i)
    i += 1

print(a)


#    95-misol.


#    96-misol.                                  bir xil sonlarni uchirish
a = [5,4,8,9,3,21,5,4,8,5,7,9,4]

i = 0
while i < len(a):
    t = a.count(a[i])

    if t >= 2:
        while t > 1:
            a.remove(a[i])
            t -= 1
    i += 1
    print(i-1)
print(a)


#    97-misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    -misol.


#    105-misol.
a = [5,4,8,9,3,21,5,4,8,5,7,9,4]
k = 21; m = 3
print(*a)

for i in range(m):
    a,insert(k+1, 0)
# a = a[:k+1] + [0]*n + a[k+1:]
print(a)


#    109-misol.                                                 manfiy sonlardan keyin 0 sonini chiqaradi
n = 10  # int(input("n= "))
a = [random.randint(0, n) for i in range(n)]
print("a:  ", a)

i = 0
while i < len(a):
    if a[i] < 0:
        a.insert(i+1, 0)
    i += 1

print(a)




#    112-misol.                                              sortlash algoritmi
#a = [3,5,-5,-1,6,4,-7,7,6,-1,6,7,2,2]
b = []

while a:
    min = a[0]
    for i in range(len(a)):
        if min > a[i]:
            min = a[i]
    b.append(min)
    a.remove(min)
print("sortlash 1-usul.", b)


for i in range(len(a)):
    for j in range(len(a) - 1 -i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("sortlash 2-usul.")


for i in range(len(a)-1):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("sortlash 3-usul.")




#    -misol.


#    -misol.


#    -misol.


#    116-misol.                                     ketma ket kelgan sonlarni nechtaligini c massivga yuklash
a = [3,5,5,5,6,4,7,7,6,6,7,2,2]
b = []; c = []
s = 1
for i in range(1, len(a)):
    if a[i-1] == a[i]:
        s += 1
    else:
        b.append(a[i-1])
        c.append(s)
        s = 1
b.append(a[len(a)-1])
c.append(s)
print(b, c)



#    117-misol.
a = [3,5,5,5,6,4,7,7,6,6,7,2,2]
b = []; c = []
s = 1; k = 5
for i in range(1, len(a)):
    if a[i-1] == a[i]:
        s += 1
    else:
        b.append(a[i-1])
        c.append(s)
        s = 1
b.append(a[len(a)-1])
c.append(s)

a = []
for i in range(len(b)):
    if k == i+1:
        c[i] *= 2
    for j in range(c[i]):
        a.append(b[i])
print(a)




#    122-misol.
k = 4
print(a)

b = []; c = []
s = 1

for i in range(1, len(a)):
    if a[i-1] == a[i]:
        s += 1
    else:
        b.append(a[i-1])
        c.append(s)
        s = 1
b.append(a[len(a) - 1])
c.append(s)
print(b)
print(s)

a = []
for i in range(len(b)):
    if k == i+1:
        continue
    for j in range(c[i]):
        a.append(b[i])
print(a)



#    124-misol.

k = 7
print(a)

b = []; c = []
s = 1

for i in range(1, len(a)):
    if a[i-1] == a[i]:
        s += 1
    else:
        b.append(a[i-1])
        c.append(s)
        s = 1
b.append(a[len(a) - 1])
c.append(s)
print(b)
print(s)

if not k > len(b):
    b[k], b[-1] = b[-1], b[k-1]
    c[k], c[-1] = c[-1], c[k-1]

a = []
for i in range(len(b)):
    for j in range(c[i]):
        a.append(b[i])
print(a)



#    127-misol.

k = 7
print(a)

b = []; c = []
s = 1

for i in range(1, len(a)):
    if a[i-1] == a[i]:
        s += 1
    else:
        b.append(a[i-1])
        c.append(s)
        s = 1
b.append(a[len(a) - 1])
c.append(s)
print(b)
print(s)

if not k > len(b):
    b[k], b[-1] = b[-1], b[k-1]
    c[k], c[-1] = c[-1], c[k-1]

a = []
for i in range(len(b)):
    for j in range(c[i]):
        if c[i] > k:
            a.append(b[i])
            break
print(a)


#    129-misol.

def uzunlik(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)**0.5

x = [3,5,-5,-1,6,4,-7,7,6,-1,6,7,2,2]
y = [3,5,-5,-1,6,4,7,-1,7,2]
print(x)
print(y)

c = []
for i in range(len(a)):
    s = 0
    for j in range(len(a)):
        s += uzunlik(x[i],y[i], x[j],y[j])
    c.append(s)
a = c.index(min(c))
print(a)













########                                                     FIBONACHI  SONLARI hadigacha son topish
f = [0, 1]
n = 4 #int(input("n= "))
for i in range(1, n-1):
    f.append(f[i-1] + f[i])
print(*f)                       #     * belgisi qavs va vergullarni olib beradi


########                                D o' s t    sonlar
#from random import randrange
a = [randrange(2, 10000, 2) for i in range(100)]
b = [randrange(2, 10000, 2) for i in range(100)]
c = []

for i in a:
    S = 0
    for j in range(1, i//2 + 1):
        if i%j == 0:
            S += j
    if S in b:
        c.append(i)
        c.append(S)
print(c)

