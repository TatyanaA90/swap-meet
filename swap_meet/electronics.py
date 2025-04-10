from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id=id, condition=condition)
        self.type = type
    
    def __str__(self): 
        item_message = super().__str__()
        electronics_message = f"This is a {self.type} device."
        return " ".join((item_message,electronics_message))
