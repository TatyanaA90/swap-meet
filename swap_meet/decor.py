from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id=id, condition=condition)
        self.width = width
        self.length = length
    
    def __str__(self): 
        item_message = super().__str__()
        decor_message = f"It takes up a {self.width} by {self.length} sized space."
        return " ".join((item_message,decor_message))
