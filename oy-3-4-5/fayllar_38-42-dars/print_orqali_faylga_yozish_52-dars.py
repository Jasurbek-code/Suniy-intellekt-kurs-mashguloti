

file_name = 'files.txt' #input("Fayl nomi: ")
def AddIdNumber():          #   1- buyruq
    global file_name
    with open(file_name, 'a') as table:
        Familiya = input("Familiya kiriting: ")
        Ism = input("Ism kiriting: ")
        Yosh = input("Yoshingizni kiriting: ")
        Kurs = input("Kursni kiriting: ")
        Average = input("Ortacha bahosini kiriting: ")
        Tel= input("Telefon raqam kiriting: ")

        print('\n', Familiya, "\t", Ism, "\t", Yosh, "\t", Kurs, "\t", Average, "\t", Tel,
              file=table)                            # file - printni funksiyasi bo'lib natijani ekranga chiqarmasdan, faylga yozib qo'yadi.


def DeleteIdNumber():       #   2- buyruq
    global file_name
    Familiya = input("Familiya kiriting: ")
    with open(file_name, 'r') as table:
        lines = table.readlines()
    with open(file_name, 'w') as table:
        for i in lines:
            if not i.strip('\n').startswith(Familiya):
                table.write(i)


def EditIdNumber():         #   3- buyruq
    global file_name
    Fam = input("Familiya: ")
    with open(file_name, 'r') as table:
        lines = table.readlines()
    with open(file_name, 'w') as table:
        for i in lines:
            if not i.strip('\n').startswith(Fam):
                table.write(i)
            else:
                Familiya = input("Familiya kiriting: ")
                Ism = input("Ism kiriting: ")
                Yosh = input("Yoshingizni kiriting: ")
                Kurs = input("Kursni kiriting: ")
                Average = float(input("Ortacha bahosini kiriting: "))
                Tel = input("Telefon raqam kiriting: ")

                table.write('\n' + Familiya + "\t" + Ism + "\t" + Yosh + "\t" + Kurs + "\t" + str(Average) + "\t" + Tel)

def SearchBySecondName():   #   4- buyruq
    global file_name
    Fam = input("Familiyasi: ")
    with open(file_name, 'r') as table:
        for i in table:
            S = i.split('\t')[0]
            if Fam in S:
                print(i)

def SearchByPhone():        #   5- buyruq
    global file_name
    Tel = input("Telefon raqam: ")
    with open(file_name, 'r') as table:
        for i in table:
            S = i.split('\t')[-1]
            if Tel in S:
                print(i)

def Printing():             #   6- buyruq
    global file_name
    with open(file_name, 'r') as table:
        malumot = table.read()
        print(malumot)



while True:
    print("Buyruqlar: \n1-Id qo'shish, 2-Idni o'chirish, 3-Idni edit qilish, \n4-Familiya qidirish, 5-Telefon qidirish, 6-Ekranga chiqarish, \n0-Exit")
    buyruq = int(input("Buyruq: "))

    if buyruq == 1:
        AddIdNumber()
    if buyruq == 2:
        DeleteIdNumber()
    if buyruq == 3:
        EditIdNumber()
    if buyruq == 4:
        SearchBySecondName()
    if buyruq == 5:
        SearchByPhone()
    if buyruq == 6:
        Printing()
    if buyruq == 0:
        print("Rahmat men ishlashdan to'xtadim.")
        break




