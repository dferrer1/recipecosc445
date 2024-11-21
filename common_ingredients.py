import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('WebAgg') # Uncomment when using plots remotely or with wsl


def get_colors(color_num):
    cmap = plt.get_cmap('viridis')
    spread = np.array(np.arange(0,len(cmap.colors),len(cmap.colors)/color_num),dtype=np.int64)
    colors = []
    for val in spread:
        colors.append(cmap(val))
    return colors

#
df = pd.read_csv("hf://datasets/AkashPS11/recipes_data_food.com/recipes.csv")
df.dropna(thresh=2)

#
df2 = pd.read_csv("hf://datasets/Shengtao/recipe/recipe.csv")
df2.dropna(thresh=2)

measurements = [
                "cups)", "tablespoons)", "ounces)", "teaspoons)", "packages)"
                "cup)", "tablespoon)", "ounce)", "teaspoon)", "package)",
                "cups", "tablespoons", "ounces", "teaspoons", "packages",
                "cup", "tablespoon", "ounce", "teaspoon", "package",
                "9", "8", "7", "6", "5", "4", "3", "2", "1",
                "¼", "⅛", "⅓", "½"
                ]   

# Parse recipe data and count all the times each ingredient is used
all_ingredients = {}
for entry in df2['ingredients']:
    entry_ingredients = entry.split(" ; ")
    for item in entry_ingredients:
        if '(Optional)' in item:
            item = item.replace('(Optional)','')
        if '%' in item:
            item = item.replace('%','')
        
        #
        for x in measurements:
            i = item.find(x)
            if i != -1:
                item = item[i+len(x)+1:]
        
        # Add item to dictionary
        if item not in all_ingredients:
            all_ingredients[item] = 1
        else:
            all_ingredients[item] += 1

del all_ingredients['']
print(len(all_ingredients))
print(df2.keys())
print(df2['rating'])
print(df2.loc[df2['title'] == 'Homemade Gluten-Free Cinnamon Rolls'])
print(df2.loc[7496,'ingredients'])
# exit()

# Find the top 15 most common ingredients in all ingredients
from collections import Counter
n = 15
top_n_ingredients = dict(Counter(all_ingredients).most_common(n))
print(top_n_ingredients)                                                                                                                                                                                                                                                 

# Plot the top n ingredients
fig = plt.figure(f"Top {n} Most Commonly Used Ingredients")
plt.suptitle(f"Top {n} Most Commonly Used Ingredients")
plt.subplot(1,1,1)
plt.barh(list(top_n_ingredients.keys()),list(top_n_ingredients.values()),color=get_colors(n))
# plt.title(f"Top {n} Most Commonly Used Ingredients")
# plt.xlabel("# of Recipes With Ingredient")
plt.tight_layout()
plt.savefig(f"images/Top {n} Most Commonly Used Ingredients")

# Grade recipes by how many of the most common ingredients they use
recipe_scores = {}
for i, entry in enumerate(df2['ingredients']):
    recipe_scores[df2['title'][i]] = 0
    for ingredient in top_n_ingredients:
        if ingredient in entry:
            recipe_scores[df2['title'][i]] += 1

# Find the top n "graded" recipes
n = 30
top_n_recipes = dict(Counter(recipe_scores).most_common(n))

# Plot the top n that use the most of the most common ingredients
fig = plt.figure(f"Top {n} Recipes Using Most Common Ingredients")
fig.suptitle(f"Top {n} Recipes Using Most Common Ingredients")
plt.subplot(1,1,1)
plt.viridis()
plt.barh(list(top_n_recipes.keys()),list(top_n_recipes.values()),color=get_colors(n))
# plt.title(f"Top {n} Recipes Using Most Common Ingredients")
# plt.xlabel("# of Common Ingredients Used in Recipe")
plt.tight_layout()
plt.savefig(f"images/Top {n} Recipes Using Most Common Ingredients")
# plt.text(0.1, 0.5, 'Left-aligned text', horizontalalignment='left')
# import textwrap
# labels = [textwrap.fill(label, 10) for label in list(top_n_recipes.keys())]

print()
print()
print("--------------------------------------------------------------------------")
print(f"top {n} ingredients:")
print(top_n_ingredients)
print()
print(f"top {n} recipes using these ingredients:")
print(top_n_recipes)
print("--------------------------------------------------------------------------")

# Find top n "graded" recipes excluding some x ingredients
n = 30
x = ['white sugar', 'all-purpose flour', 'vanilla extract', 'ground cinnamon']

all_ingredients_excluding_x = all_ingredients.copy()
for item in x:
    del all_ingredients_excluding_x[item]

top_n_ingredients_excluding_x = dict(Counter(all_ingredients_excluding_x).most_common(n))

recipe_scores_excluding_x = {}
for i, entry in enumerate(df2['ingredients']):
    recipe_scores_excluding_x[df2['title'][i]] = 0
    for ingredient in top_n_ingredients_excluding_x:
        if ingredient in entry:
            recipe_scores_excluding_x[df2['title'][i]] += 1

top_n_recipes_excluding_x = dict(Counter(recipe_scores_excluding_x).most_common(n))

