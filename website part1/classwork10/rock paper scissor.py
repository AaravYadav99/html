import random
ch=["rock","paper","scissor"]
comp=random.choice(ch)
print(comp)
user=input("enter rock or paper or scissor")
if comp.lower() == user.lower():
    print("it is a tie")
elif(user.lower()== 'rock' and comp.lower()== 'scissor') or(user.lower()== 'scissor' and comp.lower()== 'paper') or (user.lower()== 'paper' and comp.lower()== 'rock'):
    print("you win the game")
else:
    print("computer win")

