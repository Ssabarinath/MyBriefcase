num = int(input("Enter any number: "))
a = num%2
if a == 0:
    print(num, "It is an even number")
elif a == 1:
    print(num, "It is an odd number")
else:
    print("The input is Invalid")
