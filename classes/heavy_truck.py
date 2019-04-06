

from vehicle import Vehicle
   
"""
    *   HeavyTruck is the child class inherited from class Vehicle
    *   Construct __init__ takes 3 arguments
            -   company (sets name of the Heavy Truck company)
            -   weight (sets the weight of the Heavy Truck)
            -   capacity_load (sets the capacity of the truck to carry loads)
    *    Comprises of functions:
            -   cover_distance()
                    => prints the distance covered by the truck
            -   carry_load()
                    => prints the amount of load the truck is carrying
"""
         
class HeavyTruck(Vehicle):
    
    def __init__(self, company,weight,capacity_load):
        self.company = company
        self.weight = weight
        self.capacity_load = capacity_load
        
    def cover_distance(self,distance):
        print("covers the distance : ",distance,' miles')
        
    def carry_load(self,load):
        print("the heavy truck is carrying load : ", load, " tons")
        
    

if __name__ == '__main__':
    v = Vehicle("Heavy Truck", '$20000000', "Ba 1 ja 2015", color="red")
    print(v.plate, "is the plate no")
    print(v.name , "is the name")
    print(v.price, " is the price")
    print(v.color , "is the color")
    
    truck = HeavyTruck('TATA','1000kg','2000 kg')
    print(truck.company, 'is the company')
    print(truck.weight, ' is the weight')
    print(truck.capacity_load, ' is the capacity of carrying load')
    truck.cover_distance(5000)
    truck.carry_load(0.5)
    