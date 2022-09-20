
#try:                                                # xato bo yuqligini bildiradi
#    print(1/0)
#except ZeroDivisionError:                           # try da aniq bir xatolikni bilsak shuni yozib quyish mumkin
#    print("ZeroDivisionError  ishladi")
#except:                                             # try da xatolik bo'lsa ishlaydi
#    print("nolga bulib bulmaydi")
#    #raise ZeroDivisionError("Zero xato chiqdi")    # xatolikni tekshirish
#else:                                               # faqat try ishlasa ishlaydi
#    print("try dan keyin else ishladi")
#finally:                                            # try va except ishlab bo'lgandan keyin ishlaydi
#    print("hammasi ishlab buldi.")






#                                         map funksiyasi
a, b, c = map(int, input().split())
print(a,b,c)

a = map(int, input().split())
print(list(a))
a = list(map(int, input().split()))
print(a)

l = [2,6,5,4,8,6,13,1]
b = list(map(lambda i: i*3, l))
print(b)

matn = ['Ruslan', 'Eldor']
a = list(map(list, matn))








