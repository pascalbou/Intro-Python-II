# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, is_light = True):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.items = []

    def describe(self, lamp = False):
        if self.is_light or lamp:
            print(f'You are at {self.name}')
            print(self.description)
            self.check()
        else:
            print(f'It is too dark. You cannot see anything. Find a source of light.')

    def check(self):
        print(f'Items in this room : {self.items}')

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)       