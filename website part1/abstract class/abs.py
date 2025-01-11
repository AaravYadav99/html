from abc import ABC,abstractmethod 
class ABCclass(ABC):
    def print1(self,x):
        print("passed value",x)
    @abstractmethod
    def task(self):
        pass
class test_class(ABCclass):
    def task(self):
        print("we are inside test_class")
obj1=test_class()
obj1.task()
obj1.print1(200)