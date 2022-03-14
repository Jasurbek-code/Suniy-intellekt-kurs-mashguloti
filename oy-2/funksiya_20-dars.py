#  1-misol.
print("~~~~~~~      1-misol.       ~~~~~~~~~~~~~~~~~~~")
def PowerA3(A,B,C):
    return A**3, B**3, C**3
print(PowerA3(2,3,4))

#  2-misol.
print("\n~~~~~~~      2-misol.       ~~~~~~~~~~~~~~~~~~~")
def PowerA234(A, B, C):
    return "A >", A ** 2, A ** 3, A ** 4, "  B >", B ** 2, B ** 3, B ** 4, "  C >", C ** 2, C ** 3, C ** 4
print(PowerA234(3, 5, 4))

#  3-misol.
print("\n~~~~~~~      3-misol.       ~~~~~~~~~~~~~~~~~~~")
def Mean(A,B,C,D):
    return (A+B)/2, (A+C)/2, (A+D)/2
print(Mean(2,3,5,6))

#  4-misol.
print("\n~~~~~~~      4-misol.       ~~~~~~~~~~~~~~~~~~~")
def Triangle(A,B,C):
    per_A = 3*A
    yuza_A = (per*((per-A)**3))

    per_B = 3*B
    yuza_B = (per*((per-B)**3))

    per_C = 3*C
    yuza_C = (per*((per-C)**3))

    return per_A, yuza_A, " <> ", per_B, yuza_B, " <> ", per_C, yuza_C

#  5-misol.
print("\n~~~~~~~      5-misol.       ~~~~~~~~~~~~~~~~~~~")
def RectPS(x1,x2, y1,y2):
    peremetr = 2*(abs(x1-x2) + abs(y1-y2))
    yuza = (abs(x1-x2))*(abs(y1-y2))

    return peremetr, yuza
print(RectPS(2,3,4,5))

#  6-misol.
print("\n~~~~~~~      6-misol.       ~~~~~~~~~~~~~~~~~~~")
def DigitSum(a):
    S_a = 0; l = 0
    while a > 0:
        S_a += a % 10
        a //= 10
        l += 1
    return S_a, l
print(DigitSum(23456))

#  7-misol.
print("\n~~~~~~~      7-misol.       ~~~~~~~~~~~~~~~~~~~")
def InvertDigit(a):
    S_a = 0
    while a > 0:
        S_a = a % 10
        a //= 10
        print(S_a)
print(InvertDigit(235))

#  8-misol.
print("\n~~~~~~~      8-misol.       ~~~~~~~~~~~~~~~~~~~")
def AddRightDigit(a, R):
    return str(a) + str(R)

print(AddRightDigit(456, 2))


#  9-misol.
print("\n~~~~~~~      9-misol.       ~~~~~~~~~~~~~~~~~~~")
def AddLeftDigit(a, R):
    return str(R)+str(a)

print(AddRightDigit(456, 2))


#  10-misol.                        # sonlar o'rnini almashtirish
print("\n~~~~~~~      10-misol.       ~~~~~~~~~~~~~~~~~~~")
def AddRightDigit(a, b, c,d):
    a = a + b
    b = a - b
    a = a - b

    c =c + d
    d = c - d
    c = c - d

    return a,b,  c, d
print(AddRightDigit(2,3,4,5))



#  11-misol.   1                                                                !!!!!!!!!!!!!???
print("\n~~~~~~~      11-misol.  1     ~~~~~~~~~~~~~~~~~~~")
def MinMax(X, Y):
    if X > Y:
        X, Y = Y, X
    return X, Y

mini = MinMax(4, 12)
maxi = MinMax(8, 3)
print(MinMax(5, 17))

#  11-misol.    2                                                               !!!!!!!!!!!!!???
print("\n~~~~~~~      11-misol.  2     ~~~~~~~~~~~~~~~~~~~")
def MinMax(X, Y):
    if X > Y:
        return X
    else:
        return Y

n = int(input("n= "))           # sikl ishlash davri
c = int(input("X = "))
for i in range(2, n+1):
    X = int(input("X= "))
    c = MinMax(c, X)
print(c)




