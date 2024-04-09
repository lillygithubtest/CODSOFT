import random 
import string

length=int(input("Enter the length of your password: "))
letters=string.ascii_letters
numbers=string.digits
special=string.punctuation

character=letters+numbers+special
pwd = random.sample(character,length)
password = "".join(pwd)
print("Generated password : ")   
print(password)