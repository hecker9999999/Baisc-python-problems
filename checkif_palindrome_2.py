while True:
    my_string = input("Enter the string (or 'q' to quit): ")
    
    if my_string.lower() == 'q':
        break
    
    if my_string == my_string[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
