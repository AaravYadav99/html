from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("I can crawl")
s=snake()
s.move()
h=human()
h.move()