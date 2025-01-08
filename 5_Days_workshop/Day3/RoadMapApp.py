print("Roadmap Provider Project")
level = input("Enter F for fresher and E for Experienced ")

if level == 'F':
    intrest = int(input("Enter in which domain you are intrested 1-Web Dev 2-App Dev 3-DS,ML,AI "))
    if intrest==1:
        print("Learn HTML, CSS, Js and Python Django")
    elif intrest==2:
        print(" Learn Java, DSA and Build Projects")
    elif intrest==3:
        print(" Learn Python, Maths and R")
    else:
        print("Please enter valid option")
elif level == 'E':
    intrest = int(input("Enter in which domain you are intrested 1-Data Analytics 2-Cloud Computing 3-Front end "))
    if intrest==1:
        print(" Learn Pyton,Excel and PowerBI")
    elif intrest==2:
        print(" Learn DevOps and Python for Automation")
    elif intrest==3:
        print(" Learn Python and Django for Backend")
    else:
        print("Please enter valid option")
else:
    print("Please Enter valid Option")