from random import randint  


num1 = int(input("Enter your 1st number: "))

num2 = int(input("Enter your 2nd number: "))

if num1 > num2:
    num1, num2 = num2, num1

def random_number(num1, num2):
    return random.randint(num1, num2)



choice_grabber = random_number(num1, num2)




guess = int(input("Guess your number"))

while(True):
    if guess != choice_grabber:
        print("Try again")
        guess = int(input("Guess your number"))
    else:
        print("You got it!")
        break