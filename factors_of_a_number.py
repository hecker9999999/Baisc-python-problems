num = int(input("Enter a number: "))

lst = []

for i in range(1, 10):
    if num%i == 0:
        lst.append(i)
print(lst)
