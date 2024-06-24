n = int(input("Enter the nth natural number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of the first {n} natural numbers is {total}")