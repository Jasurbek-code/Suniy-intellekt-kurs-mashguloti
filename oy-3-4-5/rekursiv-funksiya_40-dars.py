#       3-misol.
def poern(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/poern(x, -n)
    else:
        if n % 2 == 0:
            return poern(x, n//2)**2
        else:
            return x*poern(x, n - 1)

x = int(input("x= "))
a, b, c = map(int, input().split())

print(x, a)
print(x, b)
print(x, c)


#       5-misol.
def fib2(n):
    global k
    if n <= k:
        return d[n]
    d[n] = fib2(n-1) + fib2(n - 2)
    k = n
    return d[n]
d = [1] * 20
k = 1
print(fib2(4))


#       6-misol.                        kombinatorika
def comb(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return comb(n-1, k-1) + comb(n-1, k)
n = 3;   k = 4
print("kombitorika: ", comb(n, k))

#       6-misol.                        kombinatorika
def combin2(n, k):
    if d[n][k] != 0:
        return d[n][k]
    if n == k or k == 0:
        d[n][k] = 1
    d[n-1][k] = combin2(n-1, k)
    d[n-1][k-1] = combin2(n-1, k-1)
    d[n][k] = d[n-1][k] + d[n-1][k-1]
    return d[n][k]
d = [[0]*15 for i in range(15)]
n = 10;   a = 2
print(combin2(n, a))




#       7-misol.
def rootK(X, K, N):
    if N == 0:
        return 1
    else:
        return rootK(X, K, N-1) - (rootK(X, K, N-1) - X/rootK(X, K, N-1)**(K-1))/K
print(rootK(3,4,2))


#       10-misol.                                           summani topish
def DigSum(n):
    if n < 10:
        return n
    return DigSum(n//10) + n%10
x = 1234
print(DigSum(x))


#       11-misol.
def strDigitSum(n):
    if len(n) == 1:
        return int(a)
    return strDigitSum(a[:len(n) - 1]) + int(a[-1])
print(strDigitSum(input("n = ")))


#       12-misol.
def Str(a):
    return a if len(a) == 1 else a[-1] + Str(a[:len(a) - 1])
b = "salom"
print(Str(b))



#       60-misol.                       Determinant ni topish
def matrix(mat, j):
    row = []
    for i in (mat[:j] + mat[j+1:]):
        row.append(i[1:])
        print(row)
        return row

def deter(m):
    print(m)
    if len(m) == 2:
        nat = m[0][0] * m[1][1] - m[1][0]*m[0][1]
        return nat
    summ = 0
    for j in range(len(m)):
        ishora = (-1)**j
        s = deter(matrix(m, j))
        summ += (ishora*m[0][j]*s)
    return summ

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(deter(a))


#       60-misol.                       Determinant ni topish
def getcofactor(m, i, j):
    return [row [:j] + row[j+1:] for row in m[:i] + m[i+1:]]

def deterofMatrix(mat):
    if (len(mat) == 2):
        valu = mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
        return valu
    Sum = 0
    for current_column in range(len(mat)):
        sign = (-1)**(current_column)
        sub_det = deterofMatrix(getcofactor(mat, 0, current_column))
        Sum += (sign*mat[0][current_column] * sub_det)
    return Sum

a = [
    [1,2,3],
    [4,5,5],
    [7,8,9]]
print("Matrixning Determinanti: ", deterofMatrix(a))



#       60-misol.                       Determinant ni topish
def determinant(det):
    if len(det) <= 1:
        return det[0][0]
    else:
        s = 0
        det0 = [[row[j] for j in range(1, len(det))] for row in det]
        for i in range(len(det)):
            det1 = det0[:]
            det1.pop(i)
            if i % 2 == 0:
                s += det[i][0]*determinant(det1)
            else:
                s -= det[i][0]*determinant(det1)
            return s
a = [
    [1,2,3],
    [4,5,5],
    [7,8,9]
]
print("Matrix determinanti: ", determinant(a))


