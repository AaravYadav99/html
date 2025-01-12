class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a<other.a:
            return "obj1 is less than obj2"
        else:
            return "obj2 is less than obj1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "obj1 is equal to obj2"
        else:
            return "obj2 is not equal than obj1"
obj1=A(32)
obj2=A(234)
print("the passed value",obj1.a,obj2.a)
print(obj1 <obj2)
print(obj1==obj2)
    
    
        
        