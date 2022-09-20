##################++++++++++++++++++++++++#############################
from random import randint
#def matrix(m, n):
#    return [[randint(1,9) for i in range(n)] for j in range(m)]
#def matrix_print(a):
#    for i in a:
#        print(*i)
#    print()
#def SwapCol(a, k1,k2):
#    if k1>len(a[0])-1 or k2>len(a[0])-1:
#        return a
#    else:
#        for i in range(len(a)):
#            a[i][k1], a[i][k2] = a[i][k2], a[i][k1]
#        return a
#m, n = int(input("m= ")), int(input("n= "))
#a = matrix(m, n)
#matrix_print(a)
#k1, k2 = int(input("k1=")), int(input("k2="))
#a = SwapCol(a, k1, k2)
#matrix_print(a)





###################################################
#def Salom(func):
#    def SwapCol(m,n, k1,k2):
#        a = func(m,n)
#        if k1>len(a[0])-1 or k2>len(a[0])-1:
#            return a
#        else:
#            for i in range(len(a)):
#                a[i][k1], a[i][k2] = a[i][k2], a[i][k1]
#            return a
#    return SwapCol
#def matrix(m,n):
#    a = [[randint(1,9) for i in range(n)] for j in range(m)]
#    print(a)
#    return a
#
#matrix2 = Salom(matrix)
#print(matrix2(5,5, 3,1))
#
###       ====================       ##              Tepa bilan past bir xil vazifa bajaradi
#def Salom(func):
#    def SwapCol(m,n, k1,k2):
#        a = func(m,n)
#        if k1>len(a[0])-1 or k2>len(a[0])-1:
#            return a
#        else:
#            for i in range(len(a)):
#                a[i][k1], a[i][k2] = a[i][k2], a[i][k1]
#            return a
#    return SwapCol                                              #Dekoratsiya usulidan foydalanish
#@Salom                                                          #matrix2 = Salom(matrix)    >>>  shunga teng
#def matrix(m,n):
#    a = [[randint(1,9) for i in range(n)] for j in range(m)]
#    print(a)
#    return a
#print(matrix(5,5, 3,1))





##################++++++++++++++++++++++++#############################
#def hi(func):
#    def hello():
#        return func()**2
#    return hello
#def hi1(func):
#    def hello1():
#        return func()**3
#    return hello1
#
#@hi         # 2- ishlaydi
#@hi1        # 1- ishlaydi
#def salom():
#    return 2
#print(salom())




##################++++++++++++++++++++++++#############################
#import re
#def Katta(func):
#    def kattalashtir():
#        return func().upper()                                       # matnni katta qiladi
#    return kattalashtir
#def Uchir(vazifa):
#    def uchirish():
#        return re.sub('[aoiue]', '', vazifa())                      # unli harflarni olib tashlash
#    return uchirish
#@Katta                              # 2-ishlaydi
#@Uchir                              # 1-ishlaydi
#def Chiqar():
#    a = input("matn: ")
#    return a
#print(Chiqar())



##################++++++++++++++++++++++++#############################
#import time
#from math import factorial
#def Timer(func):
#    def timetop(n):
#        a = time.time()
#        func(n)
#        b = time.time()
#        print(func.__name__, "=", b-a)
#    return timetop
#@Timer
#def sin(m):
#    S = 0
#    for i in range(m+1):
#        S += 1/factorial(i)
#    print(S)
#sin(1000)




##################++++++++++++       TUB son   ++++++++++++#############################
#N = 1000 #int(input("N= "))
#def Tub(N):
#    global sana
#    sana = 0
#    for i in range(3, N+1, 2):
#        S = 0
#        for j in range(3, int(pow(N+1, 0.5))+1, 2):
#            sana += 1
#            if i%j == 0:
#                S += 1
#                break
#        if S == 0:
#            print(i, end=" ")
#Tub(1000)
#print(sana)


#############               optimali
#import time
#def Timer(func):
#    def farq(N):
#        a = time.time()
#        func(N)
#        b = time.time()
#        print(func.__name__, b-a)
#    return farq
#
#@Timer
#def Tub(N):
#    global sana
#    sana = 0
#    tubs = [3]
#    for i in range(5, N+1, 2):
#        S = 0
#        for j in tubs:
#            sana += 1
#            if j > int(pow(i, 0.5)):
#                break
#            if i%j == 0:
#                S += 1
#                break
#        if S == 0:
#            tubs.append(i)
#    tubs.insert(0, 2)
#    print(tubs)
#Tub(N)
#print(sana)









