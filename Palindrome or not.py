num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('Yes,it is PALINDROME')
    else:
        print('No,it is not a palindrome')
except ValueError:
    print("It is not a number,So it not a palindrome !")
