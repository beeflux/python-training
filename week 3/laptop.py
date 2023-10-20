class Laptop:
	def __init__(self,name,ram,graphics=None):
		self.name = name 
		self.ram = ram
		self.graphics = []
		self.ram = []
	def add_ram(self,ram):
		self.ram.append(ram)
	def add_graphics(self,graphics):
		self.graphics.append(graphics)
a=Laptop('Dell','32')
a.add_ram('16 gb')
print('laptop name is ',a.name)
print('ram is ',a.ram)
