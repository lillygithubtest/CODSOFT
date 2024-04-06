print("Simple calculator\n")

print("operations:")
print("1-Addition")
print("2-Subtration")
print("3-Multiplication")
print("4-Division")
print("5-Power")
print("6-Exit")

opp=input("Choose Operation(1/2/3/4/5/6):")
if(opp in [1,2,3,4,5]):
    x=float(input("First number = "))
    y=float(input("Seccond number = "))

    if(opp==1):
        print(x+y)
    elif(opp==2):
       print(x-y)
    elif(opp==3):
        print(x*y)
    elif(opp==4):
        if y==0:
            print("Error! Division by zero")
        else :
         print(x/y) 
    elif(opp==5):
        print(x**y) 
elif(opp==6):
     print("Exiting the calculator")   
else:
    print("Invalid input.Enter a valid choice(1/2/3/4/5/6): ")    
                       