#  12-misol.                        # sonlarni tartiblash
print("\n~~~~~~~      12-misol.       ~~~~~~~~~~~~~~~~~~~")
def SortInc3(A,B,C):
    while True:                     # 3 ta sonni joyini almashtirib olamiz A soni kichik bo'lmaguncha
        A = A + B + C
        B = A - B - C
        C = A - B - C
        A = A - B - C

        if A <= B and A <= C:                       # tenglik bo'lmasa, hammasni bir xil son kiritilsa cheksiz ishlaydi funksiya
            while True:             # B va C ni joyini amashtiramiz. B kichik bulmaguncha
                if B <= C:
                    break
                B = B + C
                C = B - C
                B = B - C

            return A, B, C          # natija chiqishga tayyor buldi.
print(SortInc3(9,7,2))


#  13-misol.                    # sonlarni kamayish tartibida chiqarish
print("\n~~~~~~~      13-misol.       ~~~~~~~~~~~~~~~~~~~")
def SortDec3(A,B,C):
    while True:                     # 3 ta sonni joyini almashtirib olamiz C soni kichik bo'lmaguncha
        A = A + B + C
        B = A - B - C
        C = A - B - C
        A = A - B - C

        if  C <= B and C <= A:                       # tenglik bo'lmasa, hammasni bir xil son kiritilsa cheksiz ishlaydi funksiya
            while True:             # B va A ni joyini amashtiramiz. B kichik bulmaguncha
                if B <= A:
                    break
                B = B + A
                A = B - A
                B = B - A

            return A, B, C          # natija chiqishga tayyor buldi.
print(SortDec3(5,9,7))


#  14-misol.                    SONLARNI O'RNINI ALMASHTIRISH
print("\n~~~~~~~      14-misol.       ~~~~~~~~~~~~~~~~~~~")
def ShiftRight(A,B,C):
    A = A + B + C
    B = A - B - C
    C = A - B - C
    A = A - B - C

    return A, B, C
print(ShiftRight(3,6,5))

#  15-misol.                   SONLARNI O'RNINI ALMASHTIRISH
print("\n~~~~~~~      15-misol.       ~~~~~~~~~~~~~~~~~~~")
def ShiftRight(A,B,C):
    A = A + B + C
    C = A - B - C
    B = A - B - C
    A = A - B - C

    return A, B, C
print(ShiftRight(3,6,5))


#  16-misol.
print("\n~~~~~~~      16-misol.       ~~~~~~~~~~~~~~~~~~~")
def Ishora(a):
    print(-1) if a<0 else print(1) if a>0 else print(0)
    return "son = %s" %(a)
print(Ishora(-6))


#  17-misol.
print("\n~~~~~~~      17-misol.       ~~~~~~~~~~~~~~~~~~~")
def KvadratTenglama(A,B,C):
    Dis = B*B - 4*A*C
    x1 = ((-B) - (Dis**(0.5)))/ (2*A)
    x2 = ((-B) + (Dis**(0.5)))/ (2*A)

    if Dis < 0:
        return "Yechimga ega emas."
    if Dis > 0:
        return "2 ta yechimga ega."
    if Dis == 0:
        return "1 ta yechimga ega."

print(KvadratTenglama(1,4,4))


#  18-misol.
print("\n~~~~~~~      18-misol.       ~~~~~~~~~~~~~~~~~~~")
def DoiraYuzi(R):
    return 3.14*R*R
print(DoiraYuzi(6))


#  19-misol.           markazi 1 nuqtada bo'lgan R1 va R2 radiusga ega 2 ta aylananing ustma-ust tushmaydigan qismi yuzini    ?????????????????????????????????????????????????????
print("\n~~~~~~~      19-misol.       ~~~~~~~~~~~~~~~~~~~")
def RingS():
    pass


#  20-misol.
print("\n~~~~~~~      20-misol.       ~~~~~~~~~~~~~~~~~~~")
def TriangleP(a, b):
    c = pow(a*a + b**2, 0.5)
    per = a + b + c
    return c
print(TriangleP(8, 6))


#  21-misol.
print("\n~~~~~~~      21-misol.       ~~~~~~~~~~~~~~~~~~~")
def SumRange(A,B):
    if A > B:
        return 0
    else:
        S = 0
        for i in range(A, B+1):
            S += i
        return S

print(SumRange(3, 9))


