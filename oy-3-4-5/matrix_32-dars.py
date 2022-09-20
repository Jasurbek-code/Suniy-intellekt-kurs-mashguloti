#  1-misol.
m = 8
n = 7

matrix = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(10*i)
    matrix.append(a)

for i in range(m):
    print(*matrix[i])


#  2-misol.
m = 8
n = 7

matrix = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(10*j)
    matrix.append(a)
for i in range(m):
    print(*matrix[i])


#  3-4-misol.
m = 4
n = 4
k = [1,2,3,4]

matrix = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(k[i])               # i -> j ga uzgarsa 3-misolni beradi
    matrix.append(a)

for i in range(m):
    print(*matrix[i])


#  5-misol.
m = 4
n = 4
k = [1,2,3,4]
d = 2

matrix = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(k[i]+d)
    matrix.append(a)

for i in range(m):
    print(*matrix[i])

#  12-misol.
# m=8; n=7
a = [[randint(1, 10) for j in range(n)] for i in rnage(m)]
for i in range(m):
    print(*a[i])

b = []
for i in range(n):
    c = []
    if i%2 == 0:
        for j in range(m):
            c.append(a[j][i])
    else:
        for j in range(m-1, -1, -1):
            c.append(a[j][i])
    b.append(c)
print()

for i in range(m):
    for j in range(n):
        print(b[j][i], end=" ")
    print()


#  12-misol.         2-usul.    optimalroq
a = [[randint(1, 10) for j in range(n)] for i in rnage(m)]
for i in a:
    print(*i)
print()

for i in range(m//2):
    for j in range(1,  n, 2):
        a[i][j],  a[m-i-1][j] = a[m-i-1][j], a[i][j]
for i in a:
    print(*i)
print()


#  13-misol.                                            diagonali 1 ga teng matritsa
n = 6
b = []
for i in range(n):
    a = []
    for j in range(n):
        if i==j or  i+j==n-1:
            a.append(1)
        else:
            a.append(0)
    b.append(a)
for i in range(n):
    print(*b[i])



#  14-misol.                              2,3,4,5 lar uchburchak shaklda hammasi kvadrat hosil qilish
n = 5
b = []
for i in range(n):
    a = []
    for j in range(n):
        if i==j or i+j == n-1:
            a.append(0)
        elif i < j and i+j < n-1:
            a.append(2)
        elif i < j and i+j > n-1:
            a.append(3)
        elif i > j and i+j > n-1:
            a.append(4)
        else:
            a.append(5)
    b.append(a)

for i in range(n):
    print(*b[i])



#  15-misol.   1-usul                               spiral hosil qilish, tashqaridan boshlab

n = 5

a = [[0 for i in range(5)] for i in range(6)]         # indexlarga son hosil qilib olish
l = 1; r = 1
u = n; d = n

k = n
for i in range(n):
    for j in range(i, k):
        a[i][j] = l
        l += 1
    u = l
    for j in range(i+1, k):
        a[j][k-1] = u
        u += 1
    r = u
    for j in range(k-2, i-1, -1):
        a[k-1][j] = r
        r += 1
    d = r
    for j in range(k-2, i, -1):
        a[j][i] = d
        d += 1
    l = d
    k -= 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()


#  15-misol.   2-usul                               spiral hosil qilish, ichidan boshlab
n = 5

a = [[0 for i in range(5)] for i in range(6)]
c = n**2                # sonni kvadratidan 1 ayirib ketaveramiz

k = n
for i in range(n):
    for j in range(i, k):
        a[i][j] = c
        c -= 1
    for j in range(i+1, k):
        a[j][k-1] = c
        c -= 1
    for j in range(k-2, i-1, -1):
        a[k-1][j] = c
        c -= 1
    for j in range(k-2, i, -1):
        a[j][i] = c
        c -= 1
    k -= 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()



#  15-misol.   3-usul                               spiral hosil qilish


#  15-misol.   4-usul                               spiral hosil qilish
#  15-misol.   5-usul                               spiral hosil qilish





#  16-misol.                        diagonal buyicha 2 va 1 markaziy diagonalda, qolganlari 0 chiqarish
n = 5
b = []
for i in range(n):
    a = []
    for j in range(n):
        if i == j:
            a.append(2)
        elif abs(j-i) == 1:
            a.append(1)
        else:
            a.append(0)
    b.append(a)

for i in range(n):
    print(*b[i])



#  17-misol.                        2 ta matritsani ko'paytirish
import random
n = 2
a = [[random.randint(1,10) for j in range(n)] for i in range(n)]
b = [[random.randint(1,10) for j in range(n)] for i in range(n)]
c = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    print(*a[i])

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] = a[i][k] * b[k][j]
print(*c)

#  25-misol.
n = 3
a = [[random.randint(10,99) for j in range(n)] for i in range(n)]

for i in a:
    print(*i)
print()
j=0
for i in a:
    if sum(i) == min(sum(i) for i in a):
        print(sum(i), j)
        break
    j += 1


#  27-misol.
n = 3
a = [[random.randint(10,99) for j in range(n)] for i in range(n)]

for i in a:
    print(*i)
print()

for i in a:
    if sum(i) == min(sum(i) for i in a):
        print(max(i))
        break



#  28-misol.
n = 3
a = [[random.randint(10,99) for j in range(n)] for i in range(n)]

for i in a:
    print(*i)
print()

x = True
for j in range(n):
    s = 0
    for i in range(n):
        s += a[i][j]
    if x:
        maxi = s
        k = j
        x = False
    if maxi < s:
        maxi = s
        k = j
mini = a[0][k]
for i in range(n):
    if mini > a[i][k]:
        mini = a[i][k]
