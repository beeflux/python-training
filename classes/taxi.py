from vehicle import Vehicle
class Taxi(Vehicle):
	def __init__(self,price):
		self.price = price
	def warrenty(self):
		print("I got no warranty")
	def getPrice(self):
		return self.price
if __name__ == '__main__':
	#v = Vehicle("Car", 200, "Ba 1 ja 2015", color="red")
	#print(v.plate, "is the plate no")

t = Taxi(1000)
print(t.run())
print(t.repair("engine"))
print(t.warrenty())
print(t.getPrice())

