#def f (n):
#    return(n*n*n)
#print(f(5))
#
#def g(n):
#    return f(n)-5
#print(g(5))


#a = int(input())
#b = int(input())

#def x (a,b):
#    for i in range(a, b+1):
#        print(i*i)

#print(x(a,b))


#def y(n):
#    for i in range(n):
#        if(i % 3 == 0 and i % 5 == 2):
#            print(i)
#
#print(y(50))

import math

def u(x):
    if x%2==0:
        return 2
    if x <= 1:
        return 3
    for i in range(2, math.sqrt(x)):
        if x % i == 0:
            return 2
            
    return 0




#def pkv(x):
#    k=math.sqrt(x)
#    f = math.floor(k)
#    if f*f == x:
#        return 1
#    else:
#        return 0
#print(pkv(25))
#print(pkv(7))

#a = int(input())
#brojeviParni = 0
#for i in range(a):
#    x = int(input())
#    if x % 2 == 0:
#        brojeviParni = brojeviParni + 1
#print(brojeviParni)


#b = int(input())
#def a():
#    brojeviNeparniZbir = 0
#    for i in range(b):
#        x = int(input())
#        if x % 2 != 0:
#            brojeviNeparniZbir = brojeviNeparniZbir + x
#    print(brojeviNeparniZbir)   
#a()

#def f(n):
#    last=-1000
#    for i in range(n):
#        x=int(input())
#        if x <= last:
#            return 0
#        last = x
#        
#    return 1
#n=int(input())
#print(f(n))

cifre = []
suma = 0
def h(x):
    global suma
    a = str(x)
    for i in range(len(a)):
        cifre.append(a[i])
        print(int(cifre[i]))
        suma = suma + int(cifre[i])

h(22)
print(suma)
    
        
        
