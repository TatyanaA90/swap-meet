import uuid
class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid1().int if id is None else id
        self.condition = condition
    
    def get_category(self):
        return self.__class__.__name__ 

    def __str__(self): 
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        descriptions = {
            0: "Mint-fresh off the shelf, no signs of use.",
            1: "Like new - just a hint of use, almost perfect.",
            2: "Gently used—shows light signs of wear.",
            3: "Well-worn-used, but still good.",
            4: "Heavily used—lots of wearand tear, but it still works like a charm.",
            5: "You probably want a glove for this one..."
        }

        return descriptions.get(self.condition, "Unknown condition")
