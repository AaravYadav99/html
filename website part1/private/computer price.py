class computer:
    def __init__(self):
        self._computerprice=1000
    def display(self):
        print("the computer price",self._computerprice)
    def setprice(self,price):
        self._computerprice=price

comp1=computer()
comp1.display()
comp1.setprice(1500)
comp1.display()