class employee:
    def __init__(self,name):
        print("object intiated")
        self.name=name
    def intro(self):
        print("i am",self.name)
    def __del__(self):
        print("object deleted")
emp1=employee("john")
emp1.intro()
del emp1

    