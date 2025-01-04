class Vehicle:
    def __init__(self,  max_speed, mileage):
        
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("the mileage is",self.mileage)
        print("the maxspeed is",self.max_speed)
        



class Bus(Vehicle):
    pass
schoolbus=Bus(30,120)
schoolbus.display()

   





