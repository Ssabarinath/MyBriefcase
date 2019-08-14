n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("YES, it is an armstrong number. ")
else:
    print("NO, it is not an arsmtrong number. ")
