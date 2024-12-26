l1=[1,2,3,4]
l2=[100,200,300,400]
l3=zip(l1,l2)
print(list(l3))
for(x,y) in zip(l1,l2[::-1]):
    print(x,y)
l3=zip(l1,l2[::-1])
print(list(l3))
stock = ["reliance",'infosys','truecaller']
price=[1213,3223,3434,]
dic1={stock:price for stock,price in zip(stock,price)}
print(list(dic1))