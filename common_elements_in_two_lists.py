lst1=list(input("enter 1st list : "))
lst2=list(input("enter 2nd list : "))

print(list(set(lst1).intersection(lst2))) #Since lst2 is a list, it is implicitly converted to a set within the intersection method to perform the operation.