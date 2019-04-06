from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, kind, engine, speed):
        self.kind = kind
        self.engine = engine
        self.topspeed = speed
        self.age = 0

    def setAge(self, age):
        self.age = age

    def servicing(self):
        if self.age == 0:
            print("Your {} bike don't need servicing".format(self.kind))

        elif self.age > 0 and self.age <= 1:
            print('Your {} need to be serviced'.format(self.kind))

        else:
            print('Your {} is in emergency'.format(self.kind))
    def print_info(self):
        print("Your bike is {}, with engine power {} and topspeed = {} "
        .format(self.kind,self.engine,self.topspeed))
        self.servicing()

if __name__ == '__main__':
    # v = Vehicle("Car", 200, "Ba 1 ja 2015", color="red")
    # print(v.plate, "is the plate no")
    b = Bike('racing','400HP','300km/hr')
    b.setAge(1)
    b.print_info()
