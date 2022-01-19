#  1-2-misol.   Kvadratni perimetri va yuzasi
a = 15;            print("P=", 4*a, "  S=", a**2)

# 3-4-misol.    Tog'rito'rtburchak Perimetri va Yuzasi
a,b = 10,8;        print("P=", 2*(a+b), "   S=", a*b)

# 4-misol.      Aylanani diametri bor, Uzunligini topish
d = 10;            print("L=", 3.14*d)

# 5-misol.      Kubni hajmi
a = 4;             print("V=", a**3)

# 6-misol.  Kubni to'la sirti
a, b, c = 2,3,4;     print("Shar Sirti=", 2*(a*b + b*c + a*c))

# 9-misol.      O'rta geometrigi
a,b = 4,9;            print("O'rta geometrik=", pow(a*b, 1/2))

# 12-misol.     Uchburchak gipotenuzasi va perimetri
a,b = 3,4;           c= pow(a*a + b**2, 1/2)
print("Gipotenuza c=", c,  "  Perimetri= a+b+c =", a + b + c)

# 13-misol.     Markazda bo'lmagan 2 ta Radius berilgan (R1 > R2). Yuzalari S1, S2
R1, R2 = 15, 10;        print("S1=", 3.14*R1, "  S2=", R2*3.14)

# 17-misol.     AC va BC kesmaning uzunligi va kesmalar uzunligining yig'indisi         ????????????????????????????????????
A,B,C = 3,4,5;          AC = A+B;   BC = B+C
print("AC=", AC, "  BC=", BC, "  Yig'indisi=", AC+BC)

# 20-misol.     Tekislikda berilgan nuqtalar orasidagi masofa
x1,x2,y1,y2 = 2,3,4,5;          L = pow(((x2-x1)**2 + (y2-y1)**2), 1/2)
print("Masofa L=", L)

# 22-misol.         Sonni qiymatini almashtirish
A, B = 5, 6
A = A + B
B = A - B
A = A - B
print("A=", A, "  B=", B)

# 23-misol.         A => B ga, B => C ga, C => A ga o'zlashtirilsin
A, B, C = 4,5,6
A = A + B + C
B = A - B - C
C = A - B - C
A = A - B - C
print("A=",A, "  B=",B, "  C=",C)

# 25-misol.     x ni qiymati berilgan.
x=2;          y = 3*x**6 - 6*x*x - 7;       print("y=", y)

# 27-misol.
A=2;            print("A^2=", A**2, "  A^4=", A**4, "  A^8=", A**8)

# 29-misol.     radianga o'tqazuvchi
gradus = 180;       print("Radian=", 3.14*gradus/180)

# 31-misol.       Temperaturani Farengeytda chiqarish
Tc = 45;         Tf = (Tc - 32)*5/9
print("Farengeyt Tf=", Tf)

# 35-misol.     Qayiq tezligi V, oqim tezligi U, daryo oqim buyicha harakati vaqti T1, oqimga qarshi T2.
#                qayiqni yurgan S yuli aniqlansin
V = 20; U = 2;  T1=1; T2=3;                         S = (V+U)*T1 + (V-U)*T2
print("Yurgan yuli  S=", S)

# 36-misol.     v1, v2 tezlikli mashinalar S masofada,uzoqlashmoqda, t vaqtdan keyin ular orasidagi masofa.
v1, v2 = 2,3; t = 2; S = 30;                      L = t*(v1 + v2) + S
print("Uzoqlashganda masofa L=", L)

# 38-misol.         chiziqli tenglama
A, B = 4,6;            x = - (B/A);              print("x=", x)

# 39-misol.         diskriminant topish
A,B,C = 4,5,6
D = B*B - 4*A*C;   x1= -B + (D)**(1/2)/(2*A);   x2= -B - (D)**(1/2)/(2*A)
print("D=", D,"  x1=",x1, "  x2=",x2)

# 40-misol.
A1, B1, C1, A2, B2, C2 = 2,3,4,5,6,7
D = (A1*B2 - A2*B1);   x = (C1*B2 - C2*B1)/D; y = (A1*C2 - A2*C2)/D
#A1*x + B1*y = C1
#A2*x + B2*y = C2