
#def args_tuple(a, b, *c):                      # * - tuple qiymat qabul qiladi
#    return a, b, c
#print(args_tuple("a harfi.", "b harfi.", "c harfi1", "c harfi2.", "c harfi2.", "c harfi < memory error > bo'lguncha uzgaruvchi oladi"))
#print()
#
#def args_dict(k, **n):                         # ** - lugat qiymat qabul qiladi
#    print(k, f"harf.      n ni type {type(n)}")
#    for i, j in n.items():
#        print(f"{i} - {j}")
#print(args_dict('k', a = 'bir', b = 'ikki', c = 'uch'))


##       yield  funksiyasi
#def lazy_iteratsiyasi(a):
#    yield a + 1                                             # bu funksiya xotiradan juda kam joy egallab foydalanih uchun
#    yield a + 2
#    yield a + 3
#    yield a + 4
#print("type", type(lazy_iteratsiyasi(6)))


#print("for orqali")
#for i in lazy_iteratsiyasi(2):
#    print(i)
#print()


#print("__next__() funksiya orqali")
#n = lazy_iteratsiyasi(4)
#print(n.__next__())
#print(n.__next__())
#
#m = lazy_iteratsiyasi(1)            # 1 raqamini o'zgaruvchi sifatida olmasdan avvalgi ishlanganni davom ettirib ketadi
#print(n.__next__())
#print(n.__next__())




##   katta hajmli faylni ochib undan unumli foydalanish
##        yield funksiyasi bilan katta hajmli faylni ochish
#def katta_faylni_uqish(fayl_nomi):
#    for i in open(fayl_nomi, encoding="utf-8"):
#        yield i
#
#S = 0
#for i in katta_faylni_uqish("fayl_nomi_kiritamiz.csv"):
#    S += 1


##        F I B O N CH CH I    topish
#def Fib(n):
#     a = 0;  b = 1
#     yield a
#
#     i = 2
#     while i <= n:
#         yield b
#         a, b = b, a + b
#         i += 1
#for i in Fib(9):
#    print(i)








#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                      C L A S S
class Salom():
    def Tanishuv(self, ismiZ, yoshiZ):
        self.ismiz = ismiZ
        self.yoshiz = yoshiZ

    def Qadirdonlarga(self):
        return "Salom qadrdonim"
    def Begona_tanishlar(self, ism, yosh):
        self.ismiz = ism
        self.yoshiz = yosh

y = Salom()
y.Tanishuv("Aziz", "25")
print(f"ismingizni {y.ismiz} shunaqa dedizmi, yoshiz {y.yoshiz} yoshdami?")

print(Salom.Qadirdonlarga(self=Salom()))

x = Salom()
x.Begona_tanishlar("Bilol", "23")
print(f"salom ismingiz {x.ismiz} shunaqami, yoshiz {x.yoshiz} shunaqa edi a")








