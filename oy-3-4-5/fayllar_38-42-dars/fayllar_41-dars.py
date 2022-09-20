#  'r' - o'qish
#  'a' - append orqasidan qushish
#  'w' - write
#  'x' - yangi new fayl yaratamiz
#> "t"  - text fayl
#> "b"  - binary fayl

# .read(5)          # boshidan 5 ta harf uqiydi
# .readline(6)      # qatorni uqish
# .readlines()      # qatorlarni uqish, har bir qatorni massiv elementi sifatida belgilaydi
# .write(str)       # faylga matn yozish
# .close()          # faylni yopish

file = open("files.txt", 'r')        # ("C:\\Users\\files.txt") or (r"C:\Users\files.txt")




#       1-misol.
N = 5;  K = 3
file = open("files.txt", 'w')

for i in range(N):
    file.write("*"*K + "\n")
file.close()


#       2-misol.
N = 18;  K = 97    # 97 ASCii da "a" harfiga teng

file = open("files.txt", 'w')
file.write(chr(K))

for i in range(1, N+1):
    file = open("files.txt", 'r+')

    l = file.readlines()
    #print(l[-1])                          # har bir qatorni natijasini chiqaramiz

    file.write("\n" + l[-1] + chr(K + i))
    file.close()


#       3-misol.
N = 6;  K = 97    # 97 ASCii da "a" harfiga teng

file = open("files.txt", 'w')
file.write(chr(K))

for i in range(1, N):
    file = open("files.txt", 'r+')

    l = file.readlines()

    file.write("*"*(N-i) + "\n" + l[-1] + chr(K + i))
    file.close()


#       4-misol.                            satrlar va belgilar sonini chiqarish
file = open("files.txt", 'r')
# print("1-usul: ", len(file.read().strip("\n")))

s = 0;  j = 0
for i in file:
    s += 1
    j += len(i)
print("s=", s)
print("j=", j)

file.close()


#       6-misol.                                2 ta file ni bitta filega utqazish
file1 = open("file1.txt", 'w')
file2 = open("file2.txt", 'w')

file1.write("Birinchi file\n")
file2.write("Ikkinchi files\n")

file1.close()
file2.close()


file1 = open("file1.txt", 'a')
file2 = open("file2.txt", 'r+')

file1.write(file2.read())

file1.close()
file2.close()


#       7-misol.                            Satrni fayl boshiga qushish
S = "salom"

with open("files.txt") as file:
    a = file.read()

with open("files.txt", 'w') as f:
    f.write(S + "\n" + a)


#       8-misol.                        1-fayl boshiga 2-file matnini yozish
with open("file1.txt") as file:
    a = file.read()

with open("file1.txt", 'w') as f1, open("file2.txt", 'r') as f2:
    f1.write(f2.read() + "\n" + a)


#       9-misol.                            k-satr boshiga bush joy tashlash
k = int(input("index: "))

with open("files.txt") as file:
    a = file.read()
a = a.split("\n")

if k < len(a):
    a[k] = " " + a[k]

with open("files.txt", 'w') as f:
    f.write("\n".join(a))


#       11-misol.                               bush satrlar ikkilantirilsin
with open("files.txt") as file:
    a = file.read()
a = a.split("\n")
print(a)

i = 0
while i < len(a):
    if "" == a[i]:
        a.insert(i+1, "")
        i += 1
    i += 1
print(a)

with open("files.txt", 'w') as f:
    f.write("\n".join(a))


#       12-misol.
s = input("satr: ")
with open("files.txt") as file:
    a = file.read()
a = a.split("\n")
print(a)

i = 0
while i < len(a):
    if a[i] == "":
        a[i] += s
    i += 1

with open("files.txt", 'w') as f:
    f.write("\n".join(a))


#       15-misol.                               satr raqamiga qarab uchirish
k = int(input("index: "))
with open("files.txt") as file:
    a = file.read()
a = a.split("\n")
if k < len(a):
    a.pop(k-1)
with open("files.txt", 'w') as f:
    f.write("\n".join(a))


#       16-misol.                               fayldan bush joylarni olib tashlash
with open("files.txt") as file:
    a = file.read()
