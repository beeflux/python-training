import random
from vehicle import Vehicle
from bike import Bike

class Motorbike(Bike):

    def __init__(self, numberplate):
        self.numberofwheels = 2
        self.numberplate =  numberplate
        self.gear = [y for y in range(6)]
        self.clutch  = [1, 0]
        self.brake = [1, 0]
        self.speed = [x+10 for x in range(201)]
    
    def run(self):
        # for i in range(random.randint(0, 6)):
        gear = random.randint(0, 5)
        if gear == 0:
            print("Your bike is at neutral and you are at rest.")
        elif gear == 1:
            print("Your speed must be in beween 0 and 30")
        elif gear == 2:
            print("Your speed must be in beween 30 and 60")
        elif gear == 3:
            print("Your speed must be in beween 60 and 90")
        elif gear == 4:
            print("Your speed must be in beween 90 and 120")
        elif gear == 5:
            print("Your speed must be in beween 120 and 150. Slow down !!!")
        
        

        