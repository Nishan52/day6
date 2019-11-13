marks=int(input("Enter your marks"))
if marks>=90 and marks<100:
    print("You have scored A")
elif marks>=70 and marks<90:
    print("You have scored B")
elif marks>=40 and marks<70:
    print("You scored C")
elif marks<40 and marks>=0:
    print("YOu are fail")
else:
    print("ENTERED MARKS IS OUT OF RANGE")