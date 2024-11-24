try:
    n=int(input("enter the number"))
    print("the given no is",n)
except ValueError as e:
    print(e)