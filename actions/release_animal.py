import os
from animals import RiverDolphin
from animals import Kikakapu
from animals import Gecko
from animals import Goose
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import Spider

def release_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
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

    try:
        if animal.fresh:
            habitat_list.extend(arboretum.rivers)
    except AttributeError:
        pass

    try:
        if animal.stagnant:
            habitat_list.extend(arboretum.swamps)
    except AttributeError:
        pass

    try:
        if animal.salty:
            habitat_list.extend(arboretum.coastlines)
    except AttributeError:
        pass

    try:
        if animal.mountain_bound:
            habitat_list.extend(arboretum.mountains)
    except AttributeError:
        pass

    try:
        if animal.grassland_bound:
            habitat_list.extend(arboretum.grasslands)
    except AttributeError:
        pass

    try:
        if animal.forest_bound:
            habitat_list.extend(arboretum.forests)
    except AttributeError:
        pass


    for index, habitats in enumerate(habitat_list):
        print(f'{index + 1}. {habitats.type} ({len(habitats.animals)} animals)')


    print("Release the animal into which biome?")
    choice = input("> ")

    if len(habitat_list[int(choice)-1].animals) < habitat_list[int(choice)-1].max_animals:
        habitat_list[int(choice)-1].animals.append(animal)
    else:
            print("**** That Biome is not large enough **** \n **** Please choose another one ****")
            for index, habitats in enumerate(habitat_list):
                print(f'{index + 1}. {habitats.type} ({len(habitats.animals)} animals)')

                print("Release the animal into which biome?")
                choice = input("> ")


    # for places in getattr(arboretum, habitat_list[int(choice) - 1].type):
    #     if places.id == habitat_list[int(choice) - 1].id:
    #         places.animals.append(animal)



