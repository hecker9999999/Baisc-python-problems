print("1st number : ")
a = int(input())
print("2nd number : ")
b = int(input())
print("operation : ")
opr = input()

def add(a,b):
    c=a+b
    return c

def sub(a,b):
    d = a-b
    return d

def mul(a,b):
    e = a*b
    return e

def div(a,b):
    f = a/b
    return f

def mod(a,b):
    g = a%b
    return g

if opr == "+":
    print("sum is : ",add(a,b))
elif opr == "-":
    print("subtraction is :", sub(a, b))
elif opr == "*":
    print("multiplication is :", mul(a, b))
elif opr == "/":
    print("division is : ", div(a,b))
else:
    print("modulo is : ", mod(a,b))