#################++++++++++++       CLASS      ++++++++++++#############################
#class Ish:
#    time = 8
#    def __init__(self, turi, manzil, kontakt, boshlanish):
#        self.turi = turi
#        self.manzil = manzil
#        self.kontakt = kontakt
#        self.boshlanish = boshlanish
#        self.tugash = boshlanish + self.time        #self = job ni oladi
#job = Ish("Davlat", "Navoi", "71 315 5315", 9)
#job1 = Ish("Xususiy", "Nukus", "90 166 6156", 10)
#print(job.tugash)
#print(job1.tugash)


#    method orqali chaqirib uzgartirib bolmaydigan uzgaruvchi elon qilish
#class Ish:
#    time = 8
#    def __init__(self, turi, manzil, kontakt, boshlanish):
#        self.turi = turi
#        self.manzil = manzil
#        self.kontakt = kontakt
#        self.boshlanish = boshlanish
#        self.tugash = boshlanish + self.time
#
#    def get_turi(self):
#        return self.turi
#    def get_manzil(self):
#        return self.manzil
#
#     def set_manzil(self, new_manzil):             # manzilni uzgartirish
#         self.manzil = new_manzil
#     def update_boshlanish(self):
#         self.boshlanish += 1
#         self.tugash += 1

#    def get_info(self):
#        return f"{self.turi}: {self.manzil}, {self.kontakt}, Ish vaqti: {self.boshlanish}-{self.tugash}"
#    def __del__(self):                                                                                      # buni yozgan yaxshi. obyekt ishlab bulgandan keyin uzidan uzi uchirib yuboradi
#        return self
#
#
#job = Ish("Davlat", "Navoi", "71 315 5315", 9)
#job1 = Ish("Xususiy", "Nukus", "90 166 6156", 10)
#print(job.tugash)
#print(job1.tugash)
#print(job.get_info())
#print(job1.get_info())
#job.update_boshlanish()        # vaqtni uzgartirish
#job.info()                     # uzgartirilgan malumotni tekshirib olish




#################++++++++++++++++++++++++#############################
##               kasbni olish
#class Dev:
#    laqab = "IT chi"
#    def __init__(self, ism, familiya,tyil, telefon, tili, tajriba, ish_joyi, manzil):
#        self.ism = ism
#        self.familiya = familiya
#        self.tyil = tyil
#        self.telefon = telefon
#        self.tili = tili
#        self.tajriba = tajriba
#        self.ish_joyi = ish_joyi
#        self.manzil = manzil
#
#    def info(self):
#        return f"{self.ism} {self.familiya} {self.tyil}, tel: {self.telefon}, {self.tili} tili \
#{self.tajriba} yil tajriba, {self.ish_joyi}, Manzil: {self.manzil.get_manzil()}"
####  dev1 = Dev("Kamol", "Alimov", 2000, "+998 75 1355345", "Python", 2, "AKT agentligi")           pastda davom ettiramiz
####  print(dev1.info())                                                                             pastda davom ettiramiz
#
#
#class Ish:
#    time = 8
#    def __init__(self, nomi, turi, manzil, kontakt, boshlanish):
#        self.nomi = nomi
#        self.turi = turi
#        self.manzil = manzil
#        self.kontakt = kontakt
#        self.boshlanish = boshlanish
#        self.tugash = boshlanish + self.time
#
#    def get_nomi(self):
#        return self.nomi
#    def get_turi(self):
#        return self.turi
#    def get_manzil(self):
#        return self.manzil
#
#    def set_manzil(self, new_manzil):             # manzilni uzgartirish
#        self.manzil = new_manzil
#    def update_boshlanish(self):
#        self.boshlanish += 1
#        self.tugash += 1
#
#    def get_info(self):
#        return f"{self.turi}: {self.manzil}, {self.kontakt}, Ish vaqti: {self.boshlanish}-{self.tugash}"
#    def __del__(self):                                                                                      # buni yozgan yaxshi. obyekt ishlab bulgandan keyin uzidan uzi uchirib yuboradi
#        return self
#job3 = Ish("Kamera nablyudatel", "Davlat", "Navoi", "71 315 5315", 9)
#
#
#class Manzil:
#    def __init__(self, vil, tuman, kucha, uy):
#        self.vil = vil
#        self.tuman = tuman
#        self.kucha = kucha
#        self.uy = uy
#    def get_vil(self):       return self.vil
#    def get_tuman(self):     return self.tuman
#    def get_kucha(self):     return self.kucha
#    def get_uy(self):        return self.uy
#    def get_manzil(self):
#        return f"{self.vil} viloyati, {self.tuman} shahar, {self.kucha} ko'chasi {self.uy}-uy"
#    def __del__(self):
#        return self
#manzili = Manzil("Qashqadaryo", "Qarshi", "Nasaf", 368)
#
##  tepadagi Dev classga va Ish, Manzil nomli klassdan ma'lumot olib qushish
#dev2 = Dev("Kamol", "Alimov", 2000, "+998 75 1355345", "Python", 2, job3.get_nomi(), manzili)    # job3, manzili uzgaruvchilari olib ichidan malumot olamiz
#print(dev2.info())                                                                 # manzil uzgaruvchini ichki metodlarini Dev classi ichidagi manzil chaqirgandagi uzgaruvchi orqali chaqirildi



