from bike import Bike

class PedalBike(Bike):
	def __init__(self, gear, backseat, height, color):
		self.gear = gear
		self.backseat = backseat
		self.height = height
		self.color = color

	def get_cycle_property(self):
		self.gear = int(input("No. of gear you want: "))
		self.backseat = input("Do you need backseat: ")
		self.height = int(input("Size of cycle height: "))
		self.color = input("Cycle Color: ")
		self.price()
		Bike.setAge(5)

	def price(self):
		if (self.gear>0) and (self.backseat == "YES" or "yes"):
			print(f"The Cycle with Gear {self.gear} price ranges from 10k to 100k")
		else:
			print("The Cycle costs price ranges from 10k to 50k")

	def brake(self):
		print("Front and Rear both has DiscBrake")

	def check_condition(self):
		print("Is in Condition")

if __name__ == '__main__':
	cycle1 = PedalBike(0, "YES", 0, "red")
	cycle1.get_cycle_property()
	# cycle1.price()
	cycle1.brake()
	cycle1.check_condition()