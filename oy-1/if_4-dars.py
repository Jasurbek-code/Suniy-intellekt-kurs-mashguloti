import math
#  1-misol.
son = 21
if son >= 0:
    print("Son musbat:", son + 1)
else:
    print("Son manfiy:", son)

#  2-misol.
if son >= 0:
    print("Son musbat:", son + 1)
else:
    print("Son manfiy:", son - 2)

#  3-misol.
if son == 0:
    son = 10
    print("Son nol:", son)
if son > 0:
    print("Son musbat:", son + 1)
else:
    print("Son manfiy:", son)

#  4-misol.
a,b,c = 2,-3,4;          S=0
if a > 0:       S += 1
if b > 0:       S += 1
if c > 0:       S += 1
print(S, "ta musbat son")

#  5-misol.
a,b,c = 2,-3,4;          S=0
if a > 0:       S += 1
if b > 0:       S += 1
if c > 0:       S += 1
print(S, "ta musbat.  ", 3-S, "ta manfiy")

#  6-misol.
a,b = 2,3;
if a>b:    print("a > b")
else:      print("a < b")

#  7-misol.
A, B = 5, 4
if A > B:
    print(B)
else:
    print(A)

#  8-misol.
a, b = 4,3
if a>b:     print(a, b)
else:       print(b, a)

#  9-misol.
A, B = 4,3
if a>b:     A,B = B,A;        print("B=", B, "  A=", A)
else:                         print("B=", B, "  A=", A)

#  10-misol.
a, b = 7,5
if a != b:          print("a + b =", a+b)
else:               print("nol=", 0)

#  11-misol.
a, b = 7,5
if a == b:
    print("Teng ekan:", 0)
if a>b:
    print("Kattasi  a:", a)
else:
    print("Kattasi  b:", b)

#  12-misol.
a,b,c = 6,1,4
if a < b < c or a < c < b:           print("a kichigi")
elif b < a < c or b < c < a:         print("b kichigi")
else:                                print("c kichigi")

#  13-misol.
a, b, c = 5,8,4
if a < b < c or a > b > c:      print("b o'rtacha")
elif b < a < c or b > a > c:    print("a o'rtacha")
else:                           print("c o'rtacha")

#  14-misol.
m,k,l = 2,3,4
if m < k < l:
    print("m=", m, "l=", l)
if m < l < k:
    print("m=", m, "k=", k)
if k < m < l:
    print("k=", k, "l=", l)
if k < l < m:
    print("k=", k, "m=", m)
if l < k < m:
    print("l=", l, "m=", m)
if l < m < k:
    print("l=", l, "k=", k)

#  15-misol.
a,b,c = 2,8,4
if a+b > b+c or a+b > a+c:          print("a", a, " b", b)
elif a+c > a+b or a+c > b+c:        print("a", a, " c", c)
elif b+c > a+b or b+c > a+c:         print("b", b, " c", c)

#  16-misol.
a,b,c = 2,3,4
if a < b < c:
    print("O'sish tartibida:", "a=", a*2, "b=", b*2, "c=", c*2)
if a > b > c:
    print("O'sish tartibida:", "a=", -a, "b=", -b, "c=", -c)


#  19-misol.
a,b,c,d = 2,2,2,5
if a == b ==c:
    print("d=", d)
elif a == b == d:
    print("c=", c)
elif a == c == d:
    print("b=", b)
elif b == c == d:
    print("a=", a)

#  20-misol.
a,b,c = 2,3,4
if (b-a) < (c-a):
    print("masofa b-a=", b-a)
elif (c-a) < (b-a):
    print("masofa c-a=", c-a)

#  21-22-23-misol.                                                       ?????????????????????????

#  24-misol.
x = 5
if x>0:
    fx = 2*math.sin(x);        print("f(x) = 2*sin(x)", fx)
else:
    fx = x - 6;                print("f(x) = x - 6", fx)

#  26-misol.
x = 6
if x <= 0:          fx = -x;            print("f(x) = -x", fx)
if 0 < x < 2:       fx = x*x;           print("f(x) = x*x", fx)
if x >=2:           fx = 4;             print("f(x) = 4", fx)

#  27-misol.
x = 5
if x < 0:                               print("f(x) = 0")
if x == 0:                               print("f(x) = 1")
if x < 0:                               print("f(x) = -1")

#  28-misol.
a = 1999
if a % 4 == 0:      print("kabisa", 365)
if a // 400:        print("kabisa emas")

#  29-misol.
K = 15
if K >= 0 and K % 2 != 0:
    print("Musbat toq son.", K)
elif K >= 0 and K % 2 == 0:
    print("Musbat Juft son.", K)
elif K < 0 and K % 2 != 0:
    print("Manfiy toq son.", K)
elif K < 0 and K % 2 == 0:
    print("Manfiy juft son.", K)