##################++++++++++++     Talabalar  ruyxati      ++++++++++++#############################
#class Shaxs:
#    def __init__(self, ism, fam, tyil, ID, manzil):
#        self.ism = ism
#        self.fam = fam
#        self.tyil = tyil
#        self.ID = ID
#        self.manzil = manzil
#    def ism(self):           return self.ism
#    def fam(self):           return self.fam
#    def Id(self):            return self.ID
#    def manzil(self):        return self.manzil
#    def tyil(self):          return self.tyil
#    def info(self):
#        return f"{self.ism} {self.fam} Id: {self.ID}, {self.tyil}-yil, {self.manzil.info_manzil()}"
#    def update_fio(self, fio):
#        self.fam, self.ism = fio.split()                                                # ism va familiyani fio ga split() qilib yuklayabdi
#
#
#class Manzil:
#    def __init__(self, vil, shah, kocha, uy):
#        self.vil = vil
#        self.shah = shah
#        self.kocha = kocha
#        self.uy = uy
#    def vil(self):           return self.vil
#    def shah(self):          return self.shah
#    def kocha(self):         return self.kocha
#    def uy(self):            return self.uy
#    def info_manzil(self):
#        return f"{self.vil} viloyati {self.shah} shahri {self.kocha} {self.uy}-uy"
#    def __del__(self):
#        return self
#manzili = Manzil("Qashqadaryo", "Qarshi", "Nasaf", 368)
#shaxsi = Shaxs("Nurik", "Abdurahimov", 1999, 25456, manzili)
#
#
#class Talaba:
#    def __init__(self, Fio, ID, Universitet, Fakultetit, Kurs):
#        self.Fio = Fio
#        self.Id = ID
#        self.Universitet = Universitet
#        self.Fakultetit = Fakultetit
#        self.Kurs = Kurs
#    def get_Fio(self):                  return f"{self.Fio.ism} {self.Fio.fam()}"
#    def get_Id(self):                   return self.Id
#    def get_Universitet(self):          return self.Universitet
#    def get_Fakultetit(self):           return self.Fakultetit
#    def get_Kurs(self):                 return self.Kurs
#    def info_talaba(self):
#        return f"{get_Fio}, {self.Id} {self.Universitet} {self.Fakultetit} {self.Kurs}"
#
#talaba = Talaba(shaxsi.info(), shaxsi.Id(), "Politex", "mexanika", 2)
#
#print("1) ", shaxsi.info())
#print("2) ", shaxsi.update_fio("Akmalov Jura"))
#print("3) ", shaxsi.info())


