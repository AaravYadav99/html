class Bird:
    # Constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Method 1
    def fly(self):
        print(f"{self.name} is flying.")

    # Method 2
    def make_sound(self):
        print(f"{self.name} is chirping.")


# Child class inheriting from Bird
class Sparrow(Bird):
    # Constructor using super to call parent constructor
    def __init__(self, name, color, size):
        # Call the parent class constructor
        super().__init__(name, color)
        self.size = size

    # Method 1
    def hop(self):
        print(f"{self.name} is hopping around.")

    # Method 2
    def display_details(self):
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}")


# Create an instance of Sparrow
sparrow = Sparrow("Jack", "Brown", "Small")

# Access parent and child methods
sparrow.fly()             # Inherited method
sparrow.make_sound()      # Inherited method
sparrow.hop()             # Child method
sparrow.display_details() # Child method