# Plot the top n that use the most of the most common ingredients
fig = plt.figure(f"Top {n} Using Most Common Ingredients\n(Excluding {x})")
fig.suptitle(f"Top {n} Using Most Common Ingredients (Excluding \n{x})")
plt.subplot(1,1,1)
plt.viridis()
plt.barh(list(top_n_recipes_excluding_x.keys()),list(top_n_recipes_excluding_x.values()),color=get_colors(n))
# plt.title(f"Top {n} Using Most Common Ingredients (Excluding {x})")
plt.tight_layout()
plt.savefig(f"images/Top {n} Recipes Excluding xyz")

print()
print()
print("--------------------------------------------------------------------------")
print(f"top {n} ingredients excluding {x}:")
print(top_n_ingredients_excluding_x)
print()
print(f"top {n} recipes using these ingredients:")
print(top_n_recipes_excluding_x)
print("--------------------------------------------------------------------------")

# Find top rated recipes using x ingredient
x = 'soy sauce'
n = 10
recipes_using_x = {}
for i, entry in enumerate(df2['ingredients']):
    recipes_using_x[df2['title'][i]] = 0
    if x in entry:
        recipes_using_x[df2['title'][i]] = df2['rating'][i] * 1
top_n_recipes_using_x = dict(Counter(recipes_using_x).most_common(n))

# Plot the top n that use the most of the most common ingredients
plt.figure(f"Top {n} Recipes Using {x} (Out of 5 Stars)")
plt.suptitle(f"Top {n} Recipes Using {x} (Out of 5 Stars)")
plt.subplot(1,1,1)
# plt.tight_layout()
# plt.yticks(rotation=45, ha='right')
plt.viridis()
plt.barh(list(top_n_recipes_using_x.keys()),list(top_n_recipes_using_x.values()),color=get_colors(n))
# plt.title(f"Top {n} Recipes (Using {x})")
plt.tight_layout()
plt.savefig(f"images/Top {n} Recipes Using x")

print()
print()
print("--------------------------------------------------------------------------")
print(f"top {n} recipes using {x}:")
print(top_n_recipes_using_x.keys())
print("--------------------------------------------------------------------------")

# Find top rated recipes using x,y ingredient
x = 'garlic powder'
y = 'ground cumin'
n = 10
recipes_using_x = {}
for i, entry in enumerate(df2['ingredients']):
    recipes_using_x[df2['title'][i]] = 0
    if x in entry:
        recipes_using_x[df2['title'][i]] = df2['rating'][i] * 1
    elif y in entry:
        recipes_using_x[df2['title'][i]] = df2['rating'][i] * 1
top_n_recipes_using_x = dict(Counter(recipes_using_x).most_common(n))

# Plot the top n that use the most of the most common ingredients
fig = plt.figure(f"Top {n} Recipes Using {x} and {y} (Out of 5 Stars)")
plt.suptitle(f"Top {n} Recipes Using {x} and {y} (Out of 5 Stars)")
plt.subplot(1,1,1)
plt.viridis()
plt.barh(list(top_n_recipes_using_x.keys()),list(top_n_recipes_using_x.values()),color=get_colors(n))
# plt.title(f"Top {n} Recipes (Using {x} and {y})")
plt.tight_layout()
plt.savefig(f"images/Top {n} Recipes Using xy")

print()
print()
print("--------------------------------------------------------------------------")
print(f"top {n} recipes using {x} and {y}:")
print(top_n_recipes_using_x.keys())
print("--------------------------------------------------------------------------")

# Find top rated recipes using x,y,z ingredient
x = 'soy sauce'
y = 'honey'
z = 'minced garlic'
n = 10
recipes_using_x = {}
for i, entry in enumerate(df2['ingredients']):
    recipes_using_x[df2['title'][i]] = 0
    if x in entry:
        recipes_using_x[df2['title'][i]] = df2['rating'][i] * 1
    elif y in entry:
        recipes_using_x[df2['title'][i]] = df2['rating'][i] * 1
    elif z in entry:
        recipes_using_x[df2['title'][i]] = df2['rating'][i] * 1
top_n_recipes_using_x = dict(Counter(recipes_using_x).most_common(n))

# Plot the top n that use the most of the most common ingredients
fig = plt.figure(f"Top {n} Recipes Using {x}, {y}, and {z} (Out of 5 Stars)")
plt.suptitle(f"Top {n} Recipes Using {x}, {y}, and {z} (Out of 5 Stars)")
plt.subplot(1,1,1)
plt.viridis()
plt.barh(list(top_n_recipes_using_x.keys()),list(top_n_recipes_using_x.values()),color=get_colors(n))
# plt.title(f"Top {n} Recipes (Using {x}, {y}, and {z})")
plt.tight_layout()
plt.savefig(f"images/Top {n} Recipes Using xyz")

print()
print()
print("--------------------------------------------------------------------------")
print(f"top {n} recipes using {x}, {y}, and {z}:")
print(top_n_recipes_using_x.keys())
print("--------------------------------------------------------------------------")
plt.show()
