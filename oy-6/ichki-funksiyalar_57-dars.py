# __main__ -
# __name__ -
# __next__ - next() - iteratsiyani bitta-bitta utqazish uchun
# __iter__ - iter() - iteratsiya hosil qilib beradi
# __init__ -
# __doc__ -   funksiya ichidagi kommentariyalarni chiqarib beradi.
# __import__ -  moduldan funksiya chaqirib ishlatish mumkin
# __
# map - filter - lambda --> iteratsiya hosil qilish uchun funksiya




## bir fayldan ikkinchi fayl nomini bilish
### >> bir.py
#import ikki
#if __name__=='__main__':
#    print("Birinchi faylman")
#print(ikki.__name__)
#
### >> ikki.py
#if __name__=='__main__':
#    print("Men Ishladim")
#else:
#    print(__name__)
#    print("Boshqa joydaman")


##  modulni chaqirish
#matemetika = __import__('math')         # import math as matematika
#print(matemetika.sqrt(4))


##   iteratsiay qilish
#a = [2,3,5,4,8,7,6]
#a = iter(a)
#for i in a:
#    print(i)
#
#b = a.__iter__()
#for i in b:
#    print(i)



#####      next  funksiya
#a = [1,2,3,4,5,6]
#a = iter(a)
#print(a.__next__())
#print(next(a))
#print(a.__next__())









#####       Lambda va Filter funksiyalari
#a = [1,2,3,4,5,6]
#a = map(lambda i : i*2, a)
#print(list(a))
#
#a = [1,2,3,4,5,6]
#a = filter(lambda i : i*2, a)           # shartni tekshirib javob qaytaradi
#print(list(a))
#
#
#a = [1,2,3,4,5,6]
#a = map(lambda i : i%2, a)
#print(list(a))
#
#a = [1,2,3,4,5,6]
#a = filter(lambda i : i%2, a)           # shartni tekshirib javob qaytaradi
#print(list(a))
#
#
#a = [1,2,3,4,5,6]
#def funksiya(i):
#    return i%3 == 0
#a = filter(funksiya, a)
#print(list(a))








####   global va local uzgaruvchiga murajaat
#def salom():
#    print(a)        # globalda va localda 1 xil uzgaruvchi bulsa localni oladi faqat
#a = "helo"
#salom()







#####             TUB sonlarni chiqarish
#def find(x):
#    for i in range(2, x):
#        if x%i == 0:
#            return False
#    return True
#n = list(filter(find, range(2, 100)))
#print(n)


####        Katta kichik so'zlarni chiqarish. 2 ta funksiya ishatish
#def katta(a):
#    return a.upper()
#def kichik(a):
#    return a.lower()
#def chaqir(funcsiya):
#    return funcsiya(input("So'z kiriting: "))
#
#chiqar = chaqir
#print(chiqar(katta))
#print(chiqar(kichik))



####   massivdan keraksiz raqamlarni o'chirish
#import random
#def Olib_tashlash(a, x):
#    for i in range(a.count(x)):
#        a.remove(x)
#    return a, len(a)
#a = [random.randint(1,9) for i in range(random.randint(10, 20))]
#print(a)
#x1 = int(input("x1= "))
#print(Olib_tashlash(a, x1))
#x2 = int(input("x2= "))
#print(Olib_tashlash(a, x2))
#x3 = int(input("x3= "))
#print(Olib_tashlash(a, x3))





