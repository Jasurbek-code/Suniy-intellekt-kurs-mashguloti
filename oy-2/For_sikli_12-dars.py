#  1-misol.
k, n = 2, 1  #int(input("k=")), int(input("necha marta chiqarish kerak. n="))
for n in range(1, n+1):
    print("k=", k, "marta", n, "ta")

#  2-misol.
a, b = 3, 8  #int(input("a=")), int(input("b="))
s = 0
for i in range(a, b+1):
    s += 1
    print(i, end=" ")
print("   Umimiy", s, "ta son ishlatildi.")

#  2-misol.                                     enumerate  orqali
a, b = 3, 8  #int(input("a=")), int(input("b="))
for soni, i in enumerate(range(a, b+1)):
    print(i, end=" ")
print("   Umimiy", soni+1, "ta son ishlatildi.")

#  3-misol.                         sonlar orasidagini teskarisini chiqarish
a, b = 3, 8  #int(input("a=")), int(input("b="))
s = 0
for i in range(b, a-1, -1):
    s += 1
    print(i, end=" ")
print("   Umimiy", s, "ta son ishlatildi.")

#  4-misol.                     kvadratini hisoblash
n = 3   #int(input("n="))
for i in range(1, n+1, 2):
    print(i, "^ 2 =", i*i)
print()

#  5-misol.                          konfetni narxini chiqaruvchi
narx = 3000     # 1 kg konfet narxi
                # og'irlik  0.1; 0.2; ...; 0.9; 1  oraliqda
for i in range(10):
    i = i/10 + 0.1
    S = float(format(i, ".1f")) * narx
    print("%.1f narxi %s so'm" %(i, S))
print()

#  6-misol.                          konfetni narxini chiqaruvchi
narx = 5000     # 1 kg konfet narxi
                # og'irlik  1.2; 1.4; ...; 1.8; 2  oraliqda
for i in range(0, 10, 2):
    i = (i+10)/10 + 0.2
    S = float(format(i, ".1f")) * narx
    print("%.1f narxi %s so'm" %(i, S))        # round(i, 1)    >> format urnida oson ixchamlash, butundan keyin 1 ta raqam chiqadi
print()

#  7-8-9-misol.                 a dan b gacha son yig'indisi
a, b = 3, 8
S, K, k = 0, 1, 0
for num, i in enumerate(range(a, b+1)):
    S += i
    K *= i
    k += i**i
print(num, "marta ishladi. Yig'indi=", S)
print(num, "marta ishladi. Ko'paytmasi=", K)
print(num, "marta ishladi. Kvadrati yig'indisi=", k)

#  10-misol.            yig'indi,
n = 3
S = 0
for i in range(1, n+1):
    S += 1/i
print("yig'indi=", S)

#  11-misol.
n = 5
S = 0
for i in range(1, n+1):
    S += pow(n+i, 2)
print("kvadratini yig'indisi=", S)

#  12-misol.
n = 4
s, S = 0, 1
for i in range(1, n+1):
    s = 1+i/10
    S *= s
print("N ta kopaytuvchi=", S)

#  13-misol.                                                                     !!!!!!
n = 2
S, k = 0, 0
for i in range(1, n+1):
    k += 1
    S += 1+(k/10)
    for j in range(1):
        k += 1
        S -= 1+(k/10)
print("yig'indi=", S)

#  14-misol.
n = 6
for i in range(1, n+1):
    S += 2*i-1
print("S=", S)

#  15-misol.
n = 3   #int(input("daraja:"))
a = 2   #int(input("son="))
k = 1
for i in range(1, n+1):
    k *= a
print("2 ^", i, "=", k)

#  16-misol.
n = 5   #int(input("daraja:"))
a = 3   #int(input("son="))
k = 1
for i in range(1, n+1):
    k *= a
print("3 ^", i, "=", k)

#  17-misol.
n = 5   #int(input("daraja:"))
a = 3   #int(input("son="))
S = 0
for i in range(0, n+1):
    S += a**i
print(a, "^", i, "=", S)

#  18-misol.
n = 5   #int(input("daraja:"))
a = 3   #int(input("son="))
S = 0
for i in range(1, n+1):
    S += ((-1)**i)*pow(a, i)
print(a, "^", i, "=", S)

#  19-misol.                 ==================   faktorial    ==================
n = 5
f = 1
for i in range(1, n+1):
    f *= i
print(i, "faktorial=", f)

#  20-misol.            1! + 2! + 3! + ... + n!    ni hisoblash
n = 4
f, S = 1, 0
for i in range(1, n+1):
    f *= i
    S += f
print("Faktorial Yig'indisi=", S)

#  21-misol.            1/1! + 1/2! + 1/3! + ... + 1/n!    ni hisoblash
n = 4
f, S = 1, 0
for i in range(1, n+1):
    f *= i
    S += 1 / f
print("bir taqsim faktorial. Yig'indisi=", S)







#  22-misol.            1+x^1/1! + x^2/2! + x^3/3! + ... + x^n/n!  = e^x  ni hisoblash
n = 4; x= 2
f, S = 1, 0
for i in range(1, n+1):
    f *= i
    S += (x**i)/f
print("Yig'indi=", S)


