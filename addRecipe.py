import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'myRecipes.settings')

import django
django.setup()

from book.models import Recipe, Ingredient, Measurement, Note, Icon


# For each file in recipeFiles dir, check if title already exists. If not, create it!
cwd = os.getcwd()
recipe_dir = cwd + "\\recipeFiles"
filenames = os.listdir(recipe_dir)
for filename in filenames:
    path = recipe_dir + "\\" + filename
    with open(path) as f:
        contents = f.read().splitlines()
    f.close()
    # Get all recipe info
    recipe_title = contents[0].split(":")[1]
    recipe_source = contents[1].split(":")[1]
    recipe_url = contents[2][11:]
    icon_name = contents[4].split(":")[1]
    icon_code = contents[5].split(":")[1]    
    print("ONE")
    existing = Recipe.objects.all().filter(title=recipe_title).first()
    if existing:
        break
    steps_text = ""
    for i in range(8, len(contents)):
        step = contents[i]
        if step:
            if step[0] != "-":
                break
        if i == 8:
            steps_text += step[1:]
        else:
            steps_text += "+" + step[1:]
    steps = steps_text[:-1]
    ingredients = []
    measurements = []
    ingredient_start_index = 0
    for line in contents:
        if line != "Ingredients:":
            ingredient_start_index += 1
        else:
            break
    print("TWO")
    ingredient_start_index += 1
    # NEED TO HANDLE INGREDIENTS AND MEASUREMENTS BETTER (1 4-oz can green chiles, 1 white onion (NO UNIT!), 4 tsp butter)
    for i in range(ingredient_start_index, len(contents)):
        # split ingredient from quantity and measurement
        ing_qty_unit = contents[i].split(":")
        ingredient = ing_qty_unit[0][1:]
        qty_unit = ing_qty_unit[1].split()
        quantity = qty_unit[0]
        if len(qty_unit) == 1:
            unit = ""
        elif len(qty_unit) > 1:
            glue = " "
            unit = glue.join(qty_unit[1:])
        ingredients.append(ingredient)
        measurements.append(quantity + " " + unit)
    # Populate database
    ingredient_objects = []
    for ingredient in ingredients:
        # Check if it already exists
        i = Ingredient.objects.all().filter(name=ingredient).first()
        if not i:
            new_ing = Ingredient(name=ingredient)
            new_ing.save()
            ingredient_objects.append(new_ing)
        else:
            ingredient_objects.append(i)
    icon = Icon.objects.all().filter(code=icon_code).first()
    if not icon:
        icon = Icon(name=icon_name, code=icon_code)
        icon.save()
    print("THREE")
    new_recipe = Recipe(
        title = recipe_title,
        source = recipe_url,
        sourceName = recipe_source,
        steps = steps,
        tries = 1,
        icon = icon,
    )
    new_recipe.save()
    print("FOUR")
    # Violated DRY here, should not make a measurements object above (keep it quantities and units)
    for idx, measurement in enumerate(measurements):
        qty = measurement.split()[0]
        try:
            glue = " "
            unit = glue.join(measurement.split()[1:])
        except:
            unit = ""
        new_measurement = Measurement(recipe=new_recipe, ingredient=ingredient_objects[idx], qty=qty, unit=unit)
        new_measurement.save()
        print("SAVED: " + measurement)

print("END")