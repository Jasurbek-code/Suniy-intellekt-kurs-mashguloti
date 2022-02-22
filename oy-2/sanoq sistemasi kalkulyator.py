s = int(input("Qaysi sanoq sistemasidan o'tqazishni tanlang: "))
s_o = int(input("Qaysi sanoq sistemasiga o'tqazishni tanlang: "))
son = int(input("Son= "))

yana = True
while yana:
    natija = 0; daraja = 0
    while son > 0:
        had = son%s_o
        natija += had * (s ** daraja)
        daraja += 1
        son //= s_o
    print(natija)


    yana = input("\n>>> Qayta ishga tushirmoqchi bo'lsangiz < ha > ni kiriting: ")
    if yana == "ha":
        yana = True
        s = int(input("Qaysi sanoq sistemasidan o'tqazishni tanlang: "))
        s_o = int(input("Qaysi sanoq sistemasiga o'tqazishni tanlang: "))
        son = int(input("Son= "))
    else:
        yana = False
    #print("Xato kiritildi!")





