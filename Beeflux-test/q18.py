"""Q18
Create a class Building 
Create Appartment, House  and Commercial Building class inheriting Building class.
"""

class Building:
  def __init__(self,storey):
    print("Building")
    self.storey = storey

  def storey(self):
    return f"{self.storey} storey"

  def greet(self):
    return f"I got {self.storey} which is the Tallest in my area"



class Appartment(Building):
  def __init__(self,number):
    print("Appartment")
    self.number = number

  def flat_no(self):
    return f"{self.number} is my flat_no"

  def greet(self):
    return f"My flat number {self.number} is lucky to me"



class House(Building):
  def __init__(self,name):
    print("House")
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)



buld = Building(34)
app = Appartment(3345)
house = House("Sweet Home")

print(house.storey())
print(app.flat_no())
print(house.greet())
























