import random
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
p1 = first_name[0:3]
p2 = last_name[0:3]
randomint = random.randint(1,99)
p3=str(randomint)
print(p1+p2+p3 , "is your generated username")