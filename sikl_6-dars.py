#  1-misol.
n = 3
k = 1; s = 0
while k <= n:
    s += 1/k
    k += 1
    print(s)

#  2-misol.
n =5
k, S = 1, 0
while k <= n:
    S += 1/(2*k+1)**2
    k += 1
    print("ikkinchi", S)

#  3-misol.
n =5
k, S = 1, 0
while k <= n:
    S += pow(-1, k)/((2*k+1)**k)
    k += 1
    print("ikkinchi", S)

#  4-misol.
n, x = 5, 4
i, S = 1, 0
while i <= n:
    S += pow(x, i)/(i)
    i += 1
    print("ikkinchi", S)
#  5-misol.

#  6-misol.                                 raqamni yig'indisi 1-usul
son = 123456789 # int(input("son ="))
S, l = 0, 1
while l < son:
    S += son//l%10
    l *= 10
print(S)

#  7-misol.                                 raqamni yig'indisi 2-usul
son = 123456789
s = 0
while son > 0:
    s += son % 10
    son //= 10
print(s)

#  8-misol.
n = 45 #int(input("son="))
i, s = 1, 0
print("bo'luvchi:", end=" ")
while i <= n:
    if n%i == 0:
        print(i, end=", ")
        s += 1
    i += 1
else:
    print(" >>", s, "ta")

#  9-misol.
#oxirgisi businda


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.


#  -misol.




