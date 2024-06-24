num1=int(input("enter 1st number : "))
num2=int(input("enter 2nd number : "))

maxnum=max(num1,num2)

while(True):
        if maxnum%num1==0 and maxnum%num2==0:
            print(f"lcm of the two numbers is {maxnum}")
            break
        maxnum=maxnum+1
                
