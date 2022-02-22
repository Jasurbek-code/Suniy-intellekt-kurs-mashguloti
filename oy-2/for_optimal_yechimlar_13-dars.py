#  1-misol.
n = 9       # int(input("n="))
for i in range(1, n+1):
    print(i, end=" ")
print()

#  3-misol.         # sonni TUBligini topish                      !!!
a = 47
tub = True
for i in range(3, a+1):
    b = a%i
    print(b)
    if a % i != 0:
        tub = False
        break
    else:
        tub = True
if tub:
    print("tub son")
else:
    print("tub son emas")


#  4-misol.   1-usul                        <<<<<     TUB  soni n ta hadi      >>>>>        optimali
print("<<<<<     TUB  son n ta hadini topishning  1-usuli.")
n = 12
S = 1;  i = 3
print(2, end=" ")
while S < n:
    tub = True
    for j in range(3, (int(pow(i, 0.5)) + 1), 2):             # ildizi va toq sonlarni tekshiradi
        if i%j == 0:
            tub = False
            break
    if tub:
            print(i, end=" ")
            S += 1
    i += 2
print()

#  4-misol.   2-usul              <<<<<     TUB  soni n ta hadi      >>>>>
print("<<<<<     TUB  son n ta hadini topishning  2-usuli.")
n = 12
S = 1;  i = 3
print(2, end=" ")
while S < n:
    for j in range(2, i):
        if i%j == 0:
            break
    if i == j + 1:
        print(i, end=" ")
        S += 1
    i += 1
print()



#  5-misol.                             # faktorial.
n = 5
f = 1
for i in range(1, n+1):
    f *= i
    print(i, " faktoriali ", f)

#  6-misol.           TUB  sonni oxirgisini chiqarish                    !!!!!!??????
son = 23
i = son
while i <= son and i > 2:
    j, S = son, 0
    while j <= int(pow(i, 0.5)):
        if i % j == 0:
            S = 1
            break
        j -= 2
    if S == 0:
        print(i, end=" ")
        break
    if i%2 == 0:
        i -= 1
    else:
        i -= 2

#  7-misol.                             # EKUB
a = 9; b = 135
for i in range(1, b//a):
    b -= a
print("Ekubi=", b)

#  8-misol.                     sonni raqamlar yog'indisi
n = 2354
k = 0; m = 1
S = 0
for i in range(1, len(str(n)) + 1):
    k = n // (m) % (10)
    m *= 10
    S += k
print("yig'indi:", S)

#  9-misol.
n = 4
S = 0; b = 0
for i in range(1, n + 1):
    S += (b + i)
    print("hisobi=", S, b)
    b += i

#  10-misol.                    -1 kiritilmaguncha son kiritamiz.   min va max chiqaramiz
mini = 9; maxi = 0; sanoq = 0
while True:
    a = -1  #int(input("a="))
    if a == -1:
        break
    if a > 0:
        sanoq += 1
    if a < mini:
        mini = a
    if a > maxi:
        maxi = a
print("min:", mini, "  max:", maxi, "  musbat sonlar:", sanoq, "ta")

#  11-misol.                   murakkab sonlarni chiqarish                 ????????????????????????????????????


#  12-misol.                            kvadrat yasash
n = 5
for i in range(n):
    print("# "*n)
print()

#  13-misol.                karra jadvali
n = 5
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"%s x {j} =" %(i), i*j)
    print(end="\n")

#  14-misol.                n ta toq son chiqarish                  !!!
N = 9
S = 0
for i in range(1, N*2, 2):
        S += i
        print(i, end=" ")
print("   Yig'indisi=", S)

#  15-misol.                 n ta juft son chiqarish
N = 10
S = 0
for i in range(0, N*2, 2):
    S += i
    print(i, end=" ")
print("   Yig'indisi=", S)

#  16-misol.                    1+11+111+1111+ +...+n
n = 5
birlar = 0; S = 0
for i in range(n):
    birlar += 10**i
    S += birlar
    print("Birlar=", birlar, "   S=", S)

