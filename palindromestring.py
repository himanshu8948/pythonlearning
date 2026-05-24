string = input("enter the string to check palindrome !")

reverse_string = ""

for character in string :

 reverse_string = character+reverse_string


if (reverse_string == string):

   print("the string is palindrome its confirmed !:")

else:
   print("the string is not palindrome literally!")