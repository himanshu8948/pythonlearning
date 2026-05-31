a = int(input("enter the no. to find its digits sum :"))

sum = 0
digits = 0
while (a!= 0) :
    sum = a % 10

    digits += sum

    a = a//10


print("Sum of the digits of the no. : ",digits)