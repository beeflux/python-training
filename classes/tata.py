
from vehicle import Vehicle
class Tata(Vehicle):
	def __init__(self,price):
		self.price = price
	def warrenty(self):
		print("the warranty is provided")
	def getPrice(self):
		return self.price
if __name__ == '__main__':
	t = Tata(1000)
	print(t.run())
	print(t.repair("engine"))
	print(t.warrenty())
	print(t.getPrice())

