# # Skriva ut en lista på alla hundar
# # Lägga till en ny hund
# # Ta bort en existerande hund
# # Editera informationen om en hund
# # Checka in och ut hundar, så man vet vilka som är på plats.
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword",
    database="Hund_dagis"
)
cursor = database.cursor(dictionary=True)


def get_all_dogs():
    cursor.execute("SELECT * FROM dogs")
    return cursor.fetchall()


def add_new_dog_db(name, age, ras, color, inchecked, contact_owner):
    cursor.execute(f"INSERT INTO dogs (name, age, ras, color,inchecked,contact_owner)"
                   f"VALUES ('{name}', {age}, '{ras}', '{color}', {inchecked}, '{contact_owner}')")
    database.commit()


def remove_dogs_by_id():
    cursor.execute(f"DELETE FROM dogs WHERE dogs.id")
    database.commit()


def edit_dogs_info():
    cursor.execute(f"update Hund_dagis.dogs")
    database.commit()


def checkin_dogs():
    cursor.execute(f"SELECT inchecked FROM dogs")
