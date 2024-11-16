def totalamt(amt):
    total=amt + (amt*10)/100
    return total
amt=float(input("enter the amount for the bill"))
print("the total amt is",totalamt(amt))