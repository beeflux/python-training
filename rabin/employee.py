class Employee:
 
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
           

    def add_age(self):
        x=int(input("enter the age:"))
        self.age=x
        print("new age is:",self.age)
   
d=Employee('Rabin',15,'chunikhel')
d.add_age()
  
        
  
