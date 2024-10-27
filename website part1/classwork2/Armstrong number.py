num=int(input("enter the number"))

sum=0
temp=num
while temp>0:
    dig=temp%10
    sum=sum+dig**3
    temp=temp//10
if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")