#  22-misol.
print("\n~~~~~~~      22-misol.       ~~~~~~~~~~~~~~~~~~~")
def Calc(A, B, Op):
    if Op == 1:
        return ("%r - %a = %i" % (A, B, A-B))
    elif Op == 2:
        return (f"{A} * {B} = {A*B}")
    elif Op == 3:
        return ("{1} / {2} = {0}".format(A/B, A, B))
    elif Op == 4:
        return ("%d + %.f = %g" %(A, B, A+B))
print(Calc(15,5,4))


#  23-misol.
print("\n~~~~~~~      23-misol.       ~~~~~~~~~~~~~~~~~~~")
def Quarter(x, y):
    if x > 0 and y > 0:
        return "1-chorakda"
    elif x < 0 and y > 0:
        return "2-chorakda"
    elif x < 0 and y < 0:
        return "3-chorakda"
    elif x > 0 and y < 0:
        return "4-chorakda"
    else:   return "0  o'qda joylashgan"
print(Quarter(6, -4))


#  24-misol.
print("\n~~~~~~~      24-misol.       ~~~~~~~~~~~~~~~~~~~")
def Even(K):
    if K%2 == 0:
        return True
    else:
        return False

for i in range(4, 7):
    print(Even(i))


#  25-misol.                            # son kvadratmi yoki yo'q aniqlash
print("\n~~~~~~~      25-misol.       ~~~~~~~~~~~~~~~~~~~")
def Square(K):
    t = (int(K**0.5)*int(K**0.5))
    if t == K:
        return pow(t, 0.5)
    else:
        return "kvadrati emas"
print(Square(17))
print(Square(16))
print(Square(18))



#  26-misol.     2                                                      # 5 ni darasimi yo'qmi
print("\n~~~~~~~      26-misol. 2      ~~~~~~~~~~~~~~~~~~~")                              #    !!!!!!!!!!????
def isPower(a):
    k=1; i=1
    while a > k:
        k = 5**i
        i += 1
    if a == k:
        return True
    else:
        return False
sana = 0
for i in range(5):
    k = int(input("k= "))
    r = isPower(k)
    if r:
        sana += 1
print(sana)


#  27-misol.
print("\n~~~~~~~      27-misol.       ~~~~~~~~~~~~~~~~~~~")
def IsPowerN(K, N):
    while N > 0:
        N /= K
        if N == 1:
            return "darajasi"
print(IsPowerN(3, 27))


#  28-misol.                                                        ?????????????????????????
print("\n~~~~~~~      28-misol.       ~~~~~~~~~~~~~~~~~~~")
def IsPrime(K):
    if K == 2:
        return f"1)  {K}  tub son"
    s = 0
    for i in range(3, K+1, 2):
        if K%i != 0:
            s += 1
            print(f"2) {s}  natija: {K} tub son emas.  {K} % {i} = {K%i}")
        if s >= 1:
                return f"3)  {K} tub son"

print(IsPrime(7))
print()
print(IsPrime(24))



#  29-misol.                                # raqamlar soni
print("\n~~~~~~~      29-misol.       ~~~~~~~~~~~~~~~~~~~")
def DigitCount(K):
    s = 0
    while K > 0:
        s += 1
        K //= 10
    return f"{s} ta"
print(DigitCount(58))


#  30-misol.  1                             N raqami K sonini ichidaligini tekshirish
print("\n~~~~~~~      30-misol.  1     ~~~~~~~~~~~~~~~~~~~")
def DigitN(K, N):
    if str(N) in K:
        return f"{K} ni ichida {N} mavjud."
    else:
        return "mavjud emas"

print(DigitN(str(6548), 7))


#  30-misol.  2                       K sonini N- tartibidagi raqam. chapdan o'ngga qarab
print("\n~~~~~~~      30-misol.  2     ~~~~~~~~~~~~~~~~~~~")
def Innum(K, N):
    k = K

    #============   xonalar sonini aniqlab olamiz     ==================
    xonasi = 1              # sonning xonalarin xisoblaydi
    while K > 9:
        K = K//10
        xonasi += 1
    print(xonasi, "xanalik son \n")        # necha xonali ekanini chiqaradi

    #============    natija chiqaramiz     ==================
    son = 0
    for i in range(1, xonasi+1):
        son = k // (10**(xonasi-i))
        k %= 10**(xonasi-i)
        if i == N:
            return f"{N}- tartibdagi son= {son}"

