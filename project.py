import random

response = 'y'

while response == 'y':
    num = random.randint(1,6)
    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(3)
    elif num == 4:
        print(4)
    elif num == 5:
        print(5)
    elif num == 6:
        print(6)
    
    response = input("Type y to continue and n to exit")
    if response == 'y' or response == 'Y':
        continue
    elif response == 'n' or response == 'N':
        break
    else:
        print("Please enter suitable input")
        break
    
    
print("Done")
