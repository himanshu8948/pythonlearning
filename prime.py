a = int(input("enter the no. to check if it is prime or not :"))

divisible = 0
count = 0

for i in range(1,a+1):
 if(a % i == 0):

    count += 1 
else :
    count += 0

if(count == 2):
    print("your entered no. is prime no. :")

else :
    print("your entered no. is not a prime no. :")