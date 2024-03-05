num1=int(input("Enter first number... "))
num2=int(input("Enter second number... "))
print("1 for addition... ","2 for substraction...", "3 for division... ","4 for mutiplication... ")
choice=int(input ("Enter your choice... "))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice==3:
    if num2==0:
        print("invalid number")
    num2=int(input("Enter second number... "))
    print(num1/num2)
elif choice==4:
    print(num1*num2)
else:
    print("invalid Choice")