#  17-misol.                        fibonachi topish                                    ??????
print("      Fibonachi. ")
n = 8
f, f1 = 1, 0
for i in range(1, n//2 + 2):
    f1 += f
    f += f1
    print(f1,f, end=" ")
print()

#  18-misol.                   ikkita tub emas son yig'indisi kurinishida chiqarish                      !!!!
n = 25
x3 = True
for i in range(2, n//2 + 1):
    x1 = False;   x2 = False
    for j in range(2, i):
        if i%j == 0:
            x1 = True
            break
    for j in range(2, n-i):
        if (n-i)%j == 0:
            x2 = True
            break
    if x1 and x2:
        print(n, "=", i, "+", n-i)
        x3 = False
if x3:
    print("Yechim yo'q")


#  19-misol.
n = 5
for i in range(1, n+1):
    print("* "*i)

#  20-misol.
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#  21-misol.
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

#  22-misol.
n = 5
s = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        s += 1
        print(s, end=" ")
    print()

#  23-misol.
print("            23-misol.")
n = 4
s = 0
for i in range(1, n+1):
    print(f"%s" %("-"*(n-i)), end=" ")
    for j in range(1, i+1):
        s += 1
        print(s, end=" ")
    print()

#  24-misol.
print("        24-misol.")
n = 5
for i in range(1, n+1):
    print(" "*(n-i), "* "*i,   end=" ")
    print()

#  25-misol.
n = 5
for i in range(1, n+1):
    print(" " * (n - i), end=" ")
    for j in range(1, i+1):
        print(i, end=" ")
    print()

#  26-misol.
print("        26-misol.")
n = 7
for i in range(1, n+1, 2):
    print(" "*(n-i), "# "*i,   end=" ")
    print()

#  27-misol.                    Floyd  uchburchagi                                  !!!!!!!!?
print("     Floyd  uchburchagi")
n = 7
k = 1               # juft va toq qilish uchun
for i in range(1, n+1):
    for j in range(1, i+1):
        print((k)%2, end=" ")
        k += 1
    print(" ")

print("  27-misol.    2-usul.")
n = 5
s = 1
for i in range(1, n+1):
    if i%2 != 0:
        a = 1
        for j in range(1, i+1):
            print(a, end=" ")
            a += (-1)**j

    if i%2 == 0:
        a = 0
        for k in range(1, i+1):
            print(a, end=" ")
            a += (-1)**(k+1)
    print()


#  28-misol.  1-usul          Romb chiqarish
print("      28-misol.   1-usul.")
n = 5
for i in range(1, n+1):
    print(" "*(n-i), "# "*i,   end=" ")
    print()
for i in range(1, n+1):
    print(" "*(i), "# "*(n-i),   end=" ")
    print()

#  28-misol.  2-usul                        Romb chiqarish
print("      28-misol.   2-usul.")          # orasida joy tashlanmagan varianti
n = 5

for i in range(0, n+1, 2):
    print(" "*(n-i), "#"*(2*i+1),   end=" ")
    print()
for i in range(1, n+1, 2):
    print(" "*(i), "#"*(2*(n-i)+1),   end=" ")
    print()


#  29-misol.                        Pascal uchburchagi                      !!!!!!!!????
print("     Pascal  uchburchak")
n = 5
f1 = f2 = 1
for i in range(n+1):
    print(" "*(2*n-2*i), end="")
    for j in range(i+1):
        if j == 0:
            print(1, end="  ")
            continue
        f2 = f1*(i+1-j)/j
        f1=f2
        print(int(f2), end="  ")
    print()




#  30-31-misol.         ??????????????????????


#  32-misol.                kvadrat   raqamlarda
print("  kvadrat")
n = 5
for i in range(0, n+1):
    #print()
    for j in range(0, n+1):
        print(abs(i-j), end=" ")
    print()
print()

#  32-misol.                kvadrat  raqamlarda,  1 va 0 faqat.       uzimniki optimal
print("  kvadrat  ")
n = 3
for i in range(0, n):
    for j in range(0, n):
        if (j-i) == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

#  32-misol.                kvadrat  raqamlarda,  1 va 0 faqat.
print("  kvadrat  ")
n = 3
m = 1
for i in range((n-1), -1, -1):
    l = 1
    for k in range(1, i + 2):
        print(l, end=" ")
        l = 0
    print(" ")
    if m == n:
        break
    for b in range(m, 0, -1):
        print(0, end=" ")
    m += 1

#  32-misol.                kvadrat  raqamlarda,  1 va 0 faqat. tepadagini teskarisi
print("  kvadrat  ")
n = 3
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
print()

#  33-misol.
n = 3
print(n, "soni ikkilik sanoq sistemasida:", bin(n).lstrip("0b"))
s = 0;  b = 0
while n > 0:
    a = n%2
    n //= 2
    s += a*(10**b)
    b += 1
    #print(a)   kerakmas
print(s)

#  34-misol.
n = 15
print(n, "sakkizlikda:", oct(n).lstrip("0o"))
s = 0;  b = 0
while n > 0:
    a = n%8
    n //= 8
    s += a*(10**b)
    b += 1
    #print(a)   kerakmas
print(s)

#  35-misol.
n = 15
print(n, "o'nlik sanoqda:", n)
s = 0;  b = 0
while n > 0:
    a = n%10
    n //= 10
    s += a*(10**b)
    b += 1
    #print(a)   kerakmas
print(s)




#############     raqamdan boshqa shakl
print()
print()
print("boshqa shakl")
n = 5
k = 1; m= 0
for i in range(1, n+1):
    print(" " * (n - i), end=" ")
    for j in range(1, i+1):
        print(j-m, end=" ")
    m -= 1
    print()

print("oraliqdagi sonni darajasi kamayuvchi, son usuvchi yig'indini topish.")
a,b = 1, 4
s = 0
for i in range(a, b+1):
    s += (i)**(b)             # <<<<   s += i**(b+a-i)   optimali    >>>>>>>>>>
    print(i,"^", b, " ", s)
    b -= 1