#  30-misol.
a = 11587
if a // 100 != 0 and a % 2 == 0:              print("uch xonali juft son:", a)
elif a // 100 != 0 and a % 2 != 0:            print("uch xona toq son:", a)
elif a // 100 == 0 and a % 2 == 0:            print("ikki xonali juft son:", a)
elif a // 100 == 0 and a % 2 != 0:            print("ikki xonali toq son:", a)

#  31-misol.         Sonni so'z ko'rinishiga keltiruvchi dastur
son = int(input(">> 10000 dan kichik Son kiriting.\n> So'z qilib beraman:"))

if son >= 100000 != 0:                           # yuz mingliklar
    if (son//100000) == 1:
        print("Bir Yuz", end=" ")
    elif (son//100000) == 2:
        print("Ikk Yuz", end=" ")
    elif (son//100000) == 3:
        print("Uch Yuz", end=" ")
    elif (son//100000) == 4:
        print("To'rt Yuz", end=" ")
    elif (son//100000) == 5:
        print("Besh Yuz", end=" ")
    elif (son//100000) == 6:
        print("Olti Yuz", end=" ")
    elif (son//100000) == 7:
        print("Yetti Yuz", end=" ")
    elif (son//100000) == 8:
        print("Sakkiz Yuz", end=" ")
    elif (son//100000) == 9:
        print("To'qqiz Yuz", end=" ")

if son >= 10000:                           # on mingliklar
    if (son//10000%10) == 1:
        print("O'n", end=" ")
    elif (son//10000%10) == 2:
        print("Yigirma", end=" ")
    elif (son//10000%10) == 3:
        print("O'ttiz", end=" ")
    elif (son//10000%10) == 4:
        print("Qirq", end=" ")
    elif (son//10000%10) == 5:
        print("Ellik", end=" ")
    elif (son//10000%10) == 6:
        print("Oltmish", end=" ")
    elif (son//10000%10) == 7:
        print("Yetmish", end=" ")
    elif (son//10000%10) == 8:
        print("Sakson", end=" ")
    elif (son//10000%10) == 9:
        print("To'qson", end=" ")

if (son//1000%10) != 0:                           # bir mingliklar
    if (son//1000%10) == 1:
        print("Bir", end=" ")
    elif (son//1000%10) == 2:
        print("Ikk", end=" ")
    elif (son//1000%10) == 3:
        print("Uch", end=" ")
    elif (son//1000%10) == 4:
        print("To'rt", end=" ")
    elif (son//1000%10) == 5:
        print("Besh", end=" ")
    elif (son//1000%10) == 6:
        print("Olti", end=" ")
    elif (son//1000%10) == 7:
        print("Yetti", end=" ")
    elif (son//1000%10) == 8:
        print("Sakkiz", end=" ")
    elif (son//1000%10) == 9:
        print("To'qqiz", end=" ")

if son // 1000 != 0:                              # mingliklar
    print("Ming", end=" ")

if son // 100 != 0:                           # yuzliklar
    if (son%1000//100) == 1:
        print("Bir yuz", end=" ")
    elif (son%1000//100) == 2:
        print("Ikk yuz", end=" ")
    elif (son%1000//100) == 3:
        print("Uch yuz", end=" ")
    elif (son%1000//100) == 4:
        print("To'rt yuz", end=" ")
    elif (son%1000//100) == 5:
        print("Besh yuz", end=" ")
    elif (son%1000//100) == 6:
        print("Olti yuz", end=" ")
    elif (son%1000//100) == 7:
        print("Yetti yuz", end=" ")
    elif (son%1000//100) == 8:
        print("Sakkiz yuz", end=" ")
    elif (son%1000//100) == 9:
        print("To'qqiz yuz", end=" ")
if son // 10 != 0:                           # onliklar
    if (son//10%10) == 1:
        print("O'n", end=" ")
    elif (son//10%10) == 2:
        print("Yigirma", end=" ")
    elif (son//10%10) == 3:
        print("O'ttiz", end=" ")
    elif (son//10%10) == 4:
        print("Qirq", end=" ")
    elif (son//10%10) == 5:
        print("Ellik", end=" ")
    elif (son//10%10) == 6:
        print("Oltmish", end=" ")
    elif (son//10%10) == 7:
        print("Yetmish", end=" ")
    elif (son//10%10) == 8:
        print("Sakson", end=" ")
    elif (son//10%10) == 9:
        print("To'qson", end=" ")
if (son % 10) != 0:                           # birliklar
    if (son % 10) == 1:
        print("Bir")
    elif (son % 10) == 2:
        print("Ikki")
    elif (son % 10) == 3:
        print("Uch")
    elif (son % 10) == 4:
        print("To'rt")
    elif (son % 10) == 5:
        print("Besh")
    elif (son % 10) == 6:
        print("Olti")
    elif (son % 10) == 7:
        print("Yetti")
    elif (son % 10) == 8:
        print("Sakkiz")
    elif (son % 10) == 9:
        print("To'qqiz")
