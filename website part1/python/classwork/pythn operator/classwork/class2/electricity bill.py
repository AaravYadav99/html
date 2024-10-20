unit=int(input("enter the units"))
if unit <=50:
   amt =unit * 2.60 + 25
elif unit <= 100:
    amt=(unit-50)* 3.20 +(50*2.60)+35
elif unit <= 200:
    amt=(unit-100)* 5.26 +(50*2.60)+(50*3.26)+45
else:
    amt=(unit-200) * 8.45 + (50 * 2.60) + (50 * 3.20) * (100 * 5.26) + (50 * 3.26) + (100 * 5.2) + 75
print("the electricity change is",amt)