#  23-misol.           sin(x) ga yaqinalshadi
n = 4; x = 3
f, S = 1, x             # range 3 dan bolangani uchun S boshlang'ich qiymat x ni uziga teng bo'ladi
ishora = -1
for i in range(3, n+1, 2):
    f *= i*(i-1)
    S += (ishora) * (x**(i))/f
    ishora *= -1
print("< sin(x) >  S=", S)

#  24-misol.           cos(x) ga yaqinlashadi
n = 4; x = 3
f, S = 1, 1          # range 2 dan bolangani uchun S boshlang'ich qiymat x ni uziga teng bo'ladi
ishora = -1
for i in range(2 ,n+1, 2):
    f *= i*(i-1)
    S += (ishora) * (x**(i))/f
    ishora *= -1
print("< cos(x)>  S=", S)







#  25-misol.
n, x = 4, 0.2           # |x| < 1
S = 0
for i in range(1, n+1):
    S += ((-1)**(i-1))*(x**i)/i
print("Yig'indi=", S)

#  26-misol.
n, x = 4, 0.2           # |x| < 1
S = 0;   ishora = 1
for i in range(1, n+1, 2):
    S += (ishora)*(x**i)/i
    ishora *= -1
print("Yig'indi=", S)

#  27-misol.            # |x| < 1                   # !!!
print("           27-misol.")
n, x = 4, 0.2
S = x
for i in range(1, n+1):
    S += S * (2*i-1) * (x**(2*i+1)) / ((2*i)*(2*i+1))           # S ko'paytirilgan bulishi mumkin
    print("S=", S)



#  28-misol.                                        # !!!!
n, x = 4, 0.2
S = 1
for i in range(1, n+1):
    S += ((-1)**(i-1))*(2*i-3)*(x**i) / (2*i)
    print("S=", S)

#  29-misol.                    # [A, B], kesmani teng n taga bulib, shu nuqtalarini topish
n, A, B = 5, 5, 17
kesma = abs(A-B)/n
print("kesma=", kesma)
a, b = A, A

for i in range(n):
    b += kesma
    print("A=", a, "B=", b)
    a = b

#  30-misol.                    # 29-misolni     f(x)=1-sin(x)                          # ???????????????????????????????????
from math import sin
n, A, B = 5, 3, 18
kesma = abs(A-B)/n
print("kesma=", kesma)
a, b = A, A
for i in range(n):
    b += kesma
    fx = 1-sin(a)
    print("f(x)=", fx)
    a = b



#  31-misol.                        # A0 = 2;   AK = 2 + 1/A(K-1);   K = 1,2,...:  dastlabki n ta hadi      !!!
n = 2
A0 = 2
AK = A0         # AK - boshlang'ich qiymat
for i in range(2, n+1):
    AK += 1 / i
print("AK=", AK)

#  32-misol.                        # A0 = 2;   ;   K = 1,2,...:  dastlabki n ta hadi          ?????????????????????????????
n = 3
AK = 0
for i in range(1, n):
    AK += (i + 1) / (i)
print("AK=", AK)


#  33-misol.                      # fibonachi                   !!!
n = 8
f, f1 = 1, 0
for i in range(1, n):
    f1 += f
    f += f1
    print(f1,f, end=" ")
print()


#  34-misol.        # A1=1; A2=2 ;  AK = (A(K-2)) + 2*A(K-1)) / 3 ;   K = 3,4,...:  dastlabki n ta hadi
n = 4
AK = 0
for i in range(3, n+1):
    AK += ((i-2) + 2*(i-1)) / 3
print("AK=", AK)

#  35-misol.    # A1=1; A2=2; A3=3;  AK = A(K-1) + A(K-2) - 2*A(K-3) ;   K = 4,5,...:  dastlabki n ta hadi
n = 10
AK = 0
for i in range(4, n+1):
    AK += (i-1) + (i-2) - 2*(i - 3)
print("AK=", AK)



###########################       ICHMA-ICH SIKLLAR       ##########################################################
#  36-misol.
N, K = 3, 2
S = 0
for i in range(1, N+1):
    S += i**K
print("S=", S)

#  37-misol.
N = 3
S = 0
for i in range(1, N+1):
    S += i**i
print("S=", S)

#  38-misol.
N = 3
S = 0;  k = N
for i in range(1, N+1):
    S += i**k              # S += i**(N-i+1)            optimalrog'i
    k -= 1
print("S=", S)
print()

#  39-misol.
print(">>>>>>>>>>>    39-misol.     <<<<<<<<<<<<<<<")
A, B = 5, 8
for i in range(A, B+1):
    for j in range(i):
        print("i=", i)
    print()

#  40-misol.    1-usul
print(">>>>>>>>>>>    40-misol. 1    <<<<<<<<<<<<<<<")
A, B = 2, 8
s = 0
for i in range(A, B+1):              # range(i-A + 1)  yozish mumkin
    s+= 1
    for j in range(s):
        print("i=", i)
    print()

#  40-misol.    1-usul                                      str orqali optimal yechim
print(">>>>>>>>>>>    40-misol. 2    <<<<<<<<<<<<<<<")
A, B = 2, 8
for i in range(A, B+1):
    print((str(i) + " ")*(i-A+1), end=" ")

print()
#                           EKUB TOPISH
print("EKUB  topish")
a = 35; b = 90
for i in range(max(a, b)):
    b = b - a
    a = b
    if b < 0:
        break
    print("b=", b)