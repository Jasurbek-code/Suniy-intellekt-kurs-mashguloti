#        1-misol.
print("==========     1-misol.      =========")

a,b,c,d = int(input("a=")), int(input("b=")), int(input("c=")), int(input("d="))

a = a + b + c + d
b = a - b- c - d
c = a - b- c - d
d = a - b- c - d + m
a = a - b- c - d

print("a=", a, "b=", b, "c=", c, "d=", d)
print()


#        2-misol.      sonni teskari chiqarish
print("==========     2-misol.      =========")

son = int(input("Son="))

x1 = son % 10
x2 = son // 10 % 10
x3 = son // 100 % 10
x4 = son // 1000 % 10

print(x1*1000 + x2*100 + x3*10 + x4)
print()


#        3-misol.
print("==========     3-misol.      =========")

a, b, c = int(input("a=")), int(input("b=")), int(input("c="))

if a < b < c or a > b > c:           print("o'rtanchasi  b=", b)
elif b < a < c or b > a > c:           print("o'rtanchasi  a=", a)
elif a < c < b or a > c > b:           print("o'rtanchasi  c=", c)
else:                                 print("teng son kiritmang!")
print()



#        4-misol.
print("==========     4-misol.      =========")

n = int(input("N butun soni="))
x = int(input("x haqiqiy son="))

N, s = 1, 0                                     # faktorialni boshlang'ich qiymati, oig'indini boshlang'ich qiymati

for i in range(3, n+1, 2):
    N *= 2*i+1                                  # faktorialni hisoblab olish uchun
    s += ((-1)**i)*pow(x, 2*i+1)/(N)

    print("S=", s)



#        5-misol.
print("\n==========     5-misol.      =========")

N = int(input("Sonni kichigini topish uchun son kiriting="))
k = 9           # kichik sonni o'zlashtirib olish uchun

while N > 0:
    n = N % 10
    N //= 10
    if n <= k:
        k = n

print("Eng kichik raqam=", k)


#        5-misol.               N ta son berilgan shu N ta sonni ichidan
#                               eng kichik musbat sonni topish kerak
print("\n==========     5-misol.   Haqiqiy shart     =========")

N = int(input("Sikl aylanishi nechtaligi yozing. N="))
minimum = 9

for i in range(N):
    a = int(input("son="))
    if minimum >= a and a > 0:
        minimum = a

print("Minimumi:", minimum)



