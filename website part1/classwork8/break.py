str1=input("enter the string")
ch=input("enter the alphabet")
for i in str1:
    if i == ch:
        print(ch,"the alphabet is preset is",str1)
        break
else:
        print(ch,"the given alphabet is not present",str1)