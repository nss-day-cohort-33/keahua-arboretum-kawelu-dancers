import os
from animals import RiverDolphin
from animals import Kikakapu
from animals import Gecko
from animals import Goose
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import Spider

def feed_animal():
    os.system('cls' if os.name == 'nt' else 'clear')
    animal = None

#When the user selects 3 from the main menu, this list appears.
# Unlike our other action files, this one does NOT get the Keahua Arboretum passed into it.
#That's becasue this action does not need to access any of the properties in the Arboretum class.

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to feed : ")

    if choice == "1":
        animal = Gecko(12)

    if choice == "2":
        animal = RiverDolphin(12)

    if choice == "3":
        animal = Goose(12)

    if choice == "4":
        animal = Kikakapu(12)

    if choice == "5":
        animal = Pueo(12)

    if choice == "6":
        animal = Ulae(12)

    if choice == "7":
        animal = Opeapea(12)

    if choice == "8":
        animal = Spider(12)

#When an animal is chosen to be fed, the program takes the prey that belong to the chosen animal class (via
# the ".prey") method/function that exists on that specific animal and EXTENDS the "food_list" to include
#the strings of food found insie that ".prey" function.

    food_list = list()

    try:
        if animal.prey:
            food_list.extend(animal.prey)
    except AttributeError:
        pass

    for index, food in enumerate(food_list):
        print(f'{index + 1}. {food}')

    print("What do you want to feed it?")
    choice = input(": ")

#The "animal.feed" action goes into the imported file that belongs to the chosen animal
# and accesses the function called "feed" so that this file will print "The {chosen animal} ate the {specified food} for a meal!"

    animal.feed(food_list[int(choice)-1])
    choice = input(": ")