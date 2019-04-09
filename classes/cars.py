"""
    Car is the derived class of Parent class Vehicle
    Car Object inherits all the properties of the Vehicle class

    Car class cosists of :

    *   Constructor __init__ takes 3 arguments:
            -   kind
            -   engine
            -   speed

    *   setage()
            - sets the age of the Car object

    *   servicing()
            -   Checks if age of the object
            -   Prints the suggestion regarding servicing

    *    print_info()
            -   prints the property of the object
"""

from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, name, price, plate, kind, engine, speed):
        super(Car, self).__init__(name, price, plate, kind=kind, engine=engine, speed=speed)
        self.age = 0

    def set_age(self, age):
        self.age = age

    def servicing(self):
        if self.age == 0:
            print("Your {} Car does not need servicing.".format(self.kind))

        elif self.age > 0 and self.age <= 1:
            print('Your {} needs to be serviced.'.format(self.kind))

        else:
            print('Your {} is in an emergency.'.format(self.kind))

    def print_info(self):
        print("Your Car is {}, with engine power {} and top speed = {}."
              .format(self.kind, self.engine, self.speed))
        self.servicing()

    def repair(self, parts):
        super(Car, self).repair(parts)
        for part in parts:
            print(part, "has been repaired.")


if __name__ == '__main__':
    b = Car("Car", 2200000, "Ba 1 JA 2015", 'racing', '800CC', '150km/hr')

    b.print_info()

    b.set_age(1)
    b.repair(['head light', 'tail light'])
