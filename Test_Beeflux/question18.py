'''

  Q18
Create a class Building 
Create Appartment, House
and Commercial Building class inheriting Building class.

'''

class Building :
    def __init__(self, color, stories, model,windows,doors, **kwargs):
        self.color = color
        self.stories = stories
        self.model = model
        self.windows= windows
        self.doors= doors
        
    def opengate(self):
        print(" gate opened")


class Apparment(Building):
    def __init__(self,no_of_flats, **kwargs):
        self.no_of_flats = no_of_flats
        

class House(Building):
    def __init__(self,no_of_familymember, **kwargs):
        self.no_of_familymember = no_of_familymember
        

class Commercial_Building(Building):
    def __init__(self,type_of_business, **kwargs):
        self.type_of_business = type_of_business

if __name__ == '__main__':
    v = Building("White", 4, "pillar_system", 62, 10)
    print('The building has',v.windows,"windows")
    v.opengate()






    
