class IOString:
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("enter the string")
    def pring_string(self):
        print("enter upper is",self.str1.upper())
obj1=IOString()
obj1.get_string()
obj1.pring_string()

        