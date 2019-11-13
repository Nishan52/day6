#yo import garyo bhane code le result paayexe aru line execute garna didaina directly program exit hunxa
import sys
#asking name and validating name
name=input("Enter your Name please\n")
a=len(name)
int(a)
if name.isalpha()==True and a>3:
    print("Valid Name")
else:
#system.exit le program lai stop garauxa
    sys.exit("OOPS! Invalid Name")
#validating phone number
phonenum=input("Please Enter your phone number")
if phonenum.isdigit()==True and len(phonenum)==10:
    print("Valid phone number")
else:
    sys.exit("OOPS! Invalid Phone number")
#validating age
age=input("please enter your age")
if age.isdigit()==True and int(age)>=18:
    print("Valid age")
else:
    sys.exit("Invalid age")
