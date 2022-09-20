import re                               # regular expression - matndan belgi izlash
#[] - belgilar to'plami. ichida xoxlagan belgi bo'lishi mumkin
#{} - aniq belgi ya'ni ichida bir nechta belgi bo'lishi
#() - Gruppa
# ^ - startwith. boshlanish qaysidir belgi bilan.  [^] --> ichida kelsa berilgan bn boshlanmasligi kerakligini bildiradi
# $ - endwith. oxiri qaysidir belgi bilan
# + - bitta yoki shundan bir nechta bo'lishi kerak
# * - 0 ta yoki undan ko'p
# ? - 0 ta yoki 1 ta
# \ - Exception. istisno re moduli o'qimaydi
# | - Or
# & - And
# . - xoxlagan belgi

# ?: - guruhni guruhga tegishli emasligini bildiradi.
#


#                                     bazi qushimcha belgialar
# \A - startwith = ^
# \B - bunda matnda berilgan suz bn boshlanmasligi kerak
# \b - binary bulib, bunda berilgan suz matn orasida bo'lsa ham space bn ajratilganini topadi.  r'matn' bo'lish kerak
# \D - raqamlarni topsa xatolik beradi
# \d - [0-9] raqamlar
# \S = [^ \t\n] - \s ni teskarisi
# \s = [' ' \t \n] --> shu belgilarga qullaniladi
# \W - \w ni teskarisi
# \w = [0-9A-Za-z_] - barcha raqam harf va past chiziq _ borligini tekshiradi        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! xatolik chiqarmayabdi
# \Z - endwith = $
# \z -
# \


#                                       f u n k s i y a l a r i
# match() - satr boshidan qidiradi
# search() - satrni hamma joyidan izlaydi
# findall() - kerakli suzni topib massivga javob qaytaradi
# split() - berilgan suzdan ajratib massivga javob qaytaradi, berilgan suz chiqmaydi
# sub() - satrni kerakli kalit so'zga almashtiradi, replace daqa.
# subn() - subn() ga qushimcha bulib bunda nechta so'zni almashtirganini qaytaradi
# finditer() -
# compile() - re modulga kompile qilishni hosil qiladi.
#           -  re.IGNORECASE,  re.VERBOSE,
# groups() -  guruhlarni elementlarini olish
# fullmatch() -  satrni hammasiga tegishli bulsa oladi
# span()[1] - nechinchi tartibdagi guruhni topish
#  -
#  -
#  -
#  -
#  -
#  -
#  -
#  -
#  -

#                                                            emailni tekshirish
#x = "youtube@gmail.com"
#y = re.search("^[A-Za-z0-9]+[@][a-zA-Z]+[\.][A-Za-z]{2,3}$", x)
#if y:                  print("ha")
#else:                  print("yo'q")



#                                                       telefon raqam boshidagi plus belgisini tekshirish
#x = '+998354354'
#y = re.match('\+', x)       # re.match('\+[0-9]{12}', x)

#x = '+998(65) 351-65-35'
#y = re.match('\+998\([0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2}$', x)            # $ belgi quyilmasa nomer orqasidan raqam qushib quysak < +998(65) 351-65-3535> xato bermaydi



#                                           matn orasidan suz izlash,    \b - funksiya
#x = 'qalesiz salom bulsin sizg'
#y = re.search(r'\bsalom', x)                # r"matn yozamiz"  -->  r harfni quyish kerak



#                                           space aniqlash
#x = 'yaxshi\tyuribsizmi'
#y = re.search("\s", x)



#                                           alnum() - funksiyaga teng \w
#x = '0_kk'
#y = re.findall("\W", x)



#                                         split() - funksiyasi orqali matnni alohida suz ko'rinishiga keltirish
#x = 'bahbcjh5wecw5wvwv645vwvwvw'
#y = re.split("\d", x)    # yoki ("[0-9]")
#print(re.split("\d", x))



#                                      matnni re modulga o'tqazish - sub() modul
#matn = "+99hsb sjhbjhd e5veve 3v4 vev6648rvr vee99"
#uzgar = 'Q'                                             # mantdagi kerakli kalit suzlarni shu so'z ('Q') ga uzgartiradi
#print(re.sub(r'\d', uzgar, matn, 2))                    # kalit suz = '\d' --> yani raqamlarni oladi.  + belgi bulsa ketma ket kelgan raqamlarni 1 ta qilib oladi, agar bo'lmasa har bir raqamni 1 ta qilib oladi
                                                         # 2 raqami matndan faqat 2 tasini almashtirib beradi
#print(re.sub(r'\d\b', uzgar, matn))                     # \b bilan matn ichidagi har bir so'zni tekshirib olamiz


#                                   c o m p i l e  --  funksiyasi
#x = re.compile(r"https?://www.[A-z0-9_+.-]*.?[A-z]+/?")
#print(x)
#if x.match(input("A=" )):
#    print(True, x)
#else:
#    print(False, x)