##################+++++++++++++          Voris  olish    +++++++++++#############################
#import datetime
#class Shaxs:
#    def __init__(self, ism, fam, tyil, ID):
#        self.ism = ism
#        self.fam = fam
#        self.tyil = tyil
#        self.ID = ID
#    def ism(self):           return self.ism
#    def fam(self):           return self.fam
#    def Id(self):            return self.ID
#    def tyil(self):          return self.tyil
#    def get_fio(self):
#        return f"{self.ism} {self.fam}"
#    def info_shaxs(self):
#        return f"{self.ism} {self.fam} Id: {self.ID}, {self.tyil}-yil"
#    def update_fio(self, fio):
#        self.fam, self.ism = fio.split()                                                # ism va familiyani fio ga split() qilib yuklayabdi
#    def update_ID(self, newID):
#        self.ID = newID
#
#class Talaba(Shaxs):
#    def __init__(self, ism, fam, tyil, ID, talabaID, univer, fakultet):     # Shaxs klassidagi (ism, fam, tyil, ID) ga bemalol muraat qila olamiz
#        super().__init__(ism, fam, tyil, ID)                                # Shaxs klassidan vorish olamiz. Shaxs kalssidagi uzgaruvchilarni super() ga initialisesiga muojaat qilish uchun yuklaymiz
#        self.talabaID = talabaID
#        self.univer = univer
#        self.fakultet = fakultet
#    def get_info(self):
#        return super().get_fio() + f"  {self.talabaID} {self.univer} {self.fakultet} Id:{self.ID}"      # super metodi orqali Shaxs klassidan get_fio() funksiyaga va shaxs ID ga murojaat qilinyapti
#
#class YomonTalaba(Talaba):
#    def __init__(self, ism, fam, tyil, ID, talabaID, univer, fakultet, bahosi):          # faqat bahosi nomli uzgaruvchi oladi yangi. qolganini Vorisdan oaldi
#        super().__init__(ism, fam, tyil, ID, talabaID, univer, fakultet)
#        self.bahosi = bahosi
#    def info(self):
#        return f"{self.get_fio()} ning bahosi: {self.bahosi}"
#
#class TalabaDown(YomonTalaba):                                                          # Yiqilgan talaba bahosini YomonTalabadan voris olamiz
#    def __init__(self, ism, fam, tyil, ID, talabaID, univer, fakultet, bahosi, yiq_yil):
#        super().__init__(ism, fam, tyil, ID, talabaID, univer, fakultet, bahosi)
#        self.yiq_yil = yiq_yil
#        self.tik_yil = ""
#    def update_grade(self, new_grade: int):                                 # kursga utgan talaba       # <<<<<    new: int  (int tipida uzgaruvchi kiritishni suraydi)    >>>>>
#        self.bahosi = new_grade
#        self.tik_yil = datetime.datetime.now().year
#    def tiklangan_yili(self):
#        return self.tik_yil
#
#talaba = TalabaDown("alish", "Valish", 2002, "GF513", 31546, "TATU", "Qmi", 3, 2020)
#print(talaba.update_grade(2))
#print(talaba.tiklangan_yili())










#################+++++++++++      Dekard  klassi - Dunder metodi    +++++++++++++#############################
#####   __eq__ - ==
#####   __le__ - <=
#####   __lt__ - <
#####   __gt__ - >
#####   __ge__ - >=
#####   __mul__ - *
#####   __add__ - +
#####   __sub__ - -
#####   __pow__ - **   x**y
#####   __div__ - /
#####   __floordiv__ - //
#####   __len__ - len()
#####   __call__ - obyektni print qilganda satr
#####   __getitem__ - indexga murojat
#####   __setitem__ - indexni uzgartirish
#####   __

#class Dekard:
#    def __init__(self, a,b):
#        self.x = a
#        self.y = b
#    def __lt__(self, b):                                                # <
#        return self.x < b.x and self.y < b.y
#    def __le__(self, b):                                                # <=
#        return self.x <= b.x and self.y <= b.y
#bir = Dekard(8, 4)          # (3 va 6) va (4 va 8)  tekshiriladi
#ikki = Dekard(8, 8)
#
#print(bir < ikki)
#print(bir <= ikki)


##################++++++++++++     len uzunlikni topish va uzgartirish     ++++++++++++#############################
#class Klub:
#    def __init__(self, nomi):
#        self.nomi = nomi
#        self.__futbolchilar = [1,2,3,4,5,6,7,8,9,0]
#    def __repr__(self):                                     # representation - umumiy ishlatish uchun
#        return f"{self.nomi} futbol komandasi"
#    def __str__(self):                                      # string formatdgi malumotni olish
#        return f"{self.nomi} futbol jamoasi"
#    def __len__(self):
#        return len(self.__futbolchilar)
#    def __getitem__(self, index):
#        return self.__futbolchilar[index]
#    def __setitem__(self, eski, yangi):
#        self.__futbolchilar[eski] = yangi
#    def __call__(self, *args, **kwargs):            #obyektlar uchun
#        return f"{self.nomi} komandasiman"
#
#j = Klub("Chelse")
#
#print(j)
#print(len(j))
#print(str(j))
#print(repr(j))
#print(j.nomi)
#print(j[7])
#
#j[7] = 2
#print(j[7])
#print(j())                  # __call__ metodiga murojaat







##################+++++++++++  class  metodlari     +++++++++++++#############################
###  classmethod -
###  staticmethod -
###  property -
###
###
###
#
#class FIFA:
#    def __init__(self, a):
#        self.a = a
#
#        @classmethod
#        def transfer(cls, a):
#            cls.a = a
#
#a = FIFA("UEFA")
#b = FIFA("AFC")
#print(a.a)
#print(b.a)              # print(FIFA.b)  - ishlamaydi
#print()
#
#a.transfer("AfFc")
#print(FIFA.a)








