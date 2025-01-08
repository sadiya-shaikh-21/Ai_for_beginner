import random

lst = [1,2,3,4,5]

user = int(input("Please enter any number between 1-5 "))
Computer = random.choice(lst)
#print(Computer)

if user not in lst:
    print("out of range")