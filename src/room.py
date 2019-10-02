# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = ['sword', 'shield']

    def describe(self):
        print(f'You are at {self.name}')
        print(self.description)

    def check(self):
        print(f'Items in this room : {self.items}')