##################++++++++++++        classmethod       ++++++++++++#############################
#class Sonlar:
#    def __init__(self, a):
#        self.x = a
#
#    @classmethod
#    def uzgar(cls, a):
#        cls.x = a
#    def uzgar1(self, a):
#        self.x = a
#
#bir = Sonlar(4)
#ikki = Sonlar(5)
#print(bir.x)
#print(ikki.x)
##print(Sonlar.x)                # bu ishlamaydi, chunki obyetni uziga murajaat bulgani yuq classmethod orqali
#print()
#
#bir.uzgar(10)
#print(bir.x)
#print(ikki.x)
#print(Sonlar.x)
#print()
#
#bir.uzgar1(200)
#print(bir.x)
#print(ikki.x)
#print(Sonlar.x)
#print()
#
#Sonlar.x = 3000                 # bir.uzgar  --> amal bn bir xil, ikkisi ham class obyektiga murojat
#print(bir.x)
#print(ikki.x)
#print(Sonlar.x)


#######  --------------------------------------------------------------
#class Son:
#    bir_x = 10
#
#    @classmethod
#    def uzgar(cls, a):
#        cls.bir_x = a
#
#
#
#bir = Son()
#ikki = Son
#print(bir.bir_x)        # bir.x --> bu classni uzgaruvchisi, barcha obyetga 1 xil boradi
#print(ikki.bir_x)
#
#Son.uzgar(100)          # classni uzagaruvchisi uzgargani uchun boshqalari ham uzgaradi
#print(bir.bir_x)
#print(ikki.bir_x)
#
#bir.uzgar(1000)
#print(bir.bir_x)
#print(ikki.bir_x)
#print(Son.bir_x)




##################++++++++++++      staticmethod     ++++++++++++#############################
#a = [2,3,5,4,45,9,2,1]
#class Tek:
#
#    @staticmethod                       # hech qanaqa class obyektiga murojat qilmasdan tashqaridan ma'lumot uqitib beradi
#    def isin(m):
#        if m in a:
#            return True
#        return False
#b = Tek
#print(b.isin(5))



##################+++++++++++        property    +++++++++++++#############################
#class Sonlar:
#    def __init__(self, x,y):
#        self.x = x
#        self.y = y
#    @property                           # funksiya nomini oddiy obyetga utqazib beradi.   plus() - qilib murojaat qilish shart emas
#    def plus(self):
#        return self.x + self.y
#    @property
#    def ayirma(self):
#        return self.x - self.y
#a = Sonlar(7, 5)

###print(a.plus())                   # property  methodi bulmagan holatda
###print(a.ayirma())                 # property  methodi bulmagan holatda

#print(a.plus)                 # property  method holatida
#print(a.ayirma)                 # property  method holatida



##################+++++++++++        setter  va  getter     +++++++++++++#############################
#class Sonlar:
#    def __init__(self, x,y):
#        self.x = x
#        self.y = y
#    @property                           # funksiya nomini oddiy obyetga utqazib beradi.   plus() - qilib murojaat qilish shart emas
#    def plus(self):
#        return self.x + self.y
#    @property
#    def ayirma(self):
#        return self.x - self.y
#
#    @ayirma.setter
#    def ayirma(self, a):
#        self.x = a
#
#    @ayirma.deleter
#    def ayirma(self):
#        self.x = None           # del self.x    #>>> obyektlarni uchiradi va xatolik beradi
#        self.y = None           # del self.y    #>>> obyektlarni uchiradi va xatolik beradi
#
#a = Sonlar(7, 5)
#print(a.plus)
#print(a.ayirma), print()
#
#a.ayirma = 9                # setter methodi uchun
#print(a.ayirma)
#print(a.plus), print()
#
#print(a.x)                  # deleter ni tekshirish uchun
#print(a.y)
#
#del a.ayirma                # deleter methodi uchun
#print(a.x)
#print(a.y)






#################+++++++++++        funksiya  anotatsiyasi      +++++++++++++#############################
#def Salom(a : int, b : str ) -> float:              # uzgaruvchidan aniq bir type suraydi
#    return a*b
#
#print(Salom(5, '100'))




#################++++++++++++                       ++++++++++++#############################



#################++++++++++++++++++++++++#############################



#################++++++++++++++++++++++++#############################


#################++++++++++++++++++++++++#############################


#################++++++++++++++++++++++++#############################


#################++++++++++++++++++++++++#############################




