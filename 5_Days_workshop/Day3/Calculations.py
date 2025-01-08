x = float(input("Enter num 1 "))
y = float(input("Enter num 2 "))

char = input("Enter which opreation u want to perform from these +,-,*:")

if(char == '+'):
    print(x+y)
elif(char == '-'):
    print(x-y)
elif(char == '*'):
    print(x*y)
else:
    print("plese enter valid operation")