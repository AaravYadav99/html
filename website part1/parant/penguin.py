class Bird:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def fly(self):
        print(f"{self.name} is flying.")

    
    def make_sound(self):
        print(f"{self.name} is chirping.")



class Sparrow(Bird):
   
    def __init__(self, name, color, size):
       
        super().__init__(name, color)
        self.size = size

    def hop(self):
        print(f"{self.name} is hopping around.")

    def display_details(self):
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}")



sparrow = Sparrow("Jack", "Brown", "Small")


sparrow.fly()             
sparrow.make_sound()      
sparrow.hop()             
sparrow.display_details() 