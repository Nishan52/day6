import sys
side1=input("Enter the length of a side one")
side2=input("Enter the length of a side two")
side3=input("Enter the length of a side three")
side4=input("Enter the length of a side four")
if side1==side2==side3==side4:
    sys.exit("The Resulted formed shape is a SQUARE")
elif side1==side2 and side3==side4:
    sys.exit("The Resulted formed shape is a RECTANGLE")
elif side1==side4 and side2==side3:
    sys.exit("The Resulted formed shape is a RECTANGLE")
elif side1==side3 and side2==side4:
    sys.exit("The Resulted formed shape is a RECTANGLE")
else:
    print("The shape is irregular polygon")
