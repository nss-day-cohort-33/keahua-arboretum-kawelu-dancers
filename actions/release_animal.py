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

    choice = input("Choose animal to release : ")

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

#this file is complex. It checks the inheritances of each Animal instance
# and approves the contents of various lists from the Keahua Arboretum (such as "self.river")
#to be added to a new list called "habitat_list".

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

#After the "habitat_list" is complete (meaning, after the user finishes creating new habitats to add to the list),
# the function below creates two NEW lists to help sort the values that are now stored in "habitat_list".
#The first list specifically functions as a counter of animal instances within habitat objects:

    if len(habitat_list) > 0:
        for index, habitats in enumerate(habitat_list):
            species_count = list()
            species_list = list()
            for species in habitats.animals:
                species_list.append(species.species)

#It goes into the ".animals" property on the "habitats" object and extracts that list.
# Then, it puts each animal that exists within the user-generated habitats (there are more than one!) into a new list
#so that the number of each kind can be counted (e.g. River Dolphin appears 5 times, there are 5 River Dolphins!)

            for animals in set(species_list):
                species_count.append(f"{str(species_list.count(animals))} {animals}")

#The loop over "animals in set(species_list)" is designed to combine our list of counted animals from "species_count"
# and the name of each type of animal while also eliminating repeats in the names of the animals. If there ARE 5 Dolphins, we don't want to
# say that 5 times in a row, we just need the word "Dolphin" and the number that represents the total number of Dolphins
# in any given habitat to appear for the user to see.

            print(f'{index + 1}. {habitats.type} ({", ".join(species_count) if len(habitats.animals) > 0 else "No animals here"})')
        print("Release the animal into which habitat?")
    else:
        print("There's no habitat for this animal!")

#The print statement above prints the index number + 1 (becasue no human wants to read a list that begins with "item 0" and
# prints the name of the type of habitat followed by "( joining of the species_count number and the corresponding name of the animal
#unless there is 0 animals in that habitat in which case it will print "No animals here".
# The same Print Statement - on a different line - also tells the user to choose a number to release the animal into one of the listed habitats.

    choice = input("> ")

    if len(habitat_list[int(choice)-1].animals) < habitat_list[int(choice)-1].max_animals:
        habitat_list[int(choice)-1].animals.append(animal)
    else:
            print("**** That Habitat is not large enough **** \n **** Please choose another one ****")
            for index, habitats in enumerate(habitat_list):
                print(f'{index + 1}. {habitats.type} ({len(habitats.animals)} animals)')

                print("Release the animal into which Habitat?")
                choice = input(": ")
#The If statement above dictates that the program should either add the user-chosen animal to the user-chosen habitat via the "habitat_list"
# or it should tell the user that the chosen habitat is full and cannot recieve anymore animals.
