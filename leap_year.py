year=int(input("Enter the year you want to check : ")) # give some mercy and check the year excluding your birthday


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):      # generally we devide with 4 to verify wether it's a leap year,
    print("Yes it is a leap year")                         # but its actually "400" which we should verify is or with bot 4 and 100
else:
    print("not a leap year mf , stay hard")    