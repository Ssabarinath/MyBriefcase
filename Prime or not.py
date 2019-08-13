num = int(input("Enter any number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "NO,it is not a prime number")
            break
else:
    Print(num, "YES, it is a prime number")
else:
    print(num, "NO,it is not a prime number")
