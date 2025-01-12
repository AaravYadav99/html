class flashc:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning =meaning
    def __str__(self):
        return self.word+("(+self.meaning+)")
flash=[]
print("welcome to flash card Application")
while(True):
    word=input("enter th word")
    meaning=input("enter the meaning")
    flash.append(flashc(word,meaning))
    op=input("do you want to continue(y/n)")
    if op.lower()=='n':
        break
print("the flash cards")
for i in flash:
    print("*",i)        