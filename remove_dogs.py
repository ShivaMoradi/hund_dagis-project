import main
def remove_dogs_by_id(name, age, ras, color, inchecked, contact_owner):
    print("Current Dog Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"ras: {ras}")
    print(f"Color: {color}")
    print(f"Checked In: {inchecked}")
    print(f"Contact Owner: {contact_owner}")
    answer = input("Do you want to remove the dog? (y/n) or write Q to exit: ").lower()
    if answer == "y":
        print("dog removed")
        main.run.main = False
    else:
        print("exit without removing")
        main.run.main = False
remove_dogs_by_id()