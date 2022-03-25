#                                                   1-misol             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#########       1-usul.   bunda sal xato bor yana ishlab kuraman.
def misol_1_1(n):
    S = 0
    i = 0

    while n-i != 0:
        S += 1/(-(n-i))
        i += 1
    if n-i == 0:
        for i in range(i-1,-1,-1):
            S += 1 / ((n - i))

    return S
print(misol_1_1(3))


#########        2-usul.  to'g'ri ishladi.
def misol_1_2(n):
    S = 0
    i = 0

    while n-i != 0:
        S += 1/(-(n-i))
        i += 1
    print("S1=", S)
    j = 0;  s = 0
    while n-j != 0:
            s += 1 / ((n - j))
            j += 1
    print("S2=", S)

    return S + s
print(misol_1_2(3))




#                                                   2-misol             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def misol_2(a, b):
    butun = 0
    while a > b:
        a -= b                  # qoldiqni olamiz
        butun += 1              # butun qismini aniqlaymiz
    return f"butun qismi: {butun},   qoldiq: {a} "

print(misol_2(7, 5))
print(misol_2(8, 3))
print(misol_2(19, 4))
print(misol_2(65, 25))
print(misol_2(81, 12))
print()




#                                                    3-misol                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def EKUK(a, b):  ## EKUK ni hisoblab olamiz
    if a > b:  # maksimal sonni topib olamiz
        k = a
        i = a
    else:
        k = b;  i = b

    while True:  # a va b ga bulinadigan sonni topishni hisoblaymiz
        if k % a == 0 and k % b == 0:
            break
        else:
            k += i
    return k

n = int(input("sikl soni: "))  # necha marta sikl aylanishini kiritamiz
a = int(input("a= "))
for i in range(n - 1):
    b = int(input("b= "))
    a = EKUK(a, b)

print(a)  # funksiyani natijasini chiqaramiz
print()



#                                                    4-misol                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def misol_4(N):
    maxi_t = 0; min_t = 0; maxi = 0     # maximum va minimum son tartibi;   maxi - maximum son

    for i in range(1, N+1):
        a = int(input("a= "))
        if maxi < a:
            maxi = a
            min_t = i
        if maxi <= a:
            maxi = a
            maxi_t = i
    return "maximum son= {0} ;   minimum tartib: {2};   maksimum tartib: {1}".format(maxi, maxi_t, min_t)

print(misol_4(int(input("sikl soni N="))))
print()



#                                                    5-misol                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def misol_5(N):
    m1, m2, m3 = -1000000000000, -1000000000000, -1000000000000
    for i in range(N):
        a = int(input("a= "))

        if m1 <= a:                            # m1 eng kattasi ekanligini tekshiramiz
            m3 = m2
            m2 = m1
            m1 = a

        if m2 <= a and m1 > a:                  # m2 o'rtancha sonni oladi
            m3 = m2
            m2 = a

        if m3 <= a and m2 > a and m1 > a:       # m3 kichik sonni aniqlash
            m3 = a

    return "%s, %s, %s" %(m1, m2, m3)           # natijani chop etamiz

print(misol_5(int(input("sikl soni N= "))))





##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def misol_1_1(n):
    S = 0
    i = 0

    while n-i != 0:
        S += 1/(-(n-i))
        i += 1

    print("S=", S)
    if n-i == 0:
        print("i=", i, "n=", n)
        for i in range(i-1,-1,-1):
            S += 1 / ((n - i))
            print("i=", i, "n=",n,"  S1=", S)
    return S
print(misol_1_1(3))
print()

i = 3; n = 3
if n - i == 0:
    for i in range(i-1, -1, -1):
        S = 1/(n-i)
        print("i=", i, "  SM=", S)



m = -1/3
k = 1/3
print(m, k, m+k)



#######################################################################################################
#######################################################################################################
#######################################################################################################

#                            D O' S T      SON
n = 3000
for i in range(1, n+1):
    S = 0
    for j in range(1, i//2 + 1):
        if i%j == 0:
            S += j
    if S > i:
        K = 0
        for j in range(1, S//2 + 1):
            if S%j == 0:
                K += j
        if K == i and K != S:
            print(K, S)


