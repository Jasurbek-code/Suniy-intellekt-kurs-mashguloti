#                       1-misol
import random

# massiv hosil qilib olish
a = [random.randint(1, 10) for i in range(10)]
print("oddiy massiv:       ", a)

# massivni bir xil elementlarini olib tashlash
a = list(set(a))
print("ixchamlangan massiv:", a)





#                      2-misol.

a = [2,5,3,2,7,5,3,1,8,0]             # berilgan massiv
b = a.copy()                        # qayta ishlov berish uchun a massiv elementlarini koppy qilamiz

max1 = a[0]                 # eng katta son
max2 = a[0]                 # eng katta sondan bir pog'ona kichik son

#  eng katta sonni aniqlaymiz
for i in a:
    if max1 <= i:
        max1 = i
a.remove(max1)               # eng katta sonni chiqarib tashlaymiz.

#    eng katta sondan bir pog'ona sonni topamiz.
for i in a:
    if max2 <= i:
        max2 = i

a.clear()               # a massivni tozlaymiz

# katta sonlarni chiqaramiz.
print("m1=", max1)
print("m2=", max2)

# b massivda elementlarni almashtrish uchun elemnt indexini aniqlaymiz.
index_max1 = b.index(max1)
index_max2 = b.index(max2)
print(index_max1, index_max2)

# natojani ciqaramiz.  indexi kichigini aniqlashadan maqasad: birinchi qaysi kelishini bilish
if index_max1 < index_max2:
    print(b[:index_max1] + b[index_max2 : index_max1-1 : -1] + b[index_max2+1:])
else:
    print(b[:index_max2] + b[index_max1 : index_max2-1 : -1] + b[index_max1+1:])




#                      3-misol.
n = 5
a = [[random.randint(1,10) for i in range(5)] for i in range(6)]
print(a)

for i in range(n):
    for j in range(n):
        print(a)




#                      4-misol.
import random
n = 5
a = [[random.randint(1,9) for i in range(n)] for i in range(n)]
print(a)
print()

S = 0           # yig'indini hisoblashga

print("maximallari")
for i in range(n):
    max = a[0][0]
    for j in range(n):
        if max <= a[i][j]:
            max = a[i][j]
    print(max, end=" ")
    S += max
print("\n")

# matritsani chiqarib olamiz
for i in range(len(a)):
    print(a[i])

print()
print("Summasi=", S)





#                      5-misol.
n = 5
a = []
for i in range(n):
    b = []
    for j in range(n):
        if i==j:
            b.append(0)
        else:
            b.append(i-j)
    a.append(b)
print(a)
print()

for i in range(n):
    print(*a[i])

