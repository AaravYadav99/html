dic1={
    'apple':2,
    'grapes':5,
    'orange':2,
    'star fruit':2,
}
k=2 
count=0
for key,value in dic1.items():
    if value==k:
        count+=1
print("the items which have frequency",k,'is' ,count)