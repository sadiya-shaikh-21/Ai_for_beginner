print("Certificate Eligibility")
level = int(input("Enter 1 if you present All Day and 2 if you present alternet Day "))
if level == 1:
    intrest = int(input("Enter in which domain you are intrested 1-if you completed all the assignment 2-you attended all live classes 3-Your camera was on during classes "))
    if intrest==1:
        print("Eligible for certificate")
    elif intrest==2:
        print("Eligible for certificate")
    elif intrest==3:
        print("Eligible for certificate")
    else:
        print("Not Eligible for certificate")
elif level == 2:
    print("Not Eligible for certificate")
else:
    print("Please Enter valid Option") 