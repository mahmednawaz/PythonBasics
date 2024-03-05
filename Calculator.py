flag =1
while flag==1:
    x = int(input("Enter first number...! "))
    y = int(input("Enter Second number...! "))
    if not type(x) or type(y) is int:
        print("wrong values enter integers...! \n")
    print("press 1 for addition")
    print("press 2 for subtraction")
    print("press 3 for division")
    print("press 4 for multiplication")
    choice = int(input("enter the choice... "))
    if choice == 1:
        print(x + y)
    elif choice == 2:
        print(x - y)
    elif choice == 3:
        print(int(x / y))
    else:
        print(x * y)    
    print ("Want to do more calculattions press 1... ")
    print ("Want to Exit 2... ")
    flag = int(input("Enter your ... "))
if flag >= 2 or flag <1:
    print("Thank you for using the calculator... ")
    

