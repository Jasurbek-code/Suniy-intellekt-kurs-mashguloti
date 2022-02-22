#  1-misol.
N = 1   # int(input("Sikllar soni:"))
mini = 9; maxi = 0
for i in range(N):
    a = 3  #int(input("a="))
    if a < mini:
        mini = a
    if a > maxi:
        maxi = a

print("min:", mini, "  max:", maxi)

#  2-misol.                     a, b tomonli to'g'rito'rtbutrchak
N = 1
x = True
for i in range(N):
    a, b = int(input("a=")), int(input("b="))
    if x:
        kichik_yuza = a*b
        x = False
    if kichik_yuza > a*b:
        kichik_yuza = a*b
print("kichik yuzalisi:", kichik_yuza)

#  3-misol.                     eng katta peremeterli turtburchak
N = 1
per_katta = 0
for i in range(N):
    a, b = 2,3  #int(input("a=")), int(input("b="))
    if 2*(a+b) > per_katta:
        per_katta = 2*(a+b)
print("Peremetri kattasi:", per_katta)

#  4-misol.                 sonni eng kichigi tartibini aniqlash
N = 1
min = 10000000000
for i in range(1, N+1):
    n = 2 #int(input("n="))
    if min >= n:
        min = n
        tartib = i
print("min=", min, "  taqrtibi:", tartib)

#  5-misol.                 katta zichlikni topish
N = 0
P = 0
for i in range(1, N+1):
    m = int(input("m="))            #massa
    V = int(input("V="))            #hajm
    p = m/V
    if p >= P:
        P = p
print("Zichligi kattasi:", P)

#  6-misol.
N = 1
x = True                                    # min va max ga qiymat berish uchun
for i in range(1, N+1):
    n = int(input("n="))
    if x:                                   # min va max ni n ga o'zlashtirib olish
        min = max = n
        x = False                           # bu if shart boshqa qaytib ishlamaydi
    if min > n:
        min = n
        min_tar = i
    if max <= n:
        max = n
        max_tar = i
print(min_tar, "da minimum:", min, "  ", max_tar, "da maximum:", max)

#  7-misol.
N = 1
min = 100000000000;  max = 0
for i in range(1, N+1):
    n = int(input("n="))
    if min >= n:
        min = n
        min_tar = i
    if max < n:
        max = n
        max_tar = i
print(min_tar, "da minimum:", min, "  ", max_tar, "da maximum:", max)

#  8-misol.                 kichik sonni birinchisi va oxirgisi
N = 1
x = True
for i in range(1, N+1):
    n = int(input("n="))
    if x:
        min = n
        x = False
    if min > n:
        min = n
        min_tar = i
    if min >= n:
        min = n
        max_tar = i
print("minimum son:", min, " >> birinchisi:", min_tar, " ikkinchisi:", max_tar)

#  9-misol.                 katta sonni birinchisi va oxirgisi
N = 1
max = 0
for i in range(1, N+1):
    n = int(input("n="))
    if max < n:
        max = n
        min_tar = i
    if max <= n:
        max = n
        max_tar = i
print("maximum son:", min, " >> birinchisi:", min_tar, " ikkinchisi:", max_tar)

#  10-misol.                        birinchi uchragan kichik va katta son (extremal element)
N = 1
x = True
for i in range(1, N+1):
    n = int(input("n="))
    if x:
        min = max = n
        x = False
    if min > n:
        min = n
    if max < n:
        max = n
print("minimum son:", min, "   maximum son", max)

#  11-misol.                    oxirgi uchragan kichik va katta son (extremal element)
N = 1
min = 100000000000; max = 0
for i in range(1, N+1):
    n = int(input("n="))
    if min >= n:
        min = n
    if max <= n:
        max = n
print("minimum son:", min, "   maximum son", max)

#  12-misol.                    eng kichik musbat son
N = 6
x = True
musbat_sanoq = 0
for i in range(1, N + 1):
    n = int(input("n="))
    if x:
        min = max = n
        x = False
    if min > n and n >= 0:
        min = n
        musbat_sanoq += 1
if musbat_sanoq > 0:
    print("minimal musbat son:", min)
else:
    print("nol")

