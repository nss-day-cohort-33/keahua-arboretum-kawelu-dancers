def build_facility_report(arboretum):

#This file is actually quite simple, it's purpose is to print to the console the IDs of each
# object created in our Arboretum.
#For every river, for example, in Arboretum's River list, print the word "River" and
# print eight characters from the ID number that belongs to each individual river.
#It does the same for all plants and animals within each of those habitats / Arboretum lists of objects.

    for river in arboretum.rivers:
        print(f'River [{str(river.id)[:8]}]')
        for animal in river.animals:
            print(f'\t {animal.species} [{str(animal.id)[:8]}]')
        for plant in river.plants:
            print(f'\t {plant.species} [{str(plant.id)[:8]}]')

    for grassland in arboretum.grasslands:
        print(f'Grassland [{str(grassland.id)[:8]}]')
        for animal in grassland.animals:
            print(f'\t {animal.species} [{str(animal.id)[:8]}]')
        for plant in grassland.plants:
            print(f'\t {plant.species} [{str(plant.id)[:8]}]')

    for swamp in arboretum.swamps:
        print(f'Swamp [{str(swamp.id)[:8]}]')
        for animal in swamp.animals:
            print(f'\t {animal.species} [{str(animal.id)[:8]}]')
        for plant in swamp.plants:
            print(f'\t {plant.species} [{str(plant.id)[:8]}]')

    for mountain in arboretum.mountains:
        print(f'Mountain [{str(mountain.id)[:8]}]')
        for animal in mountain.animals:
            print(f'\t {animal.species} [{str(animal.id)[:8]}]')
        for plant in mountain.plants:
            print(f'\t {plant.species} [{str(plant.id)[:8]}]')

    for coastline in arboretum.coastlines:
        print(f'Coastline [{str(coastline.id)[:8]}]')
        for animal in coastline.animals:
            print(f'\t {animal.species} [{str(animal.id)[:8]}]')
        for plant in coastline.plants:
            print(f'\t {plant.species} [{str(plant.id)[:8]}]')

    for forest in arboretum.forests:
        print(f'Forest [{str(forest.id)[:8]}]')
        for animal in forest.animals:
            print(f'\t {animal.species} [{str(animal.id)[:8]}]')
        for plant in forest.plants:
            print(f'\t {plant.species} [{str(plant.id)[:8]}]')

    input("\n\nPress any key to continue...")