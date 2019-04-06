class Student:
	def __init__(self):
		self.id = 1
		self.physics = "A"
		self.chemistry = "A"
		self.math = "A"
	def result(self):
		if (self.marks < 70 and self.marks > 60):
			print("You Passed Your Exam with First Division")
		elif (self.marks > 70):
			print("You Passed Your Exam with Distinction")
		else:
			print("You are upgraded")

	def get_record(self):
		self.id = int(input("Student Symbol No: "))
		self.physics = int(input("Physics: "))
		self.chemistry = int(input("Chemistry: "))
		self.math = int(input("Mathmatics: "))
	def storing_record(self):
		with open('record.xlsx','a') as file:
			file.write(f'{self.id}\t')
			file.write(' ')
			file.write(' ')
			file.write(f'{self.physics}\t')
			file.write(f'{self.chemistry}\t')
			file.write(f'{self.math}\t\n')


no_of_student = int(input("Number of Total Students: "))
i = 1
while(i<=no_of_student):
	print(f"Enter the Detail of Student {i}")
	s1 = Student()
	s1.get_record()
	s1.storing_record()
	i += 1
with open('record.txt', 'r') as file:
	f = file.read()
	print(f)
