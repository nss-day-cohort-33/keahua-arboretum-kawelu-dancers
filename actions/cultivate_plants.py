import os
from plants import Eucalyptus
from plants import Blue_Jade_Vine
from plants import Silversword
from plants import Apple_Tree

#This file does exactly the same thing as "release_animal" except for the plants available in the list on the Keahua instance of the Arboretum class.

def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Blue Jade Vine")
    print("4. Rainbow Eucalyptus Tree")

    choice = input("Choose a plant to cultivate : ")

    if choice == "1":
        plant = Apple_Tree()

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = Blue_Jade_Vine()

    if choice == "4":
        plant = Eucalyptus()

    habitat_list = []
#Just like in realease_animal, we create a "habitat_list" here and extend it with the lists of habitats
# that are being created on the Keahua Arboretum object.

    try:
        if plant.stagnant:
            habitat_list.extend(arboretum.swamps)
    except AttributeError:
        pass
#First, we take the chosen plant which is set to the empty parameter "plant" declared right after the
# opening function in this file, and, once the value of "plant" is established, the program checks to see what
#properties that plant contains (e.g."stagnant" which equates to placing that plant in to the "swap" habitat
# list on the Keahua Arboretum object).

    try:
        if plant.mountain_bound:
            habitat_list.extend(arboretum.mountains)
    except AttributeError:
        pass

    try:
        if plant.grassland_bound:
            habitat_list.extend(arboretum.grasslands)
    except AttributeError:
        pass

    try:
        if plant.forest_bound:
            habitat_list.extend(arboretum.forests)
    except AttributeError:
        pass

    if len(habitat_list) > 0:
        for index, habitats in enumerate(habitat_list):
            plant_list = list()
            plant_count = list()

#When it has the habitats captured, it generates two lists to separate the number of each created plant type
# from the name of the type of plant.
#Then, it prints the necessary information (joined) or it informs the user that they selected a habitat that has no plants yet.

            for species in habitats.plants:
                plant_list.append(species.species)

            for plants in set(plant_list):
                plant_count.append(f"{str(plant_list.count(plants))} {plants}")

            print(f'{index + 1}. {habitats.type} ({", ".join(plant_count) if len(habitats.plants) > 0 else "No plants here"})')
            print("Release the plant into which habitat?")

    else:
        print("There is no habitat for this plant!")

#There is also a catch here for in case the user tries to select a plant for which no suitible habitat has been created on the Keahua Arboretum object.

    choice = input(": ")

    if len(habitat_list[int(choice)-1].plants) < habitat_list[int(choice)-1].max_plants:
        habitat_list[int(choice)-1].plants.append(plant)
    else:
            print("**** That Habitat is not large enough **** \n **** Please choose another one ****")
            for index, habitats in enumerate(habitat_list):
                print(f'{index + 1}. {habitats.type} ({len(habitats.plants)} plants)')

#And there is a warning for "this habitat is full / can't take any more plants" and another print function
# to allow them to select a totally different plant.

                print("Release the plant into which Habitat?")
                choice = input(": ")


    # for places in getattr(arboretum, habitat_list[int(choice) - 1].type):
    #     if places.id == habitat_list[int(choice) - 1].id:
    #         places.plants.append(plant)



