"""
	Here is simple example of Inheritance, where we import Bike
	from file bike and used the property of class Bike into Pedalcycle

	Here is the class PedalBike and is the child of class Bike
"""

from bike import Bike
from vehicle import Vehicle

class PedalBike(Bike, Vehicle):
	#initializing the default value
	def __init__(self, gear, backseat, height, color):
		self.gear = gear
		self.backseat = backseat
		self.height = height
		self.color = color

	#it asks user to import all property he/she wants in his cycle
	def get_cycle_property(self):
		self.gear = input("Need Gear in cycle (y/n): ")
		self.backseat = input("Do you need backseat (y/n): ")
		self.height = int(input("Size of cycle height: "))
		self.color = input("Cycle Color: ")
		self.price()
		Bike.setAge(self, 5)

	#according to the user's demand it shows up the price
	def price(self):
		if (self.gear.lower()=='y'):
			if (self.backseat.lower() == "y"):
				print("\t\t\t\tPrice of bicycle: 10,000\n\n")
			else:
				print("\t\t\t\tPrice of bicycle: 8,000\n\n")
		else:
			print("\t\t\t\t\tPrice of bicycle: 5,000\n\n")

	#condition to check whether the bicycle has disc brake or not
	def brake(self):
		self.brake = input("Do you want Disc Brake in both front and rear(y/n): ")
		if (self.brake.lower() == 'y'):
			print("You need to pay additional 2000 for it: ")
		else:
			print("Ok:):)")

if __name__ == '__main__':
	cycle1 = PedalBike(0, "YES", 0, "red")
	cycle1.get_cycle_property()
	# cycle1.price()
	cycle1.brake()