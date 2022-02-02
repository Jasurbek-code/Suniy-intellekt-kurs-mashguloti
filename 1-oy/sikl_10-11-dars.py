#  1-misol.                 # sonlarni 2 ta kattasi
a, b, c = 3,2,4

if a > b > c or b > a > c:      print("a=", a, "b=", b)
elif a > c > b or c > a > b:    print("a=", a, "c=", c)
elif b > c > a or c > b > a:    print("b=", b, "c=", c)
else:                           print("teng son kiritmang.")
print()

#  2-misol.                 kodli kalkulyator

takror = True
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



