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
n = 81   #int(input("n="))
s = 0
f, k = 1, 0
while f<n:
    f *= 3
    k += 1
    s += 1
if n == f:
    print("3 ^", k)
else:
    print("3 ni darajasi emas")
print("umumiy=====================", s)

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
s = 0
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

#  7-misol.                  kiritilgan sondan k ni darajasi kichikligini topish
n = 15
i = 0
while i*i < n:
    i += 1
print(i-1, "^ 2 <", n)

#  8-misol.                  kiritilgan sondan k ni darajasi katta son
n = 8
i = 0
while i*i <= n:
    i += 1
print(i, "^ 2 >", n)

#  9-misol.                     3 ^ k > n shartni qanoatlantiruvchi
n = 28
i = 0
while 3**i <= n:
    i += 1
print("3 ^",i, ">", n)

#  10-misol.         3 ^ k < n shartni qanoatlantiruvchi
n = 28
i = 0
while 3**i < n:
    i += 1
print("3 ^",i-1, "<", n)

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

#  20-misol.                2 raqami nechtaligi     uzimni yulim
son = 5923625241
i, s, k = 0, 0, 0
while son > 0:
    i = son % 10
    son //= 10
    k += 1
    if i == 2:
        s += 1
        continue
print("ikki raqami ", s, "ta.  1)sikl soni:", k)

#  20-misol.                2 raqami nechtaligi optimalroq yul (kod qisqa faqat)
son = 5923625241
s, k = 0, 0
while son > 0:
    k += 1
    if son%10 == 2:
        s += 1
    son //= 10
print("ikki raqami ", s, "ta.  1)sikl soni:", k)

#  21-misol.                toq raqam nechtaligi
son = 5936541
i, s = 0, 0
while son > 0:
    i = son % 10
    son //= 10
    if i%2 != 0:
        s += 1
        continue
print("Toq raqami ", s, "ta")
print()




#  22-misol. 1               ==========    T U B   sonlar      =================   optimalmas. optimali pastada
son = 52
i = 1; S = 0
while i <= son:
    j, S = 1, 0
    while j <= i:
        if i % j == 0:
            S += 1
        j += 1
    if S == 2:
        print(i, end=" ")
    i += 1
print()

#  22-misol. 2               ==========    T U B   sonlar      =================
son = 52
i = 3; S = 0                # sanashni 3 dan boshlaymiz
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 1, 0
    while j <= i:
        if i % j == 0:
            S += 1
        j += 1
    if S == 2:
        print(i, end=" ")
    i += 2                  # 2 ni qushib ketsak toq buladi
print()

#  22-misol. 3               ==========    T U B   sonlar      =================
son = 52
i = 3; S = 0
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 1, 0
    while j <= i:
        if i % j == 0:
            S += 1
        j += 2              # j += 1  edi
    if S == 2:
        print(i, end=" ")
    i += 2
print()

#  22-misol. 4               ==========    T U B   sonlar      =================
son = 52
i = 3; S = 0
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 3, 0             # j ni 3 dan boshlaymiz
    while j < i:            # j ni uziga bulmaymiz
        if i % j == 0:
            S += 1
        j += 2
    if S == 0:
        print(i, end=" ")
    i += 2
print()

#  22-misol. 5               ==========    T U B   sonlar      =================
son = 52
i = 3; S = 0
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 3, 0
    while j < i:
        if i % j == 0:
            S = 1
            break           # S += 1  >>  2 tadan kup buluvchilarni tekshirishni tuxtatdik
        j += 2
    if S == 0:
        print(i, end=" ")
    i += 2
print()

#  22-misol. 6               ==========    T U B   sonlar      =================  5-sinf kitobida izlash
son = 52
i = 3; S = 0
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 3, 0
    while j < i:
        if i % j == 0:
            S = 1
            break
        j += 2
    if S == 0:
        print(i, end=" ")
    i += 2
print()

#  22-misol. 7
son = 52
i = 3; S = 0
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 3, 0
    while j < i // 2:       # kiritilgan sonni yarmigacha tekshiramiz. chunki eng kichigi 2 gacha bulinadi va yarmidan oshganga bulinmasligi aniq.
        if i % j == 0:      #            bu yerda hozirda faqat toq sonlarga bulib kurmoqda. shuni uchun yarmidan keyin ishlashini keragi yuq!
            S = 1           #            while j <= i // 2  >>>> bulishi ham mumkin
            break
        j += 2
    if S == 0:
        print(i, end=" ")
    i += 2
