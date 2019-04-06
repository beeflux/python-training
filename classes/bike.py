"""
    Bike is the derived class of Parent class Vehicle
    Bike Object inherits all the properties of the Vehicle class

    Bike class cosists of :

    *   Constructor __init__ takes 3 arguments:
            -   kind
            -   engine
            -   speed

    *   setage()
            - sets the age of the bike object

    *   servicing()
            -   Checks if age of the object
            -   Prints the suggestion regarding servicing

    *    print_info()
            -   prints the property of the object
"""


from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, kind, engine, speed):
        self.kind = kind
        self.engine = engine
        self.topspeed = speed
        self.age = 0

    def setage(self, age):
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
    v = Vehicle("Car", 200, "Ba 1 ja 2015", color="red")
    print("The plate no is {}".format(v.plate))
    b = Bike('racing','400HP','300km/hr')

    print(b.plate)
    b.setAge(1)
    b.print_info()
