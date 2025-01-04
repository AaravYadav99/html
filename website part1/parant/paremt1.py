class Person:
    def __init__(self,name1,id_number):
    
        self.name1 = name1
        self.id_number = id_number

    def dis(self):
        print("the person name is ",self.name1)
        
        print("the person id is ",self.id_number)
class Employee(Person):
    def __init__(self, name1, id_number, salary, post):
        Person.__init__(self,name1,id_number)
        self.salary = salary
        self.post = post
    def disedmp(self):
        Person.dis(self)
        print("the person salary is ",self.salary)
        print("the person post is ",self.post)
emp1=Employee("jack","2000","800000","engineer")
emp1.disedmp()


