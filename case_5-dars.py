#  1-misol.
kun = 5 #int(input("kunni kiriting haftani kunini chiqarib beraman:"))
if   kun == 1:         print("Dushanba")
elif kun == 2:         print("Seshanba")
elif kun == 3:         print("Yakshanba")
elif kun == 4:         print("Payshanba")
elif kun == 5:         print("Juma")
elif kun == 6:         print("Shanba")
elif kun == 7:         print("Yakshanba")
else:                   print("Boshqa kun kiritdingiz.")

#  3-misol.
oy = 9 #int(input("Oy raqamini kiriting:"))
if  2 < oy < 6:           print("Bahor")
elif 5 < oy < 9:          print("Yoz")
elif 8 < oy < 12:         print("Kuz")
else:                     print("Qish")

#  4-misol.
#oy = int(input("Oy raqamini kiriting:)
if oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10 or oy==12:
    print("31 kunlik")
elif oy==4 or oy==6 or oy==9 or oy==11:
    print("30 kunlik")
elif oy == 2:                                   print("28 kunlik")
else:                                           print("bunday oy yo'q")

#  9-misol.
kun, oy =30, 12 # int(input("Kunni kiriting:")), int(input("Oyni kiriting:"))
kun += 1
if (oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10 or oy==12):
    if kun == 32:
        kun, oy = 1, oy + 1
        if oy == 13:
            oy = 1
if kun == 30 or (oy==4 or oy==6 or oy==9 or oy==11):
        kun, oy = 1, oy + 1
elif kun == 29 and oy==2:
    kun, oy = 1, oy + 1
print(kun, "-", oy)

#  10-misol.            Robot
#y = input("robot yo'nalishi (Janub-Shimol-Sharq-G'arb) >:")
#k = int(input("Komanda (0-oldings, 1-chapga, 2-o'ngnga) >:"))
###########################################################               ????????????????????????????????


#  11-misol.
#################                                                      /????????????????????????????????

#  15-misol.                        K a r t a
M = 3 #int(input("1-g'ish, 2-olma, 3-chillak, 4-qarg'a.  >>> Birini tanlang:"))
N = 8 #int(input("6<=karta<=10, 11-valet, 12-dama, 13-qirol, 14-tuz.  >>> Birini tanlang:"))
if 6 <= N <= 14:
    if N == 11:     print("Valet", end=" ")
    elif N == 12:     print("Dama", end=" ")
    elif N == 13:     print("Qirol", end=" ")
    elif N == 14:     print("Tuz", end=" ")
    else:             print(N, end=" ")
if 1<= M <=4:
    if M == 1:          print("G'isht")
    if M == 2:          print("Olma")
    if M == 3:          print("Chillak")
    if M == 4:          print("Qarg'a")
else:                   print("bunday karta yuq")


#  18-misol.         Sonni so'z ko'rinishiga keltiruvchi dastur
son = 555   #int(input(">> 10000 dan kichik Son kiriting.\n> So'z qilib beraman:"))

if son // 1000 != 0:                              # mingliklar
    if son // 1000 == 1:
        print("Bir ming", end=" ")
    elif son // 1000 == 2:
        print("Ikk ming", end=" ")
    elif son // 1000 == 3:
        print("Uch ming", end=" ")
    elif son // 1000 == 4:
        print("To'rt ming", end=" ")
    elif son // 1000 == 5:
        print("Besh ming", end=" ")
    elif son // 1000 == 6:
        print("Olti ming", end=" ")
    elif son // 1000 == 7:
        print("Yetti ming", end=" ")
    elif son // 1000 == 8:
        print("Sakkiz ming", end=" ")
    elif son // 1000 == 9:
        print("To'qqiz ming", end=" ")

if son // 100 != 0:                           # yuzliklar
    if (son%1000//100) == 1:
        print("Bir yuz", end=" ")
    elif (son%1000//100) == 2:
        print("Ikk yuz", end=" ")
    elif (son%1000//100) == 3:
        print("Uch yuz", end=" ")
    elif (son%1000//100) == 4:
        print("To'rt yuz", end=" ")
    elif (son%1000//100) == 5:
        print("Besh yuz", end=" ")
    elif (son%1000//100) == 6:
        print("Olti yuz", end=" ")
    elif (son%1000//100) == 7:
        print("Yetti yuz", end=" ")
    elif (son%1000//100) == 8:
        print("Sakkiz yuz", end=" ")
    elif (son%1000//100) == 9:
        print("To'qqiz yuz", end=" ")

if son // 10 != 0:                           # onliklar
    if (son//10%10) == 1:
        print("O'n", end=" ")
    elif (son//10%10) == 2:
        print("Yigirma", end=" ")
    elif (son//10%10) == 3:
        print("O'ttiz", end=" ")
    elif (son//10%10) == 4:
        print("Qirq", end=" ")
    elif (son//10%10) == 5:
        print("Ellik", end=" ")
    elif (son//10%10) == 6:
        print("Oltmish", end=" ")
    elif (son//10%10) == 7:
        print("Yetmish", end=" ")
    elif (son//10%10) == 8:
        print("Sakson", end=" ")
    elif (son//10%10) == 9:
        print("To'qson", end=" ")

if (son % 10) != 0:                           # birliklar
    if (son % 10) == 1:
        print("Bir")
    elif (son % 10) == 2:
        print("Ikk")
    elif (son % 10) == 3:
        print("Uch")
    elif (son % 10) == 4:
        print("To'rt")
    elif (son % 10) == 5:
        print("Besh")
    elif (son % 10) == 6:
        print("Olti")
    elif (son % 10) == 7:
        print("Yetti")
    elif (son % 10) == 8:
        print("Sakkiz")
    elif (son % 10) == 9:
        print("To'qqiz")

elif son == 0:
    print("nol")

#  19-misol.                        M u ch a l ni  aniqlash
yil = 2008  # int(intput("Yilni kiriting:"))
print((yil-1984)//12, "--" ,(yil-1984)%12)
if ((yil-1984)//12) == 0:           print("Yashil", end=" ")
elif ((yil-1984)//12) == 1:           print("Qizil", end=" ")
elif ((yil-1984)//12) == 2:           print("Sariq", end=" ")
elif ((yil-1984)//12) == 3:           print("Oq", end=" ")
elif ((yil-1984)//12) == 4:           print("Qora", end=" ")

if ((yil-1984)%12) == 0:              print("Sichqon")
elif ((yil-1984)%12) == 1:            print("Sigir")
elif ((yil-1984)%12) == 2:            print("Yo'lbars")
elif ((yil-1984)%12) == 3:            print("Quyon")
elif ((yil-1984)%12) == 4:            print("Ajdar")
elif ((yil-1984)%12) == 5:            print("Ilon")
elif ((yil-1984)%12) == 6:            print("Ot")
elif ((yil-1984)%12) == 7:            print("Qo'y")
elif ((yil-1984)%12) == 8:            print("Maymun")
elif ((yil-1984)%12) == 9:            print("Tovuq")
elif ((yil-1984)%12) == 10:            print("It")
elif ((yil-1984)%12) == 11:            print("To'ng'iz")

#  20-misol.                    B u r j ni  aniqlash



