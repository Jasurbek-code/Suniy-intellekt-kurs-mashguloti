import re

#                        1 - misol
#  regex orqali sanani tekshiruvchi dastur


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

#def Sana(sana):
#    kun, oy, yil = map(str, sana.split("-"))
#    print("Kun:", kun, "  Oy:", oy, "  Yil:", yil, "    Sana:", sana)
#
#    #yil = r"^(1\d|20)\d\d$"
#
#    if oy=='02' or oy=='2':
#        if yil%4 == 0 and (yil%100 != 0 and yil%400==0):
#            kun = r'?:0?[1-9]|1\d|2[0-9]'
#        else:
#            kun = r'?:0?[1-9]|1\d|2[0-8]'
#    elif oy=="04" or oy=="06" or oy=="09" or oy=="4" or oy=="6" or oy=="9" or oy=="11":
#        kun = r"0?[1-9]|[12]\d|30"
#    elif oy=='01' or oy=='1' or oy=='03' or oy=='3' or oy=='05' or oy=='5' or oy=='07' or oy=='7' or oy=='08' or oy=='8' or oy=='10' or oy=='12':
#        kun = r"0?[1-9]|[12]\d|3[01]"
#    else:
#        print("kun xato")
#
#
#    natija = re.match(r"0?[1-9]|[12]\d|3[01].%s.%s" %(oy, yil), sana)
#
#    return natija, "  natijaviy:", kun, oy, yil
#
#sana = input("sanalar: ")
#print(Sana(sana))






#                           2 - misol




