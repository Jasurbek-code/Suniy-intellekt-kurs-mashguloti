#                       1-misol.



#                       2-misol.



#                       3-misol.
file = input("File nomi: ")

while open(file + ".txt", 'w') == True:
    file = input("File nomini boshqattan kiriting: ")
else:
    with open(file + '.txt', 'w') as f:
        f.write("O'zbekiston 4 Iqlimli Mamlakat.")

f = open(file + '.txt', 'r+')
matn = ""
for i in f.read():
    if i.isupper() == True:
        pass
    else:
        matn += i
f.close()
f = open(file + '.txt', 'w+')
f.write(matn)
f.close()


#                       4-misol.



#                       5-misol.

