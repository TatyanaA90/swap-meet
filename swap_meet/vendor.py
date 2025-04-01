class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_id(self, id):

        for item in self.inventory:
            if item.id == id:
                return item
        return None


    def swap_items(self, other_vendor, my_item, their_item):
        if not self.remove(my_item):
            return False

        if not other_vendor.remove(their_item):
            self.add(my_item)
            return False
        
        other_vendor.add(my_item)
        self.add(their_item)

        return True

