
import numpy as np



a = np.array([3,2,5,9,4,1,9,7,2,4,6,7,6,4,2,5,8,6,2,4,8,2,1,7,1,5,8]).reshape(3,3,3)
#print(a)
#print()
#print('===========================')
#print()
#
#print(a.max(0))


###########                 sort      ###########################3

#dtypes = [('Ism', 'U32'), ('Yosh', 'int32'), ('Kurs', 'int32')]               # type larni alohida berish     !!!!!!!!!!!!!!!!!
#
#mal = np.array([('Yodgor', 19, 3),  ('Ismoil', 21, 2),  ('Gulruh', 20, 4)],  dtype=dtypes)          # dtypes ni dtype ga tenglaymiz
#print(mal)
#print(np.sort(mal, order='Ism'))                                              # Ism buyicha saralaymiz.







#              gullarni haftalik narxini topish

narx = [3, 4, 2]
hafta_kuni1 = [[120, 80, 60], [90, 70, 40], [60, 40, 20]]
hafta_kuni = [120, 80, 60]

print(np.matmul(hafta_kuni1, narx), "=", sum(np.matmul(hafta_kuni1, narx)))