##                                   re.IGNORECASE  -- funksiyasi
#x = re.compile(r"[a-z]", re.IGNORECASE)                     # o'xshash belgilarni oladi
#print(x)
#if x.match(input("A= ")):
#    print(True, x)
#else:
#    print(False, x)

##                                   re.VERBOSE  -- funksiyasi
#x = re.compile(r"""https?://           # bu SSl bormi yuqmi
#                www.                   # www. nomini tekshirish
#                [A-z0-9_+.-]*.?        # web sayt nomi
#                [\w]+/                 # domain nomi
#""", re.VERBOSE)                                            # qatorma qator yozganimizni birlashtirib beradi
#print(x)
#if x.match(input("A= ")):
#    print(True)
#else:
#    print(False)


##                                  finditer()  --  malumotlarni guruhlanganiga qarab bulib bulib chiqarib beradi
#url = input("Url: ")
#tekshir = re.compile(r"(https?://www).(\w+).([\w]+)(/watch\?)")
#print("Tekshir:", tekshir)

#m = tekshir.finditer(url)                       # guruhlarni alogida qilib belgilab beradi. va ajratib olinadi
#print("m:", m, '\n')
#
#for mi in m:
#    print(mi[0])                    # to'liq chiqaradi
#    print(mi[1])                    # 1-gruppa
#    print(mi[2])                    # 2-gruppa
#    print(mi[3])
#    print(mi[4])


#                                        Guruhga tegishli emas qilib chiqarish
#a = r"((?:19|20)\d\d"               # ?: katta guruhga tegishli emasligini belgilab beradi
#x = re.compile(a)                   # a satrni reguler expression ga o'girib beradi
#x.match(input("a= ")).groups()      # kiritilgan matnni tekshirib keyin guruhlab chiqaradi


#                               formatlash orqli re modulini ishlatish
#a = r"(?:%s)%|".join('%s' %x for x in (oy_30,oy31))






















#                                       M I S O L L A R
#a = '01-06-2022'             # 01-06-2022 yoki 1-6-2022     sanalarni aniqlash
#b = re.match("(\d{2}|[0-9]?)(-|/|:)(\d{1,2})(-|/|:)\d{4}$", a)


#                                       email tekshirish
#a = 'https://YouTube.com/watch?v=kncnwLKNkjn'
#b = re.match("https?://[A-z0-9_+.-]*.?[A-z]+/?", a)


#                                      parolni qiyinligini tekshirish
#a = input("kalit: ")                #   parolga misol.  bvKv58vn%vbdj#ve31
#b = str(re.findall(r"[A-z0-9#@!<>&^$%*]+", a))
#
#print(len(b), b)
#if 23 > len(b) > 6 and ('#'or'@'or'!'or'<'or'>'or'&'or'^'or'$'or'%'or'*') in b:
#    print("O'rtacha parol:", b)
#elif len(b) > 8 and ('#'or'@'or'!'or'<'or'>'or'&'or'^'or'$'or'%'or'*') in b:
#    print("Murakkab parol:", b)
#else:
#    print("bu oddiy parol.")


#                                   Ism Familya chiqarish
#def Ism(ism = input("Ism: ")):
#    if re.match("[A-Z]?[a-z]+$", ism):
#        return "Natija:", ism
#    else:
#        print("Ism to'gri yozilganiga etibor bering.")
#        return Ism(ism=input("Ism: "))
#
#
#def Familiya(familiya = input("Familiya: ")):
#    if re.match("[A-Z]?[a-z]+$", familiya):
#        return "Natija:", familiya
#    else:
#        print("Ism to'gri yozilganiga etibor bering.")
#        return Familiya(familiya=input("Ism: "))
#
#print(Ism())
#print(Familiya())




#                                      K kun keyingi Sanani  aniqlash
#def IsLeapYear(yil):
#    x = True
#    if yil%100 != 0 and yil%4 == 0:
#        return x
#    elif yil%100 == 0 and yil%400 == 0:
#        return x
#    else:
#        return False
#
#def IsMonth(oy):
#    if oy == 2:                             # 28 kunlik oylar
#        return 28 + IsLeapYear(yil)
#    elif oy in [4,6,9,11]:                    # 30 kunlik oylar
#        return 30
#    elif oy in [1,3,5,7,8,10,12]:                    # 31 kunlik oylar
#        return 31
#    else:
#        print("oylar soni 12 ta", oy)
#        return IsMonth(oy=int(input("Oy: ")))
#
#def NextDate(kun, oy, yil, K):
#    kun += K
#    print("Ismonth:", kun, (oy), yil)
#    while kun > IsMonth(oy):
#        kun -= IsMonth(oy)
#        oy += 1
#        if oy > 12:
#            oy = 1
#            yil += 1
#    return kun, oy, yil
#
#kun, oy, yil = map(int, input("kun, oy, yil: ").split())
#K = int(input("K= "))
#print(NextDate(kun, oy, yil, K))


