from aocutils import get_raw

def problem1():
    all_ingredients = []
    allergens = identify_ingredients(all_ingredients)
    ingredients = set(allergens.keys())
    return len([ing for ing in all_ingredients if ing not in ingredients])

def problem2():
    allergens = identify_ingredients([])
    ingredients = list(allergens.keys())
    return ','.join(sorted(ingredients, key=lambda ing: allergens[ing]))

def identify_ingredients(all_ingredients):
    lines = get_raw(21).splitlines()
    labels = {}
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        all_ingredients += ingredients
        ingredients = set(ingredients)
        allergens = allergens[:-1].split(', ')
        for allergen in allergens:
            if allergen not in labels:
                labels[allergen] = ingredients.copy()
            else:
                labels[allergen] &= ingredients
    confirmed = set()
    allergens = {}
    while len(confirmed) < len(labels):
        for allergen in labels:
            if len(labels[allergen]) == 1:
                ingredient = labels[allergen].pop()
                confirmed.add(ingredient)
                allergens[ingredient] = allergen
            else:
                labels[allergen] -= confirmed
    return allergens