num=int(input("Enter the number"))
if num>0:
    if num%2==0:
        print(" the entered number is even")
    elif num==0:
        print("Entered number not classified as odd or even")
    else:
        print("Entered number is odd")
else:
    print("Entered number can't be classified as odd or even")