#                                       k kun oldingi kunni topish
#def IsLeapYear(yil):
#    x = True
#    if yil%100 != 0 and yil%4 == 0:
#        return x
#    elif yil%100 == 0 and yil%400 == 0:
#        return x
#    else:
#        return False
#
#def IsMonth(oy, yil):
#    if oy == 3:                             # 28 kunlik oylar
#        return 28 + IsLeapYear(yil)
#    elif oy in [5,7,10,12]:                    # 30 kunlik oylar
#        return 30
#    elif oy in [1,2,4,6,8,9,11,0]:                    # 31 kunlik oylar
#        return 31
#    else:
#        print("oylar soni 12 ta", oy)
#        return IsMonth(oy=int(input("Oy: ")), yil=yil)
#
#def NextDate(kun, oy, yil, K):
#    kun -= K
#    while kun <= 0:
#        kun += IsMonth(oy, yil)
#        oy -= 1
#        if oy == 0:
#            oy = 12
#            yil -= 1
#    return kun, oy, yil
#
#kun, oy, yil = map(int, input("kun, oy, yil: ").split())
#K = int(input("K= "))
#
#print(NextDate(kun, oy, yil, K))





#                           Sanani guruhlab regular expressionda formatlar orqali tekshirish
#yil = r"((?:19|20)\d\d)"
#matches = r"(%%s)-(%%s)-%s" %yil        # %%s  matchesdan kiritgan o'zgaruvchimiz keladi, (kun30 yoki kun31 - oy)
#kun30 = matches %("04|06|09|11", "0?[1-9]|[12]\d|30")
#kun31 = matches %("01|03|05|07|08|10|12", "0?[1-9]|[12]\d|3[01]")
#leap = "(?:%s)" % '|'.join('02d' % i for i in range(4,100,4))
#fevral = r"(02)-(%%|%s)-(%s)" %(r'((?:0?[1-9]|1\d|2[0-8])-%s' %yil,
#         r"(?:(29)-(?:(?:19|20)%s|2000))" %leap)
#
#natija = '|'.join('(?:%s)' %i for i in (kun30, kun31, fevral))
#x= re.compile(natija)
#x.match(input("a= "))





#                           M A S A L A L A R
#            a_b  wkj_lwcn  borlarini chiqarish
#x = r"[a-z]+_[a-z]+"
#x = re.compile(x)
#for i in x.findall(input("a= ")):
#    i = i.split('_')
#    print(i[0], i[1])


#               so'z boshi va oxirida z harfi ishlatilmasin lekin orasida 1 ta ishlatilasin
#x = "^[^z][a-z]*z[a-z]*[^z]$"       # yoki  "^[^z].+z.+[^z]$"
#x = re.compile(x)
#y = x.search("swjezjcbk")           #  $ belgidan foydalanmasak  x.fullmatch()  funksiya tuliq matnni uzini tekshiradi
#print(y)


#                     18-misol        matndan 1 dan 3 gacha sonlarni chiqarib berish
#x = "[1-3]*"                # yoki  "\d{1,3}"
#x = re.compile(x)
#y = x.findall("Hbhjhfw  12 425 njd1j 352bhj")
#print(y)


#                     19-misol.        matndan kerakli suzni izlash
#izlanadigan_suz = "fox|dog|horse"
#ugirish = re.compile(izlanadigan_suz)
#for i in ugirish.findall(input("matn: ")):
#    i.split(" ")
#    print(i)


#                     22-misol.          bush joylarni _ belgi bn almashtirish
#a = input("matn: ")
#x = re.sub(r" +", r"_", a)


#                     24-misol.          urldan sanani olish
#url = input("Url: ")
#if re.match(r"https://w{3}\.[A-z0-9]+\.[A-z]{2, }", url):
#    print(re.findall("/(\d{4})/(\d{2})/(\d{2})", url))



#                      27-misol.            satrdan raqamlarni chiqarib olish
#matn = "vs1f6vv1r6ea1516arjb3378fbsh"
#for i in re.findall(r"\d+", matn):              # 1-usul
#    print(i, end=' ')
#print('\n')
#for i in re.split(r"\D+", matn):                # 2-usul
#    print(i, end=' ')



#                       33-misol.              matndan 5 ta suzliklarni topish
#matn = "qale ishlar alomi bugunga vaqti bormi kitob uqishga"
#for i in re.findall(r"\b\w{5}\b", matn):
#    print(i, end=' ')



#                       41-misol.                  A-z0-9 dan tashqari hamma belgini o'chirib tashlash
#matn = "qale ishlar alomi bugunga vaqti bormi kitob uqishga"
#print(re.sub(r"[\W]+", ' ', matn))                 #  \W == [^A-z0-9_]


#                        46-misol.                Adverb (oxiri ly bilan tugaydigan suz) suzlarni topish
#print(re.findall(r"\w+ly", matn))


#                        47-misol.                : ; * + \n  suzlar buyicha split qilish
#print(re.split(r";|,|:|\+|\*|\n", matn))


#                        50-misol.                 urldan domen nomini topish
#print(re.split(r"\.", matn)[0])
#print(re.split(r"\b\W+", matn))
#print(re.split(r"\.[\w]+", matn))








