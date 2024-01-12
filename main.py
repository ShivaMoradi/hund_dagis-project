# Skriva ut en lista på alla hundar
# Lägga till en ny hund
# Ta bort en existerande hund
# Editera informationen om en hund
# Checka in och ut hundar, så man vet vilka som är på plats.
import request
print(request.get_all_dogs())
# dog dictionary ska bygas
name = {"dog.name": ""}
age = {"dog.age": ""}
ras = {"dog.ras": ""}
color = {"dog.color": ""}
inchecked = {"dog.inchecked": ""}
contact_owner = {"dog.contact_owner": ""}


def get_all_dogs():
    dogs = []
    print("List of all dogs:")
    for dog in dogs:
        print(f"Name: {dog.name}")
        print(f"Age: {dog.age}")
        print(f"ras: {dog.ras}")
        print(f"Color: {dog.color}")
        print(f"Checked In: {'Yes' if dog.inchecked else 'No'}")
        print(f"Contact Owner: {dog.contact_owner}")
        print()


get_all_dogs()


def add_new_dog():
    myrun = True
    print("Add new dog")
    while myrun:
        dog_name = input("write your dog name: ")
        dog_age = int(input("write your dog age: "))
        dog_ras = input("write your dog ras:")
        dog_color: str = input("write your dog's color:")
        dog_inchecked = bool(input("Is your dog inchecked?"))
        dog_contact_owner = input("write your dog contact owner:")
        answers = input(f"name -> {dog_name}\n"
                        f"age -> {dog_age}\n"
                        f"ras -> {dog_ras}\n"
                        f"color -> {dog_color}\n"
                        f"inchecked -> {dog_inchecked}"
                        f"contact owner -> {dog_contact_owner}"
                        f"Is that ok? (y/n) or write Q to exit: ").strip().lower()
        if answers == "y":
            request.add_new_dog(name=dog_name, age=dog_age, ras=dog_ras, color=dog_color, inchecked = dog_inchecked,
                                contact_owner=dog_contact_owner)
            myrun = False
        elif answers == "q":
            myrun = False


add_new_dog()
myrun = False

import remove_dogs
remove_dogs.remove_dogs_by_id()
import edit_dogs
import checkIn_dogs

run = True
while run:
    answer = input("\nMeny\n"
                   "\n1. show a list of all dogs"
                   "\n2. add a new dog"
                   "\n3. delete a dog"
                   "\n4. edit an existing dog"
                   "\n5. checkIn dogs"
                   "\nQ. exit from program"
                   "\n-> ").strip()

    match answer.lower():
        case "1":
            get_all_dogs()
        case "2":
            add_new_dog()
        case "3":
            remove_dogs.remove_dogs_by_id(name, age, ras, color, inchecked, contact_owner)
        case "4":
            edit_dogs.edit_dogs_info(name, age, ras, color, inchecked, contact_owner)
        case "5":
            checkIn_dogs.inchecked()
        case "q":
            print("exit!")
            run = False
        case _:
            print(f"'{answer}' is not an alternativ, choose between 1-5 or Q!")
