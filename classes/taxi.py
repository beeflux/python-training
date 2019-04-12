from vehicle import Vehicle
class Taxi(Vehicle):
	def __init__(self,seats,offroad):
		self.seats = seats
		self.offroad = offroad
		Vehicle.__init__(self,"cargo",100000,"Ba 1 ja 2015",color="red")
	def warrenty(self):
		print("I got no warranty")
	def petrol_diesel(self):
		print("Petrol engine")
if __name__ == '__main__':
	t = Taxi(4,"offroad")
	print("name is: ",t.name)
	print(t.run())
	print(t.repair("engine"))
	print(t.warrenty())
	print("no. of seats = ",t.seats)
	print(t.petrol_diesel())


