import main

class EditDogs:
    def __init__(self,name, age, ras, color, inchecked, contact_owner ):
        self.name = name
        self.age = age
        self.ras = ras
        self.color = color
        self.inchecked = inchecked
        self.contact_owner = contact_owner
    def edit_dogs_info(self, name, age, ras, color, inchecked, contact_owner):
        print("Current Dog Information:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"ras: {ras}")
        print(f"Color: {color}")
        print(f"Checked In: {inchecked}")
        print(f"Contact Owner: {contact_owner}")
        answer = input("Do you want to edit? (y/n) or write Q to exit: ").lower()
        if answer.lower() == 'y':
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            ras = input("Enter new breed: ")
            color = input("Enter new color: ")
            inchecked = input("Is the dog checked in? (yes/no): ").lower() == "yes"
            contact_owner = input("Enter new contact owner: ")
        # Updated information
            print("\nUpdated Dog Information:")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"ras: {ras}")
            print(f"Color: {color}")
            print(f"Checked In: {inchecked}")
            print(f"Contact Owner: {contact_owner}")
            print("Editing confirmed.")
            main.run.main = False
        elif answer.lower() == 'n':
            print("Editing canceled.")
            main.run.main = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return name, age, ras, color, inchecked, contact_owner
    edit_dogs_info()