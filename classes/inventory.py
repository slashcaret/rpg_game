from classes.game import Person

class Item:
    
    def __init__(self,name,type,description,prop):
        self.name=name
        self.type=type
        self.description=description
        self.prop=prop
        
    def generate_item_effect(self):
        print(self.description)
        
