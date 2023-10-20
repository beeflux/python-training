from vehicle import Vehicle
class truck(Vehicle):
	def __init__(self,capacity,dist):
		Vehicle.__init__(self,"cargo",100000,"Ba 1 ja 2015",color="red")
		self.capacity = capacity
		self.dist = dist


	def distance(self):
		return self.dist

	def power(self):
		return 1000

	def wheeler(self):
		return 12
	
	def hydrolic(self):
		print("it has 1000 hertz hydrolic power")
	

if __name__ == '__main__':
	t = truck("weight is 999 kg",1000)
	print(t.name,"is the name")	
	print(t.plate, "is the plate no")
	print(t.repair("engine")," has been repaired")
	print(t.run(),"it is running")
	print(t.distance(),"km per day")
	print((t.capacity,"only accepts less than 1000 kg"))
	print(t.power()," hertz power")
	print(t.wheeler()," number of wheels")
	print(t.hydrolic())
