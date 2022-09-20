# replace()
# upper() ; lower() ; title()
# strip() ; rstrip() ; lstrip()
# split() ; rsplit() ; lsplit()
# join()
# capitalize()
# count()
# startswith() ; endswith()
# index() ; rindex() --> izlash (xatolik qaytaradi) ; orqadan qidirib boshlaydi
# find() ; rfind() --> izalsh (xatolik qaytarmaydi) ; orqadan izlash
#
# isdigit() , isdecimal(), isalnum() , isnumeric() , isalpha() , isascii()
# isidentifier() , isprintable() , isspace() , istitle(),isupper(),islower()


#       1-misol.                    10 lik sistemadan 16 likka utqazish va teskari yozish
s = input("s= ")
S = ""
while s != "0":
    if int(s) % 16 < 10:
        S = str(int(s) % 16) + S
    else:
        S = str(chr(55 + int(s) % 16 )) + S
    s = str(int(s) // 16)
print(S)


#       2-misol.                    10 lik sistemadan 16 likka utqazish va teskari yozish
s = input("s= ")
S = ""
for i in rnage(len(s)):
    if s[i].isdecimal():
        S += int(s[i]) * 16**(len(s)-i-1)
    else:
        S += (ord(s[i])-55) * 16**(len(s)-i-1)
print(S)
print(int(s, 16))                      # int(value, base=10)          # boshq usulda.

#       3-misol.                            probeller 2tadan kop bulsa, birinchi matnni chiqaradi
s = input("s = ")
s = s.split(" ")            # probel bulsa massivga alohida elelement qilib joylaydi
if len(s) == 2:
    print(" ".join(s))      # s dagi massiv elementlarini birlashtirib yuboradi
elif len(s) > 2:
    print(s[1])


#       4-misol.                    matn boshi va usha harf yana kelsa boshqa belgiga uzgartirish
s = input("s= ")
s = s.split()
for i in range(len(s)):
    k = s[i][-1]
    s[i] = str(s[i].replace(k, '.', s[i].count(k) - 1))
print(*s)



#       5-misol.                            Fayl nomini aniqlash
s = "D:\\papka\\kerakli_papka\\fayl.1.exe"
s = s.split()
x = s[-1].rsplit(".", 1)                # nuqtani orqa tomondan 1 marta chiqquncha tekshiradi
print(x)
print(x[0])


#       6-misol.                        qavslar turlarinni tekshirish ochiq va yopiluvchilarini
s = input("s= ")
k = 1
if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
    k = 0
    print(-1)
a = ['(', '[', '{'];    b = [')', ']', '}']
if k:
    m = sum(s.count(j) for j in a)
    q = 0
    bosh = -1;   oxir = len(s)
    for i in s:
        if i in a:
            if i == a[0]:       w = 0
            elif i == a[1]:     w = 1
            else:               w = 2

            q += 1
            bosh = s[bosh+1].find(a[w]) + bosh + 1
            oxir = s[:oxir].rfind(b[w])
        if bosh > oxir:
            print(bosh, len(s)-1 -s[::-1].rfind(b[w]))
            k = 0
            break
        if q == m:
            break
if k:
    print(0)


#       65-misol.                                      kodirofka
s = intput("s= ")
k = int(input("k= "))

i = 0
while i < len(s):
    if s[i].isaloha() and (s[i].islower() and ord(s[i]) + k <= 122) or (s[i].isupper() and ord(s[i]) + k <= 90):
        s = s[:i] + chr(k + ord(s[i])) + s[i+1:]
    elif s[i].islower() and ord(s[i]) + k > 122:
        s = s[:i] + chr(k + ord(s[i]) - 26) + s[i + 1:]
    elif s[i].isupper() and ord(s[i]) + k > 90:
        s = s[:i] + chr(k + ord(s[i]) - 26) + s[i + 1:]
    i += 1
print(s)

#       66-misol.                                       rekodirofka
s = input("s = ")
k = input("k = ")
i = 0

while i < len(son):
    if s[i].isaloha() and (s[i].islower() and ord(s[i]) - k >= 97) or (s[i].isupper() and ord(s[i]) - k >= 65):
        s = s[:i] + chr(ord(s[i]) - k) + s[i + 1:]
    elif s[i].islower() and ord(s[i]) - k < 97:
        s = s[:i] + chr(ord(s[i]) - k + 26) + s[i + 1:]
    elif s[i].isupper() and ord(s[i]) - k < 65:
        s = s[:i] + chr(ord(s[i]) - k + 26) + s[i + 1:]
    i += 1
print(s)


#       -misol.

#       -misol.

#       -misol.


