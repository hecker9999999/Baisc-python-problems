num=int(input("enter the desired number : "))

def fact(num) :
    factorial=1
    for i in range(1,num+1):
       factorial*=i
    return factorial

print("Factorial is ", fact(num))
