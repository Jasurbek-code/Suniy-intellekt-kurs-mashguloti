# kofe tayyorlab beradigan avtomatik qurilma

ombordagi_maxsulotlar = {           # maxsulot : millilitr va gram da ===>  maxsulotlar zaxirasi
    "suv"    : 25000,       # 20 litr = 20 000 millilitr
    "shakar" : 1000,        # 1 kg   = 10 000 gram
    "sut"    : 5000,        # 5 litr  = 5 000 millilitr
    "cofe"   : 3000,        # 3 kg    = 3 000 gram
    "kakao"  : 1000}         # 1 kg    = 1 000 gram


masalliq_narxi = {             # masalliqlar : 1 kg narxi, sut va suv litrda narxi
    "suv"    : 2000,
    "shakar" : 15000,
    "sut"    : 9000,
    "cofe"   : 450000,
    "kakao"  : 1000}

kofe = {
    "1" :{"Americano"  : {"suv"    : 210,
                          "shakar" : 15,
                          "sut"    : 40,
                          "cofe"   : 7,
                          "kakao"  : 5}},
    "2" :{"Cappuccino" : {"suv"    : 200,
                          "shakar" : 18,
                          "sut"    : 50,
                          "cofe"   : 8,
                          "kakao"  : 7}},
    "3" :{"Latte"      : {"suv"    : 220,
                          "shakar" : 10,
                          "sut"    : 30,
                          "cofe"   : 8,
                          "kakao"  : 5}},
    "4" :{"Espresso"   : {"suv"    : 250,
                          "shakar" : 15,
                          "sut"    : 0,
                          "cofe"   : 10,
                          "kakao"  : 2}},
    "5" :{"MacCoffe"   : {"suv"    : 260,
                          "shakar" : 12,
                          "sut"    : 10,
                          "cofe"   : 8,
                          "kakao"  : 12}},
}

def Tulov(Summa):
    print("  $ Summangiz: ", ((Summa//1000 + 1)*1000))
    pul = int(input("Tulov qilishingiz mumkin: "))
    if pul >= Summa:
        print("\n  __________________________________\n",
              "|   Maxsulotni olishingiz mumkin.  |\n",
              " --  --  --  --  --  --  --  --  --\n",
              "|       Qoldiq =", pul%1000, "     \t\t\t|\n",
              " ----------------------------------\n",
              " --  --  --  --  --  --  --  --  --\n",
              "|       Qaytim =", pul//1000*1000 - ((Summa//1000 + 1)*1000), "     \t\t|\n",
              " ----------------------------------\n")
    else:
        print("Yetarli mablag' kiritmadingiz hali,")
        Tulov(Summa)


def Qayta_maxsulot_tanlash(davom_etish):
    if davom_etish == "0":
        print("Sizga xizmat ko'rsatishdan mamnunmiz.")
        return quit()
    elif davom_etish == "1":
        Asosiy()                                                                    #ffffffffffffffffffffffffffffffffffffffffffff
    else:
        davom_etish = input("Kerakli buyruqni tanlang iltimos !!!\n\t\t\t"
                            "1 -> HA\n\t\t\t"
                            "0 -> YO'Q\n\t\t\t"
                            " >>>  Tanlash: ")


def Asosiy():
    zakaz = input("""    1 >  Americano - $
    2 >  Cappuccino - $
    3 >  Latte - $
    4 >  Espresso - $
    5 >  MacCoffe - $
    0 >  Chiqish

         Kofe tanlang: """)

    if zakaz=='1' or zakaz=='2' or zakaz=='3' or zakaz=='4' or zakaz=='5':
        Summa = 0
        nechta = int(input("%s dan necha dona kerak: " %(list(kofe[zakaz].keys())[0])))

        omborda_kam_maxsulotlar = {}

        for i, j in kofe[zakaz][list(kofe[zakaz].keys())[0]].items():
                                                                                                        #print(bool(ombordagi_maxsulotlar), "va", bool(omborda_kam_maxsulotlar), "--", ombordagi_maxsulotlar, omborda_kam_maxsulotlar)
            ombordagi_maxsulotlar[i] -= kofe[zakaz][list(kofe[zakaz].keys())[0]][i] * nechta            # xatolik. bundan pastdagi shartni bajarmaydiganlarini ham hisoblab quyadi
            if ombordagi_maxsulotlar[i] <= 0:
                omborda_kam_maxsulotlar[i] = ombordagi_maxsulotlar[i]
            elif i in masalliq_narxi and not bool(omborda_kam_maxsulotlar):                 # bungacha minus bulmasa hisoblab quyadi
                Summa += masalliq_narxi[i] * kofe[zakaz][list(kofe[zakaz].keys())[0]][i] * nechta / 1000

        if bool(omborda_kam_maxsulotlar):                                               # xatolik. bu shartni bajarmaydiganlarini ombordagi_maxsulotlar[i] da hisob kitob xato
            print("Uzur bizda ", end=" ")
            for i, j in omborda_kam_maxsulotlar.items():
                ombordagi_maxsulotlar[i] += kofe[zakaz][list(kofe[zakaz].keys())[0]][i] * nechta
                        #for check   print("1) ", kofe[zakaz][list(kofe[zakaz].keys())[0]][i] * nechta ,"va", i, j,  '1)')
                print(f"< {i} - {abs(j)} >", end="")
            print(" dan kam.")
                                                                                        #for check  print(ombordagi_maxsulotlar)
            Qayta_maxsulot_tanlash(davom_etish = input("Boshqa maxsulot tanlaysizmi?\n\t\t\t"
                   "1 -> HA\n\t\t\t"
                   "0 -> YO'Q\n\t\t\t"
                   " >>>  Tanlash: "))                                                      #fffffffffffffffffffffffffffffffffffffffffffff

                                                                                                 #for check    print(ombordagi_maxsulotlar)
        Tulov(Summa)                                                                        #fffffffffffffffffffffffffffffffffffffffffffffff

        Qayta_maxsulot_tanlash(davom_etish = input("Yana maxsulot tanlaysizmi?\n\t\t\t"     #ffffffffffffffffffffffffffffffffffff
                        "1 -> HA\n\t\t\t"
                        "0 -> YO'Q\n\t\t\t"
                        " >>>  Tanlash: "))

    elif zakaz == "0":
        x = False
        print(" Sizga yoqmaydigan maxsulot borligidan afsusdamiz."
              " Keyingi safar abatta maxsulotimizni ko'paytiramiz")
    else:
        print("Iltimos mavjud buyruq kiriting.")
        Asosiy()                                                                            #ffffffffffffffffffffffffffffffffffff

Asosiy()


