import sys
import math
name=input("Enter your name")
if name.isalpha()==True and len(name)>5:
    print("Your are Successfully Registered")
else:
    sys.exit("OOPS! not reristered. TRY AGAIN")
run_again="yes"
while run_again=="yes":
    print("Select operation")
    print("1.Add           2.Subtract")
    print("3.Multiply      4.Modulous")
    print("5.square root   6. Square")
    print("7.division")
    select=int(input("your choice operation 1/2/3/4/5/6/7     "))
    if select==1:
        num1=int(input("Enter the first number"))
        num2=int(input("Enter the second number"))
        sum=num1+num2
        print("The sum of the number is ",sum)
    elif select==2:
        num1=int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        difference=num1-num2
        print("The difference of the given number is ",difference)
    elif select==3:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        product=num1*num2
        print("the product of the given number is",product)
    elif select==4:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        rem=num1%num2
        print("The remainder of the given number is",rem)
    elif select==5:
        num1 = int(input("Enter the first number"))
        sqroot=math.sqrt(num1)
        print("The square root of the given number is ",sqroot)
    elif select==6:
        num1 = int(input("Enter the first number"))
        square=num1*num1
        square=int(square)
        print("The square of the given number is ",square)
    elif select==7:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        quoitent=num1/num2
        print("The Quoitent of the given number is",float(quoitent))
    else:
        sys.exit("OPERATION OUT OF THE RANGE")
    calcagain=input("\nYou want to calculate again:(yes/no)     ")