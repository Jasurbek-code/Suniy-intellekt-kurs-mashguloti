#  1-misol.
n = 3
k = 1; s = 0
while k <= n:
    s += 1/k
    k += 1
    print(s)

#  2-misol.
n =5
k, S = 1, 0
while k <= n:
    S += 1/(2*k+1)**2
    k += 1
    print("ikkinchi darajali Summa: ", S)

#  3-misol.
n =5
k, S = 1, 0
while k <= n:
    S += pow(-1, k)/((2*k+1)**k)
    k += 1
    print("Summa: ", S)

#  4-misol.
n, x = 5, 4
i, S = 1, 0
while i <= n:
    S += pow(x, i)/(i)
    i += 1
    print("Summa=", S)
#  5-misol.     faktoriallik
n = 8       # int(input("n="))
i, S, f = 1, 0, 1
while i <= n:
    f *= i
    S += 1/f
    i += 1
print("1/i! Summasi=", S)

#  6-misol.                  kopaytmasi
N = 8    # int(input("N="))
i, f, P = 2,1,1
while i <= N:
    f *= i
    P *= (1 + 1/f)**2
    i += 1
print("Ko'paytmasi=", P)

#  7-misol.                n sondan katta summani qaysi raqamiligini aniqlash
print()
n = 3           # int(input("n="))
S, i = 0, 1
while S <= n:
    S += 1/i
    print("i=", i, "S=", S)
    i += 1
    if S > n:
        print("Aniqlandi:", i)

#  6-misol.                                 raqamni yig'indisi 1-usul
son = 123456789 # int(input("son ="))
S, l = 0, 1
while l < son:
    S += son//l%10
    l *= 10
print(S)

#  7-misol.                                 raqamni yig'indisi 2-usul
son = 123456789
s = 0
while son > 0:
    s += son % 10
    son //= 10
print(s)

#  8-misol.                                 bo'luvchilarini chiqaradi
n = 45 #int(input("son="))
i, s = 1, 0
print("bo'luvchi:", end=" ")
while i <= n:
    if n%i == 0:
        print(i, end=", ")
        s += 1
    i += 1
else:
    print(" >>", s, "ta")

#  9-misol.                   polindrom - teskarisini uqisa ham bir xil
N = 12345678987654321
d = N;  s = 0               # N ni d ga saqlab quyamiz
while N > 0:
    q = N % 10
    N //= 10
    s = s*10 + q
if d == s:           print("Polindrom")
else:                print("Polindrom emas")

#  10-misol.                  Mukammal son
son = 45

i, S = 1, 0
while i < son:
    if son % i == 0:
        print(i, end="+")
        S += i
    i += 1
print("=", S, end=" ")
if S == son:        print(S, son, "Mukammal")
else:        print(S, son, "Mukammal emas")

#  11-misol.                         =============    T U B   sonlar       =================
son = 45
m = 1
while m <= son:
    i, S = 1, 0
    while i <= m:
        if m % i == 0:
            S += 1
        i += 1
    if S == 2:
        print(m, end=" ")
    m += 1
print()

#  12-misol.            pifagor sonlar
Songacha = 15           #int(input("Songacha pifagor sonlarini chiqaradi
c = 1
while c <= Songacha:
    b = 1
    while b < c:
        a = 1
        while a < b:
            if c*c == a*a + b*b:
                print("pifagorlar:     a=", a, "b=", b, "c=", c)
            a += 1
        b += 1
    c += 1

#  13-misol.                ko'paytmani yig'indi orqali ishlash
a, b = 6,6          # int(input("a=")), int(input("b="))
i, C = 0, 0
while i < b:
    C += a
    print(C, a, b)
    i += 1

#  14-misol.
a, b = 8,3          # int(input("a=")), int(input("b="))
C = 0
while a >= b:
    a -= b
    print("bulinuvchi=", a, b)

#  15-misol.            Kabisa yili yoki kabisa yili emasligini topish
Yil = 2000
if Yil%4 == 0:
    print("Kabisa yili")
if Yil%100 == 0 and Yil%400 != 0:
    print("Kabisa yili emas")




##############        7-8-mavzular        #################################

####     if ni bir qatorda yozish usuli                   $$$$$$$$$$$$$$$$$
U = int(input("Son="))
U =U + 1 if U > 0 else 1 if U==0 else U-4
print("U=", U)

#       $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $

#  1-misol.             Devor tirqishiga g'isht sig'ishini yopish
x, y = 10, 15    # devor teshigi o'lchamlari
a,b,c = 2,3,4
if (x//a and y//b) or (x//b and y//a):
    print()

#  2-misol.
N = 123456789            # raqamni teskari tartibda chiqarish
s, Y = 1, 0
while s <= N:
    a = N//s%10
    print(a, end="")
    s *= 10
    Y += a
print("\nYig'indisi=", Y)

# 3-misol.




