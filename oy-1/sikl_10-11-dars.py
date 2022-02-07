#  1-misol.                 # sonlarni 2 ta kattasi
a, b, c = 3,2,4

if a > b > c or b > a > c:      print("a=", a, "b=", b)
elif a > c > b or c > a > b:    print("a=", a, "c=", c)
elif b > c > a or c > b > a:    print("b=", b, "c=", c)
else:                           print("teng son kiritmang.")
print()

#  2-misol.                 kodli kalkulyator

takror = False      # True bulsa dastur ishlaydi
while takror:
    son1, son2 = 4,6  #int(input("a=")), int(input("b="))
    amal = input("< + >< - >< * >< />< // >< ** > amallarini kiriting:")

    if amal == "+":
        print("%s + %s =" %(son1, son2) , son1 + son2)
    elif amal == "-":
        print("%s - %s =" %(son1, son2) , son1 - son2)
    elif amal == "*":
        print("%s * %s =" %(son1, son2) , son1  * son2)
    elif amal == "/":
        print("%s / %s =" %(son1, son2) , son1 / son2)
    elif amal == "//":
        print("%s // %s =" %(son1, son2) , son1 // son2)
    elif amal == "**":
        print("%s ** %s =" %(son1, son2) , son1 ** son2)
    else:
        print("\nXato kiritildi. Qaytadan kiriting.")
        amal = input("< + >< - >< * >< />< // >< ** > amallarini kiriting:")

    yanami = input("Yana amal bajarasizmi? (ha, istalgan tugma):")          # dastur qayta ishlashini suraydi
    if yanami == "ha":
        pass
    else:
        takror = False




#  3-misol.             N ta sonni maximumini topish
N = 1 #int(input("  N="))
x = True; i = 0
while i < N:
    a = 5  #int(input("a="))
    if x:
        maxi = a
        x = False
    if maxi < a:
        maxi = a
    i += 1
print("Maximumi=", maxi)


#  4-misol.                 =================    N ta sonni  EKUBi      ========================
N = 1 #int(input("sikl soni N ="))
ekub = 4 #int(input("a="))
i = 1
while i < N:
    i += 1
    a = int(input("a="))
    if ekub % a == 0:
        continue
    j = min(ekub, a)
    while ekub % j != 0 or a % j != 0:
        j -= 1
    ekub = j
print("ekub:", ekub)

#  4-misol.                 =================    N ta sonni  EKUBi  Evklid usulida     ========================
print(36%9)
N = 1  #int(input("sikl soni N ="))
ekub = 4  #int(input("a="))
i = 1
while i < N:
    i += 1
    a = int(input("a="))
    while a != ekub:
        if ekub>a:
            ekub %= a
        else:
            a%=ekub

        if a == 0:
            a = ekub
        if ekub == 0:
            ekub = a
print("Evklid usulida ekub:", ekub)




#  5-misol.  1               =================      E K U K        ========================
a = 5 #int(input("a="))
b = 4 #int(input("b="))
k=i = max(a, b)
s = 0
while True:
    if i%a == 0 and i%b == 0:
        break
    i += k
print("1-usul. EKUK=", i)

#  5-misol. 2                =================      E K U K        ========================  optimal usul
a = 5 #int(input("a="))
b = 4 #int(input("b="))
k=i = max(a, b)
while i%a != 0 or i%b != 0:
    i += k
print("2-usul. EKUK=", i)


#  5-misol.                 =================    N ta sonni  EKUKi      ========================
N = 1 #int(input("sikl soni N ="))
ekuk = 4 #int(input("a="))
k=i = max(4,6)
while i < N:
    i += 1
    a = int(input("a="))


