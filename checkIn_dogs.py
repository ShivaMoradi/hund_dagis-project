import main

class CheckInDogs:
    def __init__(self, name, age, ras, color, inchecked, contact_owner):
        self.name = name
        self.age = age
        self.ras = ras
        self.color = color
        self.inchecked = inchecked
        self.contact_owner = contact_owner
    def check_dogs(self, name, age, ras, color, inchecked, contact_owner):
        print(f"List of all dogs: {main.get_all_dogs()}")

        inchecked = True
        while inchecked:
            print(f"dog is checked:")

