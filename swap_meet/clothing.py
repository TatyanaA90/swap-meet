from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id=id, condition=condition)
        self.fabric = fabric
    
    def __str__(self): 
        item_message = super().__str__()
        clothing_message = f"It is made from {self.fabric} fabric."
        return " ".join((item_message,clothing_message))
