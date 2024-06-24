num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))

if num1>num2:
    minnum=num2
else:
    minnum=num1

for i in range(1,minnum+1):
        if num1%i==0 and num2%i==0:
            hcf =i
print(f"hcf of the two numbers is {hcf}")
