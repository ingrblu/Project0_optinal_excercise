
def add(x, y):
    add = x+y
    return add

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def sinius(x, N):
    sin = 0
    for n in range(N+1):
        sin += ((-1)**n*x**(2*n+1))/(fact(2*n+1))
    return sin

def divide(x, y):
    div = x/y
    return div

def exalted(x, n):
    return x**n

def multiply(x, y):
    return x*y
