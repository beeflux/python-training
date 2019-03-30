class Bird:

    def __init__(self, bird_class, bird_name, bird_type = None, bird_size = None,
                 beak = None, color = None, foot_type = None, habitat = None, 
                 locomotion_type = None, egg_size = None):
        self.bird_class = "Aves"
        self.bird_name = self.add_birds()
        self.habitat = self.add_habitats()
        self.food_type = self.add_foods()
        
    def add_birds(self):
        bird_name = input("Enter bird name: ")
        return bird_name
    
    def add_habitats(self):
        bird_habitats = input("Enter habitat: ")
        return bird_habitats
    
    def add_foods(self):
        food = input("Enter food: ")
        return food
    
    def can_fly(self):
        if (self.bird_name == "Penguin" or self.bird_name == "Ostrich" or self.bird_name == "Kiwi"):
            return True
        else:
            return False
    
    def get_food_type(self):
        food_type = input("Enter the food type: ")
        return food_type
    
    def get_bird_size(self):
        bird_size = input("Enter the bird size(big/small): ")
        return bird_size
    
    def disp(self):
        print("Bird name: ", self.bird_name, "Bird food: ", self.food_type)
        print("Bird habitat: ", self.habitat, "Locomotion type: ", self.locomotion_type)
    
bird_info = Bird()
bird_info.disp()
    
    
    
