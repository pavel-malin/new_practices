import collections


def add_animal_in_family(species, animal, family):
    if family not in species:
        species[family] = set()
    species[family].add(animal)


species = {}
add_animal_in_family(species, 'cat', 'felidea')


# Faster execution


def add_animal_in_family_c(species, animal, family):
    species[family].add(animal)


species = collections.defaultdict(set)
add_animal_in_family_c(species, 'cat', 'felidea')
