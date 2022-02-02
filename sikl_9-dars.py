#  1-misol.
A, B = 11, 3
while A >= B:
    A -= B
print("A dan ", A,  "uzunlikda joy qoldi")

#  2-misol.
A, B = 19, 3
s = 0
while A >=B:
    A -= B
    s += 1
print("A ga ", (s),  "ta joylanadi")

#  3-misol.             # kopaytma ishlatmasdan N ni K ga bulgandagi qoldiq
N, K = 19, 3
s = 0
while N >= K:
    N -= K
    s += 1
print("Butun qismi=", s, "qoldiq=", N)

#  4-misol.                 3 ga karrali sonlar
Son = 36
s = 0
while Son > 0:
    print("3 ga karrali:", Son)
    Son -= 3

# 4-misol.                  3 ni darajasi
n = int(input("n="))

f, k = 1, 0
while f<n:
    f *= 3
    k += 1
if n == f:
    print("3 ^", k)
else:
    print("3 ni darajasi emas")


##################   ^^^^^^^^^^^^^     ###################################      ????????????????????

n = 90  #int(input("n="))
S = 0
i = 0; j = 3
while S < n:
    if i > 2:
        i = 3
        while j >= i:
            i += 3
            print("   j=", j, " i=", i)
    else:
        i += 1
    k = 0                       # o'zgarmaydi
    while k < i:
        S += 3
        k += 1
        print("i=", i, "k=", k, "S=", S)

################     ^^^^^^^^^^^^^      #####################################       ???????????????????



#  5-misol.             2 ni darajasini aniqlash
Son = 36
s,  = 0
while Son > 2:
    Son -= 2
    s += 1
print("2 ni ", s ,"- darajasi")

#  6-misol.
n = 12
i = 1
while n > 1:
    i *= n
    n -= 2
print("N:", i)

#  7-misol.                         ???????????????????????
n = 15
i = 1

#  8-misol.                         ?????????????????????


#  9-misol.                         ?????????????????????


#  10-misol.                        ?????????????????????


#  11-misol.
n = 11
k, s = 0, 0
while s <= n:
    k += 1
    s += k
print("k=", k, "  Yig'indisi=", s)

#  12-misol.
n = 10
k, s = 0, 0
while s < n:
    k += 1
    s += k
print("k=", k, "  Yig'indisi=", s)

#  13-misol.
n = 2
k, s = 0, 0
while s < n:
    k += 1
    s += 1 / k
print("k=", k-1, "  Yig'indisi=", s)

#  14-misol.
n = 3
k, s = 0, 0
while s < n:
    k += 1
    s += 1 / k
print("k=", k-1, "  Yig'indisi=", s)

#  15-misol.                # summa necha oydan keyin 2 marta oshadi
S = 1200        # quyilgan summa
p = 12          # foiz          0 < p < 25
K, s = S*2, 0
while k <= K:
    k += (S*p)/100
    s += 1
print("oy:", s, "  foiz summasi:", k)

#  16-misol.                sportsmen necha kundan keyin 200 km dan kup yuguradi
K = 10      # 1-kun yugurish km ri
p = 22      # keyingi kun yugurish foizi    0 < p < 50
f, d = 0, 0
while f < 200:
    f += K*p/100
    d += 1
print("kun:", d, "yugurish masofa km:", f)

#  17-misol.            bulish amalini bajarmasdan  qoldiq va butun qismni topish
n, m = 27, 4
s = 0
while n-1 > 0:
    s += 1
    n = n - m
    print("butuni=", s, "  qoldiq=", n)

#  18-misol.        raqamni teskari chiqaruvchi
n = 234
S = 1
while n >= S:
    N = n // S % 10
    S *= 10
    print(N, end="")
print()

#  19-misol.            sonni raqamlari yig'indisi
n = 23454
i, s = 0, 0
while n > 0:
    s += 1
    i += n % 10
    n //= 10
print(s, "marta ishlatildi.", " Yig'indisi=", i)

#  20-misol.
son = 5936541
i, s = 0, 0
while son > 0:
    i = son % 10
    son //= 10
    if i == 2:
        s += 1
        continue
print("ikki raqami ", s, "ta")

#  21-misol.
son = 5936541
i, s = 0, 0
while son > 0:
    i = son % 10
    son //= 10
    if i%2 != 0:
        s += 1
        continue
print("Toq raqami ", s, "ta")

#  22-misol.                    T U B   yoki   T U B   E M A S ligini topish
son = 27
k = 1
while k <= son:
    m, s = 1, 0
    while m <= son:
        if son % m == 0:
            s += 1
        m += 1
    k += 1
if s == 2:
    print(son, "tub")
else:
    print("tub emas")

#  23-misol.                    =======   E K U B      ========         ?????????????????????/
a, b = 56, 42
i, s = 2, 0         #  a uchun
k, r = 2, 0         #  b uchun
while a > 1:
    if a % i == 0:
        s += 1
        print("a=", a, "i=", i, "s=", s)
        a //= i
    else:
        i += 1
        s = 0


#  24-misol.        =========    F I B O N A CH I    S O N L A R     ===========
a = 88
i,b = 1, 0
while i <= a:
    b += i
    print(i, end=" ")
    print(b, end=" ")
    i += b
print()

#  25-26-misol.                Fibonachi sonidan bir oldingi va bir keyingi sonni chiqarish
a = 88
i,b = 1, 0
while i <= a:
    b += i
    print(i, end=" ")
    print(b, end=" ")
    i += b
print()

#  27-misol.                    Fibonachi sonini hadini aniqlash
print("\nFibonavhi soni  1-usul.")
a = 88
i,b = 1, 0
while i <= a:
    b += i
    print(i, end=" ")
    print(b, end=" ")
    i += b
print("\nFibonavhi soni  2-usul.")
n = 20
f0 = 0; f1 = 1; i = 1
while i <= n:
    fi = f0 + f1
    f0 = f1
    f1 = fi
    print(fi, end=" ")
    i += 1
print()

#  28-misol.                        ?????????????????????????????????????????


#  29-misol.                    ????????????????????????????????


#  30-misol.

A, B, C = 8, 6, 2
s = 2
while 0 <= A or 0 <= B:
    if A >=0:
        s += 1;   A -= C
    if B >=0:
        s += 1;   B -= C

    print(A, B, "dan", s, "ta")





