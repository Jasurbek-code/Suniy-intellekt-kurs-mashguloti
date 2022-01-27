
#  1-2-misol.   Kvadratni perimetri va yuzasi
a = 14
print("1-2-misol. ", "Peremetr=", 4*a, "  Yuza=", a**2)

# 3-4-misol.    Tog'rito'rtburchak Perimetri va Yuzasi
a, b = 10, 8
print("3-misol. ", "Peremetr=", 2*(a+b), "   Yuza=", a*b)

# 4-misol.      Aylanani diametri bor, Uzunligini topish
d = 10
print("4-misol. ", "L=", 3.14*d)

# 5-misol.      Kubni hajmi
a = 4;              print("5-misol. ", "V=", a**3)

# 6-misol.  Paralelepepidning Hajmi va Yuzasi
a, b, c = 2, 3, 4
V = a*b*c
S = 2*(a*b + a*c + b*c)
print("6-misol.  \n\tShar hajmi=", V, "\n\tShar Sirti=", S)

# 9-misol.      O'rta geometrigi
a, b = 4, 9
print("9-misol. ", "O'rta geometrik=", pow(a*b, 1/2))

#  10-11-misol.    N!=0 va M!=0 sonni y-yig'indisi, k-ko'paytmasi, m-moduli
N, M = 5, 7
y = M + N;      k = M*N
print("10-misol.  Yig'indisi=", y, "Kopaytmasi=", k, "Modullari: M=", abs(M), "N=", abs(N))

# 12-misol.     Uchburchak gipotenuzasi va perimetri
a,b = 3,4;              c= pow(a*a + b**2, 1/2)
print("12-misol. ", "Gipotenuza c=", c,  "  Perimetri= a+b+c =", a + b + c)

# 13-misol.     Markazda bo'lmagan 2 ta Radius berilgan (R1 > R2). Yuzalari S1, S2
R1, R2 = 15, 10
print("13-misol.  S1=", 3.14*R1, "  S2=", R2*3.14, "\n\tYuzalar ayirmasi=", 3.14*(R1 - R2))

# 14-misol.         L berilgan. Aylana radiusi va yuzasi
L = 26
R = L/2*3.14
S = 3.14*(R**2)
print("14-misol.  R=", R, "S=", S)

# 15-misol.         S aylana yuzasi berilgan. diametri va radiusi
S = 25
R = pow(S/3.14, 0.5)
d = 2*R
print("15-misol.   R=", R, "d=", d)

# 16-misol.
x1, x2 = 9, 5
print("16-misol.  Ikki nuqta orasidagi masofa=", x1 - x2)

# 17-misol.     AC va BC kesmaning uzunligi va kesmalar uzunligining yig'indisi         ????????????????????????????????????
A,B,C = 3,4,5;          AC = A+B;   BC = B+C
print("17-misol.  AC=", AC, "  BC=", BC, "  Yig'indisi=", AC+BC)

# 20-misol.     Tekislikda berilgan koordinata orqali nuqtalar orasidagi masofa
x1,x2, y1,y2 = 2,3,4,5;          L = pow(((x2-x1)**2 + (y2-y1)**2), 1/2)
print("20-misol. ", "Masofa L=", L)

# 21-misol.         Koordinata orqali uchburchak yuzasini topish
x1,y1, x2,y2, x3,y3 = 2,3, 7,6, 12,4
a = (pow((x1-x2)**2 + (y1-y2)**2, 0.5))
b = (pow((x3-x2)**2 + (y3-y2)**2, 0.5))
c = (pow((x1-x3)**2 + (y1-y3)**2, 0.5))

p = (a + b + c)/2
yuza = pow(p*(p-a)*(p-b)*(p-c), 1/2)

print("21-misol.  Peremetri=", p, "Yuzasi=", yuza)

# 22-misol.         Sonni qiymatini almashtirish
A, B = 5, 6
A = A + B
B = A - B
A = A - B
print("22-misol. ", "A=", A, "  B=", B)

# 23-misol.         A => B ga, B => C ga, C => A ga o'zlashtirilsin
A, B, C = 4,5,6
A = A + B + C
B = A - B - C
C = A - B - C
A = A - B - C
print("23-misol. ", "A=",A, "  B=",B, "  C=",C)

# 25-misol.     x ni qiymati berilgan. funksiya
x=2;          y = 3*x**6 - 6*x*x - 7
print("25-misol. ", "y=", y)

# 27-28-misol.
A=2;            print("27-28-misol. ", "A^2=", A**2, "  A^3=", A**3,"  A^4=", A**4,"  A^5=", A**5, "  A^8=", A**8)

# 29-misol.     radianga o'tqazuvchi
gradus = 100;       print("29-misol. ", "Radian=", 3.14*gradus/180)

# 30-misol.     radianga o'tqazuvchi
radian = 5;       print("30-misol. ", "Gradus=", radian*180/3.14)

# 31-misol.       Temperaturani Farengeytda chiqarish
Tc = 45;         Tf = (Tc - 32)*5/9
print("31-misol. ", "Farengeyt Tf=", Tf)

# 33-34-misol.        konfet narxi
X_kg = 2;    A_sum = 2000
Y_kg = 4    #int(input("Necha kg:"))
Y_sum = Y_kg*A_sum/X_kg
print("33-34-misol.  Sum:", Y_sum)

# 35-misol.     Qayiq tezligi V, oqim tezligi U, daryo oqim buyicha harakati vaqti T1, oqimga qarshi T2.
#                qayiqni yurgan S yuli aniqlansin
V = 20; U = 2;  T1=1; T2=3
S = (V+U)*T1 + (V-U)*T2
print("35-misol. ", "Yurgan yuli  S=", S)

# 36-misol.     v1, v2 tezlikli mashinalar S masofada,uzoqlashmoqda, t vaqtdan keyin ular orasidagi masofa.
v1, v2 = 2,3;  t = 2; S = 30
L_uzoq = t*(v1 + v2) + S
L_yaqin = S - t*(v1 + v2)
print("36-misol. ", "Uzoqlashganda masofa L=", L_uzoq)
print("37-misol. ", "Yaqinlashganda masofa L=", L_yaqin)

# 38-misol.         chiziqli tenglama
A, B = 4,6;            x = - (B/A)
print("38-misol. ", "x=", x)

# 39-misol.         diskriminant topish
A,B,C = 4,5,6
D = B*B - 4*A*C;   x1= -B + (D)**(1/2)/(2*A);   x2= -B - (D)**(1/2)/(2*A)
print("39-misol. ", "D=", D,"  x1=",x1, "  x2=",x2)

# 40-misol.
A1, B1, C1, A2, B2, C2 = 2,3,4,5,6,7
D = (A1*B2 - A2*B1);   x = (C1*B2 - C2*B1)/D; y = (A1*C2 - A2*C2)/D
print("40-misol.")
print("   C1=", A1*x + B1*y)        #A1*x + B1*y = C1
print("   C2=", A2*x + B2*y)        #A2*x + B2*y = C2