print(Innum(45678932, 6))


#  30-misol.  3                       K sonini N- tartibidagi raqam. chapdan o'ngga qarab. optimali
print("\n~~~~~~~      30-misol.  3     ~~~~~~~~~~~~~~~~~~~")
def digitN(k, n):
    if k < 10**(n-1):
        return -1
    while k > 10**n:
        k //= 10
    return k%10
print(digitN(1535416431, 6))



#  31-misol.                                                            ???????????????????????????????????
print("\n~~~~~~~      31-misol.       ~~~~~~~~~~~~~~~~~~~")
def IsPolindrom(N):
    d = N;  s = 0               # N ni d ga saqlab quyamiz
    while N > 0:
        q = N % 10
        N //= 10
        s = s*10 + q
    if d == s:         return "Polindrom"
    else:              return "Polindrom emas"

print(IsPolindrom(54645))


#  32-misol.                                        gradusni radianga aylantirish
print("\n~~~~~~~      32-misol.       ~~~~~~~~~~~~~~~~~~~")
def DegToRad(D):
    radian = 3.14*D/180
    return radian
print(DegToRad(90))

#  33-misol.                                        radianni gradusga aylantirish
print("\n~~~~~~~      33-misol.       ~~~~~~~~~~~~~~~~~~~")
def RadToDeg(R):
    deg = R*180/3.14
    return deg
print(RadToDeg(35))


