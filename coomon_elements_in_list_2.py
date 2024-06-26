lst1=list(input("enter 1st list : "))
lst2=list(input("enter 2nd list : "))

print(sorted(list(set(lst1)&set(lst2))))       #also sorting them