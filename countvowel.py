string =input("enter your string to count the no. of vowel:")

c = 0
for character in string : 
    if(character == 'a'):

     c += 1 
    elif(character == 'e'):
    
     c += 1 
    elif(character == 'i'):
    
     c += 1

    elif(character == 'o'):
    
     c += 1 

    elif(character == 'u'):
      
     c += 1

if(c>0):
     

 print( "your string has : ",c,"vowels")

else:
      
 print("your string has no vowels ! ")