#  13-misol.
N = 1
max = 0
for i in range(1, N+1):
    n = int(input("n="))
    if n%2 != 0 and max < n:
        max = n
        max_tar = i
print(max_tar, "da birinchi uchragan katta toq son:", max)

#  14-misol.                          ?????????????????  ??????????????????????????
B = 5
x = True; chegara = 0           # chegara >>> o'zgaruvchisi B dan kattalarni oladi.
for i in range(1, 5):
    n = int(input("n="))
    if x:
        min = n
        x = False
    if B < n and min > n:
        min = n
        min_tar = i
        chegara += 1
        print(">>>>>>>>>", i)

if x != True:
    print(chegara, "dagi minimum son:", min)
else:
    print("nol")

#  15-misol.                      A va B orasida sonlarni kattasi
A, B = 4, 9
x = True; max_tar = 0
for i in range(1, 6):
    n = int(input("n="))
    if x and A < n < B:
        maxi = n
        x = False
    if A < n < B and maxi < n:
        maxi = n
        max_tar = i
if x:
    print("nol")
else:
    print(max_tar, "da maximum:", maxi)

#  16-misol.                            eng kichik elementgacha sonlarni chiqarish
N = 3
min = 1000000
for i in range(1, N+1):
    n = int(input("n="))
    if min > n:
        min = n
print("Min", min)
for i in range(min+1):
    print(i, end=" ")

#  17-misol.                         eng katta sondan keyingi element
N = 3
max = 0
for i in range(1, N+1):
    n = int(input("n="))
    if max < n:
        max = n
print("Min", max+1)

#  18-misol.                          1- va 2- maximum elementlar orasida nechta son borligi
N = 1
max = 0;  max_tar = 0; min_tar = 0
for i in range(1, N+1):
    n = int(input("n="))
    if max < n:
        max = n
        min_tar = i
    if max <= n:
        max = n
        max_tar = i
if max_tar == min_tar:
    print("nol")
else:
    for i in range(min_tar, max_tar+1):
        print(i, end=" ")
    print("\telementlar orasiada", max_tar-(min_tar+1), "ta son bor.")

#  19-misol.                    min son necha marta ishlatilgani
N = 3
min = 1000000; s = 0
for i in range(1, N+1):
    n = int(input("n="))
    if min >= n:
        min = n
        s += 1
print(min, "soni", s, "marta keldi")

#  20-misol.                    oxirgi uchragan kichik va katta son (extremal element)
N = 2
min = 1000000000; max = 0
min_tar = 0; max_tar = 0
for i in range(1, N+1):
    n = int(input("n="))
    if min >= n:
        min = n
        min_tar += 1
    if max <= n:
        max = n
        max_tar += 1
print(min_tar, "ta minimum son:", min, " <<>> ", max_tar, "ta maximum son", max)

#  21-misol.                    extremal son orasidagi o'rtacha qiymat
N = 6
min = 1000000000; max = 0
S = 0
for i in range(1, N+1):
    n = int(input("n="))
    if min >= n:
        min = n
    if max <= n:
        max = n
for i in range(min+1, max):
    S += i
print("O'rtachasi:", S/(max-(min+1)))

#  22-misol.                    minimal 2 ta sonni chiqarish                    ???????????????????????????
N = 6
m1, m2 = 1000000000, 10000000000
for i in range(1, N+1):
    n = int(input("n="))
    if m2 > n:                                  #            x a t o
        m2 = n
        if m2 > m1:
            m1 = m2
print(m1, m2)

#  23-misol.                    maximal 3 ta sonni chiqarish                    !!!!!!!!!???
N = 10
m1, m2, m3 = 1, 1, 1
if m1 < m3:
    m1, m3 = m3, m1
if m1 < m2:
    m1, m2 = m2, m1
if m2 < m3:
    m2, m3 = m3, m2

for i in range(4, N+1):
    n = int(input("n="))
    if m1 <= n:
        m3 = m2
        m2 = m1
        m1 = n
    elif m2 <= n and m1 > n:
        m3 = m2
        m2 = n
    elif m3 <= n and m2 > n:
        m3 = n
print(m1, m2, m3)

#  24-misol.                                                            ??????????


#  25-misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.

