from cars import car

class Tata(car):
	def warranty(self):
		print("the warranty is provided already")

	def num_seat(self,numbers):
		print("the number of seats is:", numbers)

	def engine(self,engine):
		print("the car uses",engine,"engine")

if __name__ == '__main__':
	t = Tata()
	print(t.warranty())
	print(t.num_seat(5))
	print(t.engine("petrol"))
