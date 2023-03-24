import items
class Player:
    def __init__(self):
        self.usable = []
        self.unusable = []
        self.inventory = [self.usable, self.unusable]
        self.key = []
        self.heart = 7
        self.extra_strength = 0
        self.extra_weakness = 0

    def add_usable(self, item):
        self.usable.append(item)

    def add_unusable(self, item):
        self.unusable.append(item)

    def use(self, item):
        for usable_item in self.usable:
            if usable_item == item:
                items[usable_item]
                self.usable.remove(usable_item)

    def add_key(self, key):
        self.key.append(key)

    def add_heart(self, number):
        self.heart += number