a = int(input("Enter an Number : "))
exponent = int(input("Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * a
    
print("The Result of {0} Power {1} = {2}".format(a, exponent, power))
