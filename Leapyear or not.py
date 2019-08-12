
A = int(input("Enter Year: "))
if A % 4 == 0 and A % 100 != 0:
    print(A, "is a Leap Year")
elif A % 100 == 0:
    print(A, "is not a Leap Year")
elif A % 400 ==0:
    print(A, "is a Leap Year")
else:
    print(A, "is not a Leap Year")
