def cube(x):
    return x**3
def bythree(x):
    if x%3 == 0:
        print("cube of",x,"is",cube(x))
    else:
            print(x,"the number is not divided by three")
x=int(input("enter the number"))
bythree(x)