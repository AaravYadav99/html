import random
class fruitq:
    def __init__(self):
        self.fruit={'apple':'red','banana':'yellow','orange':'orange','watermelon':'green'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruit.items()))
            print("enter the color of",fruit)
            user_input=input()
            if user_input.lower()==color:
                print("correct answer")
            else:
                print("wrong answer")
            op=input("do you want to continue (y/n)")
            if op.lower()=='n':
                break
print("elcome to fruit quiz")
quiz1=fruitq()
quiz1.quiz()
