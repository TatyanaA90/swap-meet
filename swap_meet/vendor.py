class Vendor:
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

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)

    
    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if item.get_category() == category.capitalize():
                items_in_category.append(item)

        return items_in_category
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)

        if not items_in_category:
            return None
        
        best_item = items_in_category[0]
        for item in items_in_category:
            if item.condition > best_item.condition:
                best_item = item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)
