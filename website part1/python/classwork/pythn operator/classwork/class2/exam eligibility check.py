mc=input("enter you have a medical cause or not \n1. yes \n2. no")
if mc=="1":
    print("you are eligible to write the exam")
else:
    att=int(input("enter the attendance in percentge"))
    if att > 75:
        print("you are eligible to write the exam")
    else:
        print("you are not eligibe")