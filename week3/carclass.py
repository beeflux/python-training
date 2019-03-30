class car:
	#Constructor with arguments manufacture name, model number, price and color
	def __init__(self, manuname,modelno,price,color):
        	self.manuname = manuname
		self.modelno = modelno
		self.price = price
		self.color = color
        	self.properties = []
	#adds the properties to the instance of the class car
	def add_properties(self,properties):
		self.properties.append(properties)
	
    	def run(self):
        	print("I can run 140 km/hrs in max")
	def warrenty(self):
        	print("I got no warranty")
	def servicing(self):
        	print("servicing is free of cost!! servie your car every 1 year")

#object newcar is created
newcar = car('ford',3434,20000,'black')
#object newcar1 is created
newcar1 = car('ford',3982,20000,'white')
#method add_properties is called with the parameter "power stereing"
newcar.add_properties('power stereing')

print("properties of car ", newcar.manuname,"are", newcar.properties)
newcar.run()
newcar.warrenty()
newcar.servicing()
