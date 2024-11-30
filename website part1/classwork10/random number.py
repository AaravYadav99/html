import random
computer=random.randint(10,20)
while True:
    no=int(input("enter the numbe between 10 to 20"))
    if no == computer:
        print("you win the game")
        break;
    else:
        print("try again")

    choice = input("do you try (y/n)")
    if choice== 'n':
        break