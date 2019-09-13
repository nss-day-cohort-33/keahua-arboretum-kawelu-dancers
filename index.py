import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.cultivate_plants import cultivate_plant
from actions.feed import feed_animal

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

#this is a creation of an Arboretum. It's being named and given an address here.
#Because this Arboretum exists inside THIS file, it is passable to the actions files
# without any importing of an Arboretum inside those files.
#That's why in "release_animal", for example, we are able to use
# properties that exist on our keahua Arboretum class.

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ \n\033[1;31;40m| K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  | \033[1;37;40m\n+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

#each of these buttons tells Python to EXECUTE that "action" from the "actions" directory.
# The "annex_habitat" action takes a parameter "arboretum" on the other end. Here, we are passing
#it our lovely little instance of the Arboretum class, Keahua, so that in the "annex_habitat"
# action file we can actually add items to the Keahua object.

    if choice == "2":
        release_animal(keahua)

#also note that the imports into this file are the action files and their functions
# which will be activated via this main menu.

    if choice == "3":
        feed_animal()

#For example, when the user types "3" and hits "enter," this "index.py" file executes the "feed_animal" function.
#Feed_Animal immediately generates it's own menu of options for the user.

    if choice == "4":
        cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)

    if choice != "6":
        main_menu()

main_menu()