print(mini)



#  32-misol.
m, n = int(input("m= ", )), int(input("n= ", ))
a = [[random.randint(-10, 10) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)

for i in range(n):
    s1, s2 = 0, 0
    for j in range(m):
        if a[i][j] < 0:
            s1 += 1
        if a[i][j] > 0:
            s2 += 1
    if s1 ==s2:
        print(a[i])
        break
else:
    print("Bunday satr yuq.")



#  37-misol.
a = [[1,2,4], [2,1,5,4], [3,1,2,4]]

s = 0
for i in range(1, len(a)):
    if sorted(a[0]) == sortes(a[i]):
        s += 1
print(s)



#  46-misol.
m = 3;  n = 3
a = [[int(input("a= ")) for i in range(n)] for i in range(m)]
for i in a:
    print(*i)

for i in range(n):
    maxi = a[0][j]
    k = 0
    for i in range(m):
        if maxi < a[i][j]:
            maxi = a[i][j]
            k = 1
    if maxi == min(a[k]):
        print(maxi, a[k])
        break


#  54-misol.                      # hammasi manfiy bo'lgan 1-ustunni almashtirih
m = 3;  n = 3
a = [[random.randint(-10, 10) for i in range(n)] for i in range(m)]
for i in a:
    print(*i)
print()

k = n -1

for j in range(n):
    x= True
    for i in range(m):
        if a[i][j] >= 0:
            x = False
    if x:
        k = j
        break

for i in range(m):
    a[i][k], a[i][n-1] = a[i][n-1], a[i][k]
for i in a:
    print(*i)


#  57-misol.
m = 4;  n = 4
a = [[random.randint(1, 9) for i in range(n)] for i in range(m)]
for i in a:
    print(*i)
print()

for i in range(m//2):
    for j in range(n//2):
        a[i][j], a[i + m//2][j + n//2] = a[i + m//2][j + n//2], a[i][j]

for i in a:
    print(*i)


#  58-misol.
m = 4; n = 4
a = [[random.randint(1, 9) for i in range(n)] for i in range(m)]
for i in a:
    print(*i)
print()

for i in range(m // 2):
    for j in range(n // 2):
        a[i][j], a[i + m // 2][j - n // 2] = a[i + m // 2][j - n // 2], a[i][j]

for i in a:
    print(*i)


#  67-misol.
m = 3;  n = 3
a = [[random.randint(-10, 10) for i in range(n)] for i in range(m)]
for i in a:
    print(*i)
print()

j = 0

while j < len(a):
    x = True
    i = 0
    while i < len(a):
        if a[i][j] <= 0:
            x = False
        i += 1
    if x:
        for i in range(len(a)):
            a[i].pop(j)
    j += 1

for i in a:
    print(*i)




#  75-misol.                                # to'g'ri yonlarini tekshirish                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#import random
m = 6;  n = 6
a = [[random.randint(1, 9) for i in range(n)] for i in range(m)]
b = []
for i in a:
    print(*i)
print()

for i in range(len(a)):
    c = []
    for j in range(len(a[i])):
        c.append(a[i][j])
    b.append(c)
#print(b)
print()

for i in range(m):
    for j in range(n):
        if i == 0 and j != 0 and j != n-1:
            if a[i][j] > a[i +1][j] and a[i][j] > a[i][j+1] and a[i][j] > a[i][j-1]:
                b[i][j] = 0
        elif i == m-1 and j != 0 and j != n-1:
            if a[i][j] > a[i - 1][j] and a[i][j] > a[i][j+1] and a[i][j] > a[i][j-1]:
                b[i][j] = 0
        elif j ==0 and i != 0 and i != m-1:
            if a[i][j] > a[i][j+1] and a[i][j] > a[i+1][j] and a[i][j] > a[i-1][j]:
                b[i][j] = 0
        elif j == n-1 and j !=0 and i != m-1:
            if a[i][j] > a[i][j-1] and a[i][j] > a[i+1][j] and a[i][j] > a[i-1][j]:
                b[i][j] = 0
        elif i == 0 and j ==0:
            if a[i][j] > a[i+1][j] and a[i][j] > a[i][j+1]:
                b[i][j] = 0
        elif i == m-1 and j ==0:
            if a[i][j] > a[i-1][j] and a[i][j] > a[i][j+1]:
                b[i][j] = 0
        elif i == 0 and j == n-1:
            if a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1]:
                b[i][j] = 0
        elif i == m and j == n-1:
            if a[i][j] > a[i-1][j] and a[i][j] > a[i][j-1]:
                b[i][j] = 0
        else:
            if a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1] and a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j]:
                b[i][j] = 0

for i in b:
    print(*i)



#  80-misol.
m = 3
a = [[random.randint(1, 9) for i in range(m)] for i in range(m)]

for i in a:
    print(*i)

print(sum([a[i][j] for i in range(m)]))                # chap tomondan boshlanuvchi diagonal yig'indisi
print(sum([a[i][m-j-1] for i in range(m)]))            # o'ng tomondan boshalanuchi diagonal yig'indisi




#  81-misol.                                   satrni ustunga utqazish
m = 3
a = [[random.randint(1,9) for i in range(m)] for j in range(m)]

for i in a:
    print(*i)
print()

a = [[a[i][j] for i in range(m-1, -1, -1)] for j in range(m)]

for i in a:
    print(*i)


#  84-misol.                                 
for i in a:
    print(*i)
print()

b = [i[::-1] for i in a][::-1]

for i in b:
    print(*i)



#  -misol.
#  -misol.
#  -misol.
#  -misol.
#  -misol.
#  -misol.
#  -misol.
#  -misol.