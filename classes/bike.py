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
    def __init__(self, name, price, plate, kind, engine, speed):
        super(Bike, self).__init__(name, price, plate, kind=kind, engine=engine, speed=speed)
        self.age = 0

    def set_age(self, age):
        self.age = age

    def servicing(self):
        if self.age == 0:
            print("Your {} bike does not need servicing.".format(self.kind))

        elif self.age > 0 and self.age <= 1:
            print('Your {} needs to be serviced.'.format(self.kind))

        else:
            print('Your {} is in an emergency.'.format(self.kind))

    def print_info(self):
        print("Your bike is {}, with engine power {} and top speed = {}."
              .format(self.kind, self.engine, self.speed))
        self.servicing()

    def repair(self, parts):
        super(Bike, self).repair(parts)
        for part in parts:
            print(part, "has been repaired.")


if __name__ == '__main__':
    b = Bike("Bike", 200, "Ba 1 JA 2015", 'racing', '400HP', '300km/hr')

    b.print_info()

    b.set_age(1)
    b.repair(['head light', 'tail light'])
