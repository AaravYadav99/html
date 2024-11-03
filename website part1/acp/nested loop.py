num=int(input("enter the number"))
print(num)
str1=str(num)
len=len(str1)
if len%2 == 0:
    mid=int(len/1)-1
else:
    mid=int(len/2)

midproduct=int(str1[mid]) * int(str1[mid+1])
print("the mid product is",midproduct)