a = a.split("\n")
print(a)

i = 0
while i < len(a):
    a[i] = " ".join(a[i].split())
    i += 1

with open("files.txt", 'w') as f:
    f.write("\n".join(a))


#       17-misol.                                           ???????????????????????????????????????????
with open("file1.txt") as f1, open("file2.txt", 'r') as f2:
    a = f1.read()
    b = f2.read()

a = a.split("\n")
b = b.split("\n")
print(a)
print(b)

i = 0
while i < len(a) or i < len(b):
    print(i)

    if len(a) > len(b) and i > len(b):
        pass
    elif len(a) < len(b) and i >= len(a):
        a[i] = b[i:]
        print("i=")
    else:
        a.insert(i + 1, b[i // 2])

    i += 2



#       18-misol.                                   har bir satrdan k ta harf uchirish
with open("files.txt") as f:
    a = f.read()

a = a.split("\n")
print(a)

i = 0; k = 5                # satrdan k ta harf uchadi
while i < len(a):
    a[i] = a[i][k:]
    i += 1

print(a)
with open("files.txt", 'w') as f:
    f.write("\n".join(a))



#       19-misol.                           kichik harf kattaga, katta harf kichikka almashadi
with open("files.txt") as f:
    a = f.read()
a = a.split("\n")
print(a)

i = 0
while i < len(a):
    a[i] = a[i].swapcase()
    i += 1

print(a)


#       20-misol.                                   ortiqcha space ni olib tashlash
with open("files.txt") as f:
    a = f.read()
a = a.split("\n")
print(a)

i = 0
while i < len(a):
    a[i] = " ".join(a[i].split())
    print(a[i])
    i += 1

print(a)

#       21-misol.                               oxirgi 3 ta satrni olib tashlash
with open("files.txt") as f:
    a = f.read()

a = a.split("\n")
a = a[:len(a)-3]                # oxirgi 3 ta qator uchiriladi
print(a)


#       24-misol.
with open("files.txt") as file:
    a = file.read()
a = a.split("\n")

for i in a:

    if i.find("    ") == 0 and i[4] != " ":
        s += 1
print("Tabulyatsiyalar soni: ", s)

#       25-misol.                           # k-satrdan abzasni olib tashlash
s = 0;  k = 3               # k-abzasni uchirish uchun
for i in a:
    if i.find("    ") == 0 and i[4] != " ":
        s += 1
        if s == k:
            i = i.replace("    ", "")
            print("uzgardi: " , i)
print("Tabulyatsiyalar soni: ", s)


#       26-misol.                           # 5 ta space tashlanganni aniqlash
s = 0
for i in a:
    if i.find("    ") == 0:
        s += 1
        if i[4] == " ":
            s -= 1
            print("Qizil satr:", i)
print("Tabulyatsiyalar soni: ", s)


#       28-misol.                           ????????????????????????????


#       29-misol.                           eng uzun so'z
with open("files.txt") as f:
    a = f.read()
a = a.split()
print(a)

uzun = max(a, key=len)
print("uzun so'z: ", uzun)

#       30-misol.                           oxirgi uchragan kalta so'zni chiqarish
with open("files.txt") as f:
    a = f.read()
a = a.split()
print(a)

a.reverse()         # massiv elementlarini teskari qilib olamiz

uzun = min(a, key=len)
print("kalta so'z: ", uzun)

#       31-misol.                   # yangi faylga k ta so'zni ko'chirish
with open("file1.txt") as f1:
    a = f1.read()
a = a.split()
print(a)

k = 6                  # k ta so'zni yangi faylga yozadi
with open("file2.txt", 'w') as f2:
    if k > len(a):
        f2.close()
    else:
        f2.write(" ".join(a[:k]))


#       32-33-misol.                       R yoki r harfi bilan boshlanadiga so'zlarni file2 ga yozish
with open("file1.txt") as f1:
    a = f1.read()
a = a.split()
print(a)

with open('file2.txt', 'w') as f2:
    i = 0
    while i <= len(a)-1:
        if a[i].startswith('r') or a[i].startswith('R'):        # r harfi borligini tekshiradi
            print("===> ", a[i])
            f2.write(a[i] + " ")
        i += 1


#       34-misol.                               # satrni o'ng tomondan tekislash, suz 30 tadan kichik bulsa,
with open("files.txt") as f1:
    a = f1.read()
a = a.split('\n')
print(a)

with open("files.txt", 'w') as f:
    i = 0
    while i <= len(a)-1:
        a[i] = " ".join(a[i].split())               # ortiqcha bush joylarni olib tashlash

        b = str(f"|%{30-len(a[i])}.s%s|\n" %(" ", a[i]))      # oldidan joy tashlash, !!! suz uzun bulsa xato  !!!
        f.write(b)
        i += 1



#       35-misol.                               2 tomondan joy tashlash, matnni markazga siljitish
with open("files.txt") as f1:
    a = f1.read()
a = a.split('\n')
print(a)

with open("files.txt", 'w') as f:
    i = 0
    while i <= len(a)-1:
        a[i] = " ".join(a[i].split())               # ortiqcha bush joylarni olib tashlash
        if len(a[i])%2 == 0:
            b = str(f"|%{(30-len(a[i])) // 2}.s%s%{(30-len(a[i])) // 2}.s|\n" %(" ", a[i], " "))      # ikki tomondan joy tashlash, !!! suz uzun bulsa xato  !!!
        else:
            b = str(f"|%{(31-len(a[i])) // 2}.s%s%{(30-len(a[i])) // 2}.s|\n" %(" ", a[i], " "))      # ikki tomondan joy tashlash. 31 = 30 + 1 --> 1 qushimcha joy tashlash toq matnni yuqotish uchun
        f.write(b)
        i += 1


#       37-39-misol.                                       ??????????????????????????  tushunmadim



#       38-misol.                                       uzimni yulim
k = 25
with open("file1.txt", "r") as f1:
    a = f1.read()
a = a.split("\n")

with open('file2.txt', 'w') as f2:
    for i in range(len(a)):
        a[i] = a[i].split(" ")                  # katta massiv ichidagilarni alohida element qilamiz
        print("a[i] :", a[i])

        chegara = 0                             # elementlarni uzunligini qushib ketaveramiz, agar k dan katta bo'lsa boshqa shart ishlatadi
        for j in a[i]:
            chegara += len(j) + 1
            if chegara <= k:
                f2.write(j + ' ')               # k dan kichiklarini faylga yozib boraveramiz
            else:
                chegara = len(j) + 1
                f2.write('\n' + j + ' ')        # k dan katta bulganda keyingi qatorga matnni davomini tushirib yozib ketaveradi
        f2.write('\n')


#       38-misol.        2-usul
k = 25
with open("file1.txt", "r") as f1:
    a = f1.read()

a = a.split("\n     ")
b = ''

i = 0
while i < len(a):
    a[i] = a[i].replace("\n", ' ')
    S = 0
    for j in range(len(a[i])):
        if a[i][j] == " ":
            t = j
        S += 1
        if S > k:
            a[i] = a[i][:t] + "\n" + a[i][t+1:]
            S = 0
    i += 1

with open("file2.txt", 'w') as f2:
    f2.writelines("\n     ".join(a))



#       40-misol.    1-usul                                 2 ta ustunni o'ng tomonga tekislash
with open("file1.txt") as f1, open("file2.txt") as f2:
    a = f1.read()
    b = f2.read()
a = a.split("\n")
b = b.split("\n")

i = 0
while i < len(a):
    if len(a[i]) < 14 or len(b[i]) < 14:
        a[i] = ' '*(14 - len(a[i])) + a[i]
        b[i] = ' ' * (14 - len(b[i])) + b[i] + chr(124)
    else:
        b[i] += chr(124)
    a[i] = chr(124) + a[i]
    i += 1


#       40-misol.    2-usul. ustoz                                 2 ta ustunni o'ng tomonga tekislash
with open("file1.txt") as f1, open("file2.txt") as f2:
    a = f1.read()
    b = f2.read()
a = "".join(a.split('\n'))
b = "".join(b.split('\n'))

with open("files.txt", 'w') as f:
    i = 13
    while i < len(a) or i < len(b):
        f.write('|' + a[i-13:i] + '|' + '|' + b[i-13:i] + '|\n')
        i += 13



#       42-misol.                       ildiz osti javoblarni jadval kurinishida chiqarish
N = 10
a, b = 5, 18

x = a
with open("files.txt", 'w') as f:
    f.write(' '*4 + 'x' + ' '*5 + ' | ' + ' '*7 + 'y' + ' '*7 + '\n')

    for i in range(N+1):
        y = x**0.5
        if len(str(x)) > 10:
            x = float(str(x)[:10])
        if len(str(y)) > 15:
            y = float(str(y)[:15])

        f.write((10 - len(str(x)))*' ' + str(x) + ' | ' + (15 - len(str(y)))*' ' + str(y) + '\n')
        x += (b-a)/N


#       43-misol.                           x ni sin va cos da qiymatini jadvalini chiqarish
from math import sin, cos
N = 10
a, b = 2, 18

d = a
with open("files.txt", 'w') as f:
    f.write(f"|{' '*3}x{' '*4}|%8.3s{' '*4}|% 8.3s{' '*4}|\n" %('sin', 'cos'))
    for i in range(N+1):
        sinx = sin(i);     cosx = cos(i)

        f.write(f"|%8.4r|%12.10s|%12.10s|\n" %(d, sinx, cosx))                 #(f"% 10r teng x % 10.4s" %(d, d))  > %d - int, %r - float
        d += (b-a)/N



#       46-misol.                           kasr qismida 0 raqami yuqlarni chiqarish
b = []
for i in a:
    i = i.split()
    for j in i:
        print(j[j.find('.')])
        if '0' not in j[j.find('.') + 1:]:
            b.append(j)
with open("files.txt", 'w') as f:
    for i in range(0, len(b), 2):
        f.write(b[i] + ' | ' + b[i+1] + '\n')
    if len(b) % 2:
        f.write(b[-1] + ' | ')


#       49-misol.                    2 ta faylni har bir ustunlarini bitta ustunga joylashtirish
with open("file1.txt") as f1, open("file2.txt") as f2, open("files.txt", 'w') as f:
    m = 10
    for i in range(m):
        a = f1.readline()
        k = f2.readline()

        f.write(a.rstrip('\n') + ' ' + k)



#       55-misol.                           tinish belgilarini topish    optimali
with open("file1.txt") as f1:
    a = f1.read()
b = []
for i in a:
    if not i.isalnum() and i not in b:
        b.append(i)
b.sort()
with open("files.txt", 'w') as f:
    f.write('\n'.join(b))


#       55-misol.                           tinish belgilarini topish
with open('file1.txt') as f:
    a=f.read()
t=[]
for i in a:
    if (ord(i)==33 or ord(i)==34 or ord(i)==39 or 44<=ord(i)<=46 or ord(i)==58 or ord(i)==59 or ord(i)==63 or ord(i)==96) and not(i in t):
        t.append(i)
        for i in range(len(t)):
            for j in range(len(t)-1-i):
                if ord(t[j])>ord(t[j+1]):
                    t[j],t[j+1]=t[j+1],t[j]
with open('files.txt','w') as f:
    for i in t:
        f.write(str(i))
        f.write(' ')



#       58-misol.                              1 ta harflar necha marta ishlatilgani
with open("file1.txt") as f1:
    a = f1.read()
b = [];   c = []
for i in a:
    if i.isalpha() and i not in b and i.islower():
        b.append(i)
        c.append(a.count(i))

for i in range(len(b)):
    for j in range(len(b)):
        if c[i] > c[j]:
            b[i], b[j] = b[j], b[i]
            c[i], c[j] = c[j], c[i]
        if c[i] == c[j]:
            if b[i] > b[j]:
                b[i], b[j] = b[j], b[i]
                c[i], c[j] = c[j], c[i]
with open("files.txt", 'w') as f:
    i = 0
    while i < len(b):
        f.write(b[i] + ' - ' + str(c[i])  + '\n')
        i += 1



#       -misol.

#       -misol.