print()

#  22-misol. 8 >> 7-usul bilan boshqa usul                 5-sinfdagi.  ildiz olishdan foydalaniladi.
son = 52
i = 3; S = 0
print(2, end=" ")           # faqat ikki juft tub raqam

while i <= son:
    j, S = 3, 0
    while j <= int(pow(i, 0.5)):       # ildiz olish. int ga olib quyamiz. va i ni ildiz olinganiga teng (=) bulish kerak
        if i % j == 0:
            S = 1
            break
        j += 2
    if S == 0:
        print(i, end=" ")
    i += 2


print()
print()



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





#  23-misol.                    ===========     E K U B      ===========
a, b = 56, 42
if b > a:
    a, b = b, a
i = a
while i >= 1:
    if a%i == 0 and b%i == 0:
        ekub = i
        break
    i -= 1
print("1-usulda.  EKUB >>> ", ekub)

#  23-misol.                     E K U B    2-usuli      # optimalroq emas 1- usulga nisbatan.
a, b = 56, 42

i = 1
while (i <= a and i <= b):
    if a%i == 0 and b%i == 0:
        ekub = i
    i += 1
print("2-usulda.  EKUB >>>> ", ekub)


#  23-misol.                    =======   E K U B    EVKLID  usulida  1-usuli  ========
a, b = 48, 56

while a != b:
    if a > b:                   # kattasidan kichigini ayirish usulida ishlanadi
        a -= b                  # a = a - b
    else:                       # b = b - a
        b -= a
print("Evklid 1-usulida  UKUB >>>", a, b)


#  23-misol.                    =======   E K U B    EVKLID  usulida  1-usuli  ========
a, b = 48, 56

while a > 0 and b > 0 and a!=b:
    if a > b:                   # kichigini qoldiqqa olib, qoldiqli bulish usulida ishlanadi
        a %= b                  # a = a % b
    else:                       # b = b % a
        b %= a
    if a == 0:      a = b
    if b == 0:      b = a
print("Evklid 2-usulida  UKUB >>>", a, b)
print()




#  24-misol.        =========    F I B O N A CH I    S O N L A R     ===========
print("\nFibonachi soni  1-usul.")
a = 88
i,b = 1, 0
while i <= a:
    b += i
    print(i, end=" ")
    print(b, end=" ")
    i += b

print("\nFibonachi soni  2-usul.")
n = 20
f0 = 0; f1 = 1; i = 1
while i <= n:
    fi = f0 + f1
    f0 = f1
    f1 = fi
    print(fi, end=" ")
    i += 1


#  25-26-misol.                Fibonachi sonidan bir oldingi va bir keyingi sonni chiqarish     ?????????????????????
print("\nFibonachi sonidan bir oldingi va bir keyingisi.")
a = 88
i,b = 1, 0
while i <= a:
    b += i
    print(i, end=" ")
    print(b, end=" ")
    i += b


#  27-misol.                    Fibonachi sonini hadini aniqlash            uzimni kodim
print("\nFibonachi soni hadini topish.  1-usulda")
a = 89
i,b, h = 1, 0, 0
while i <= a:
    b += i
    h += 1
    print(i, end=" ")
    print(b, end=" ")
    i += b
    h += 1
print("   hadi:", h)

print("\nFibonachi soni hadini topish.  2-usulda")
n = 20
f0 = 0; f1 = 1; i = 1; h = 0
while i <= n:
    fi = f0 + f1
    f0 = f1
    f1 = fi
    print(fi, end=" ")
    i += 1
    h += 1
print("    hadi:", h)

print()


#  28-misol.                    ?????????????????????????????????????????


#  29-misol.                    ????????????????????????????????


#  30-misol.                 a va b turtburchakka c kvadrat necta sig'ishi.       uzimniki
A, B, C = 8, 6, 2
s = 2
while 0 <= A or 0 <= B:
    if A >=0:
        s += 1;   A -= C
    if B >=0:
        s += 1;   B -= C

    print(A, B, "dan", s, "ta")

#  30-misol.
A, B, C = 8, 6, 2
s1, s2 = 0, 0

while A >= C:
    s1 += 1
    A -= C

while B >= C:
    s1 += 1
    B -= C
s3 = 0
while s1 > 0:
    s3 += s2
    s1 -= 1
print("kub", s3, "ta sig'adi.")


