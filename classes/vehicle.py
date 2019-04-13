"""
    *   Vehicle is the parent class
<<<<<<< HEAD
=======

>>>>>>> a813a2cfe877af7aaa4153b426e0397b1361062f
    *   Construct __init__ takes 3 arguments
            -   name (sets name of the vehicle)
            -   price (sets the price of the vehicle)
            -   key value items (sets the dictionary items)
<<<<<<< HEAD
=======

>>>>>>> a813a2cfe877af7aaa4153b426e0397b1361062f
    *    Python setattr is used to set the dynamic value for the object
    *    Comprises of functions:
            -   run()
                    => prints "running"
            -   repair()
                    => access the part from the parts
                    => prints the repairing
"""

class Vehicle:
    def __init__(self, name, price, plate, **kwargs):
        self.name = name
        self.price = price
        self.plate = plate

        for k, v in kwargs.items():
            setattr(self, k, v)

    def run(self):
        print("running")

    def repair(self, parts):
        for part in parts:
            print("repairing ", part)
 


if __name__ == '__main__':
    v = Vehicle("Car", 200, "Ba 1 ja 2015", color="red")
    print(v.plate, "is the plate no")
