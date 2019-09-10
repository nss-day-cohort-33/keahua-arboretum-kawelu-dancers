import os
from plants import Eucalyptus
from plants import Blue_Jade_Vine
from plants import Silversword
from plants import Apple_Tree

def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Blue Jade Vine")
    print("4. Rainbow Eucalyptus Tree")

    choice = input("Choose a plant to cultivate > ")

    if choice == "1":
        plant = Apple_Tree()

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = Blue_Jade_Vine()

    if choice == "4":
        plant = Eucalyptus()

    habitat_list = []

    try:
        if plant.stagnant:
            habitat_list.extend(arboretum.swamps)
    except AttributeError: 
        pass

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



    # for habitat_list:

    for index, habitats in enumerate(habitat_list):
        print(f'{index + 1}. {habitats.type} ({len(habitats.plants)} plants)')

    print("Release the plant into which habitat?")
    choice = input("> ")

    if len(habitat_list[int(choice)-1].plants) < habitat_list[int(choice)-1].max_plants:
        habitat_list[int(choice)-1].plants.append(plant)
    else:
            print("**** That Biome is not large enough **** \n **** Please choose another one ****")
            for index, habitats in enumerate(habitat_list):
                print(f'{index + 1}. {habitats.type} ({len(habitats.plants)} plants)')





                print("Release the plant into which biome?")
                choice = input("> ")


    # for places in getattr(arboretum, habitat_list[int(choice) - 1].type):
    #     if places.id == habitat_list[int(choice) - 1].id:
    #         places.plants.append(plant)



