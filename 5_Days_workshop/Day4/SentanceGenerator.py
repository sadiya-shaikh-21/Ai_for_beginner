import random

print("Radom story generator")

char = ["Woman","Man","Child","Teacher","Doctor"]
Setting = ['in the hall','on the table','on the floor','in the class','in the hospital']
action = ["cooking","working","sleeping",'drawing','Marking']
objects = ['fan','laptop','bed','board','injection']

print(random.choice(char),"",random.choice(action),'',random.choice(objects),'',random.choice(Setting),'.')