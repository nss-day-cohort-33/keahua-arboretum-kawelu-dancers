from animals import RiverDolphin
from animals import Kikakapu
from animals import Gecko
from animals import Goose
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import Spider

def release_animal(arboretum):
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")

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

    habitat_list = []


    if animal.fresh:
        habitat_list.extend(arboretum.rivers)


    if animal.stagnant:
        habitat_list.extend(arboretum.swamps)
        


    # for habitat_list:

    for index, habitats in enumerate(habitat_list):
        print(f'{index + 1}. {habitats.type} {habitats.id}')





    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)


