print("Certificate Eligibility")
level = int(input("Enter 1 if you present All Day and 2 if you present alternet Day "))
if level == 1:
    Assg = (input("Enter in which domain you are intrested if you completed all the assignment y/n "))
    Live = (input("you attended all live classes y/n "))
    Camera = (input("Your camera was on during classes y/n "))
    if Assg=='y' and Live=='y':
        print("Eligible for certificate")
    elif Assg=='y' and Live=='y' and Camera=='y':
        print("Eligible for certificate")
    elif Camera=='y' and Assg=='y':
        print("Eligible for certificate")
    else:
        print("Not Eligible for certificate")
elif level == 2:
    print("Not Eligible for certificate")
else:
    print("Please Enter valid Option") 