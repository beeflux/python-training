class car:
    no_of_doors = 4
    gear = [-1, 0, 1, 2, 3, 4, 5]
    seats = 4

    def accelerate(self):
        if gear == 0:
            print("car at neutral")