#  34-misol.                                            Factorial
print("\n~~~~~~~      34-misol.       ~~~~~~~~~~~~~~~~~~~")
def Fact(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    return factorial
print(Fact(4))

#  35-misol.                                            Factorial!!
print("\n~~~~~~~      35-misol.       ~~~~~~~~~~~~~~~~~~~")
def Fact2(N):
    if N%2 != 0:
        factorial = 1
    else:
        factorial = 2

    for i in range(factorial, N+1, 2):
        factorial *= i
    return factorial
print(Fact2(5))


#  36-misol.                                                            Fibonachi
print("\n~~~~~~~      36-misol.       ~~~~~~~~~~~~~~~~~~~")
def Fib(N):
    f0 = 0;  f1 = 1
    while f1 < N:
        fi = f0 + f1
        f0 = f1
        f1 = fi
        print(fi, end=" ")
print(Fib(25))




#  37-misol.
print()
print("\n~~~~~~~      37-misol.       ~~~~~~~~~~~~~~~~~~~")
def Power1(A, B):
    return A**B
print(int(input(Power1(2, 3))))

#  38-misol.                                                                ???????????????????????
print("\n~~~~~~~      39-misol.       ~~~~~~~~~~~~~~~~~~~")
def Power2(A, N):
   pass


#  39-misol.                                                        ?????????????????????????
print("\n~~~~~~~      39-misol.       ~~~~~~~~~~~~~~~~~~~")
def Poer3(A, N):
    pass



#  40-misol.
print("\n~~~~~~~      40-misol.       ~~~~~~~~~~~~~~~~~~~")
def Exp1(x, e):
    f = 1;  S = 1
    for i in range(1, e+1):
        f *= i
        S = S + (x**i)/f
    return S
print(Exp1(2, 5))


#  41-misol.                                                            ?????????????????????????????????????
print("\n~~~~~~~      41-misol.       ~~~~~~~~~~~~~~~~~~~")


#  42-misol.                                                            ?????????????????????????????????????
print("\n~~~~~~~      42-misol.       ~~~~~~~~~~~~~~~~~~~")


#  43-misol.                                                            ?????????????????????????????????????
print("\n~~~~~~~      43-misol.       ~~~~~~~~~~~~~~~~~~~")


#  44-misol.                                                            ?????????????????????????????????????
print("\n~~~~~~~      44-misol.       ~~~~~~~~~~~~~~~~~~~")


#  45-misol.                                                            !!!!!!!!!!!!?????????????????????????
print("\n~~~~~~~      45-misol.       ~~~~~~~~~~~~~~~~~~~")
def Power4(x, e, a):
    s = 1
    f = 1
    for i in range(1, e+1):
        s += ((a - i + 1)*(x**(i)))/f

    return s
print(Power4(0.2, 3, 3))



#  46-misol.                                    =================       E K U B         =========================
print("\n~~~~~~~      46-misol.   E K U B     ~~~~~~~~~~~~~~~~~~~")
def Ekub(A, B):
    while A > 0 and B > 0 and A != B:
        if A > B:                          # kichigini qoldiqqa olib, qoldiqli bulish usulida ishlanadi
            A %= B
        else:
            B %= A
        if A == 0:      A = b           # nol raqam chiqarmaslik uchun raqamlarni almashtirib olamiz
        if B == 0:      B = A           # buni o'rniga >>> return a+b  <<< qilsak nol raqamdan boshqasi chiqadi. nol chiqmaydi.
        return f"Ekub: {B}"
print(Ekub(15,45))


#  47-misol.                                          Qisqarmas kasr   ( 5/3, 7/4, 15/4 )
print("\n~~~~~~~      47-misol.       ~~~~~~~~~~~~~~~~~~~")
def Frac1(a, b):
    k, l = a, b
    while a != b:
        if a > b:
            a %= b
        else:
            b %= a
        if a == 0:
            a = b
        if b == 0:
            b = a
    return f"{int(k/a)}/{int(l/b)}"
print(Frac1(5, 9))


#  48-misol.
print("\n~~~~~~~      48-misol.       ~~~~~~~~~~~~~~~~~~~")


#  49-misol.
print("\n~~~~~~~      49-misol.       ~~~~~~~~~~~~~~~~~~~")


#  50-misol.                                sekundni soatga ugirish
print("\n~~~~~~~      50-misol.       ~~~~~~~~~~~~~~~~~~~")
def TimeToHMS(T):
    H = T//3600%24   # H = T//3600          # soat
    M = T//60%60     # M = T%3600//60       # Minut
    S = T%60         # S = T%60             # Sekund

    return f"{H} : {M} : {S}"
print(TimeToHMS(5821))

#  51-misol.                        kiritilgan soatga  T sekund oshirish
print("\n~~~~~~~      51-misol.       ~~~~~~~~~~~~~~~~~~~")
def IncTime(T, H, M, S):
    h = T//3600%24 + H             # soat
    m = T//60%60 + M               # Minut
    s = T%60 + S                   # Sekund

    return f"{h} : {m} : {s}"
print(IncTime(3722, 1, 20, 22))


#  52-misol.                                                    Kabisa yilini topish
print("\n~~~~~~~      52-misol.       ~~~~~~~~~~~~~~~~~~~")
def IsLeapYear(Y):
    if Y%100 == 0 and Y%400 !=0:
        return False             # ("kabsa emas")
    elif Y%4 == 0:
        return True              #("kabisa")
    else:
        return False             # ("Kabisa emas")
print(IsLeapYear(2001))

#  53-misol.                                                    sana oy yilni chiqarish
print("\n~~~~~~~      53-misol.       ~~~~~~~~~~~~~~~~~~~")
def MonthDays(M, Y):
    if M == 2:
        return 28 + IsLeapYear(Y)
    elif M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        return 31
    else:
        return "bunday oy yuq"

print(MonthDays(3, 2400))


#  54-misol.                                        1 kun oldingi sanani aniqlash.  52-53-misollardan foydalanib
print("\n~~~~~~~      54-misol.       ~~~~~~~~~~~~~~~~~~~")
def PrevDate(D, M, Y):
    D = D + 1
    if MonthDays(M, Y) == 28 and D == 29:
        D = 1;   M = M + 1
    elif MonthDays(M, Y) == 29 and D == 30:
        D = 1;   M = M + 1
    elif MonthDays(M, Y) == 30 and D == 31:
        D = 1;   M = M + 1
    elif MonthDays(M, Y) == 31 and D > 31:
        D = 1;      M = M + 1
        if M >12 and D == 1:
            M = 1;  Y = Y + IsLeapYear(Y)
    elif M > 12 or (M==2 and D > 29):
        return "sanani tekshiring!"
    return (Y, M, D)

print("2", PrevDate(27, 2, 2400))
print("3", PrevDate(28, 2, 2400))
print("4", PrevDate(29, 2, 2400))



#  55-misol.                                    1 kun keyingi kunni aniqlash
print("\n~~~~~~~      55-misol.       ~~~~~~~~~~~~~~~~~~~")
#    kabisa yili yoki kabisa emasligini aniqlash
def IsLeapYear(Y):
    if Y%100 == 0 and Y%400 ==0:
        return False   #("kabsa emas")
    elif Y%4 == 0:
        return True    #("kabisa")
    else:
        return False   #"Kabisa emas"
print(IsLeapYear(2001))

#                    bir kun keyingi kunni aniqlash
def NextDate(D, M, Y):
    D = D + 1
    if (M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12):
        if D == 32:
            D, M = 1, M + 1
            if M == 13:
                M = 1
                Y = Y + 1

    if D == 31 and (M == 4 or M == 6 or M == 9 or M == 11):
        D, M = 1, M + 1

    if IsLeapYear(Y) == False and M == 2:
        D = 1
        M += 1
    elif IsLeapYear(Y) == True and M == 2:
        M = M + 1
        D = 1

    return f"{D}:{M}:{Y}"

print(NextDate(31, 12, 2020))
print(NextDate(28, 2, 2004))
print(NextDate(28, 2, 2400))
print(NextDate(29, 2, 2020))
print(NextDate(5, 10, 1993))
print(NextDate(30, 4, 2020))






#  56-misol.                                            Nuqtalar orasidagi masofa
print("\n~~~~~~~      56-misol.       ~~~~~~~~~~~~~~~~~~~")

x1,y1 = 5, 4
x2,y2 = 8, 5
x3,y3 = 9, 3

def Leng(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

#  57-misol.                                                              Uchburchak Peremetr
print("\n~~~~~~~      57-misol.       ~~~~~~~~~~~~~~~~~~~")
def Perim(xA, yA, xB, yB, xC, yC):
    Peremetr = Leng(xA, yA, xB, yB) + Leng(xB, yB, xC, yC) + Leng(xA, yA, xC, yC)
    return Peremetr

#  58-misol.                                                               Uchburchak yuzasi
print("\n~~~~~~~      58-misol.       ~~~~~~~~~~~~~~~~~~~")
def Area(x1,y1,x2,y2,x3,y3):
    a, b, c = Leng(x1, y1, x2,y2), Leng(x2, y2, x3,y3), Leng(x1, y1, x3,y3)
    P = a + b + c
    p = Perim(x1,y1, x2,y2, x3,y3)
    return (P*(P-a)*(P-b)*(P-c))**0.5,  (p*(p-a)*(p-b)*(p-c))**0.5

#  59-misol.
print("\n~~~~~~~      59-misol.       ~~~~~~~~~~~~~~~~~~~")
def Dist(x1,y1,x2,y2,x3,y3):
    print(2*Area(x1,y1,x2,y2,x3,y3)/Leng(x1,y1, x2,y2))
    print(2*Area(x1,y1,x2,y2,x3,y3)/Leng(x1,y1, x3,y3))
    return (2*Area(x1,y1,x2,y2,x3,y3)/Leng(x2,y2, x3,y3))

#  60-misol.
print("\n~~~~~~~      60-misol.       ~~~~~~~~~~~~~~~~~~~")
def Hieght(x1,y1,x2,y2,x3,y3):
    return Dist(x1,y1,x2,y2,x3,y3)



#########################################################################################################################
#########################################################################################################################
#########################################################################################################################


print(" N ta sonni EKUB ini topish")
def EKUB(a, b):
    while a != 0 and b != 0:
        if a>b:
            a %= b
        else:
            b %= a
    return a+b

n = int(input("sikl soni: "))
a = int(input("a= "))
for i in range(2, n+1):
    b = int(input("b= "))
    a = EKUB(a, b)
print(a)


#########################################################################
print(" N ta sonni EKUK ini topish")                    #  EKUB dan foydalanib
def EKUB(a, b):
    while a != 0 and b != 0:
        if a>b:
            a %= b
        else:
            b %= a
    return a+b

n = int(input("sikl soni: "))
a = int(input("a= "))
for i in range(2, n+1):
    b = int(input("b= "))
    a = EKUB(a, b)
print(a)


#########################################################################
print(" N ta sonni EKUK ini topish")
def EKUK(a, b):
    k = i = max(a, b)
    s = 0
    while True:
        if i % a == 0 and i % b == 0:
            break
        i += k
    return i

n = int(input("sikl soni: "))
a = int(input("a= "))
for i in range(2, n+1):
    b = int(input("b= "))
    a = EKUK(a, b)
print(a)



