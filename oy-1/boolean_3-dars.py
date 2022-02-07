#  1-misol.
A = 12;         print(A>=0)
#  2-misol.
print("A toq:", A%2 != 0)
#  3-misol.
print("A juft:", A%2 == 0)
#  4-misol.
A=6; B=3;       print(A>2 and B<=3)
#  5-misol.
A=6; B=3;       print(A>=0 or B<-2)
#  6-7-misol.
A=6; B=8; C=8;       print(A<=B<=C)

#  8-misol.    A va B toq son
A, B = 2,3;         print(A%2 != 0 and B%2 != 0)

#  9-misol.        hech bo'lmaganda bittasi toq
A, B = 2,3;         print(A%2 != 0 or B%2 != 0)

#  10-misol.
print((A%2 != 0 and B%2== 0) or (A%2 == 0 and B%2 != 0))

#  11-misol.
print((A%2 != 0 and B%2!= 0) or (A%2 == 0 and B%2 == 0))

#  12-misol.
A, B, C= 2,3,4;           print(A > 0 and B > 0 and C > 0)

#  13-misol.
A, B, C= -2,3,-4;         print(A > 0 or B > 0 or C > 0)

#  14-misol.
print((A>0 and B<0 and C<0) or (A<0 and B>0 and C<0) or (A<0 and B<0 and C>0))

#  15-misol.
print((A>0 and B>0 and C<0) or (A<0 and B>0 and C>0) or (A>0 and B<0 and C>0))

#  16-misol.
a = 26;             print(a%2 ==0 and a > 9 and a < 100)

#  17-misol.
a = 155;            print(a%2 != 0 and a > 99 and a < 1000)

#  20-misol.
a = 265;      yuz=a//100; on=a%100//10; bir=a%10
print(yuz!=on and yuz!=bir and on != bir)

#  21-misol.
a = 258;      yuz=a//100; on=a%100//10; bir=a%10
print(yuz < on < bir)

#  22-misol.
print((yuz < on < bir) or (yuz < on < bir))

#  23-misol.
print(yuz == bir)

#  24-misol.
A, B, C= 2,3,4;             D = B*B - 4*A*C
x1 = (-B*B - pow(D, 1/2)) / (2*A);      x2 = (-B*B + pow(D, 1/2)) / (2*A)
print(x1, x2)

#  25-misol.
x, y = 4, 5
print("Birinchi chorak:", x > 0 and y > 0);         print("Ikkinchi chorak:", x < 0 and y > 0)
print("Uchinchi chorak:", x < 0 and y < 0);         print("Ikkinchi chorak:", x > 0 and y < 0)

#  29-misol.
x,y = 5,6;      x1,y1, x2,y2 = 4,5,6,9
print(x1<x<x2 and y1<y<y2)

#  30-misol.
a,b,c = 4,5,6;          print("teng tomonli uchburchak")

#  31-misol.
a,b,c = 4,5,6;          print("teng yonli uchburchak")

#  32-misol.
a,b,c = 6,5,2;          print("tog'ri burchakli")

#  33-misol.
a,b,c = 4,5,6;          print(a+b>c and a+c>b and b+c>a)

#  35-misol.
x1, x2, y1, y2 = 2,3,4,5
print("bir xil rangli maydonmi:", (((x2-x1)%2 ==0) and ((y2-y1)%2 == 0)) or (((x2-x1)%2 !=0) and ((y2-y1)%2 != 0)))

#  36-misol.
x1, x2, y1, y2 = 2,3,4,5
print("Rux:", abs(x2-x1)==0 or abs(y2-y1)==0)

#  37-misol.
x1, x2, y1, y2 = 2,3,4,5
print("Shox:", abs(x2-x1) < 2 and abs(y2-y1) < 2 and (abs(x1-x2) + abs(y2-y1)) <3 )

#  38-misol.
print("Fil:", abs(x2-x1) == abs(y2-y1))

#  39-misol.
print("Farzin:", (abs(x2-x1) == abs(y2-y1)) or (abs(x2-x1)==0 or abs(y2-y1)==0))

#  40-misol.
x1, x2, y1, y2 = 2,3,4,5
print("Ot=", (abs(x2-x1)==1 and abs(y2-y1)==2) or (abs(x2-x1)==2 and abs(y2-y1)==1))


