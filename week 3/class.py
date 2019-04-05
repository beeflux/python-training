class College:
	def __init__(self, name, address, course):

		self.name = name
		self.address = address
		self.course = []
	
	def add_course(self, course):
		self.course.append(course)

c = College("college of applied bussiness","chhabahil",[])
d = College("st xavier college","chhabahil",[])

c.add_course("csit")
d.add_course("BBA")

print(c.course)
print(d.course)




		
