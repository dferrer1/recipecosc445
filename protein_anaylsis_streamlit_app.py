# Streamlit App for Viewing Analysis

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Integrate the uploaded Python file
exec("""
import requests
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt

recipes_df = pd.read_csv('https://huggingface.co/datasets/Shengtao/recipe/resolve/main/recipe.csv')

top_protein_recipes = recipes_df[['title', 'protein_g', 'url']].sort_values(by='protein_g', ascending=False).head(100)

top_protein_recipes.head(10)

skipwords = ["or", "chopped", "sliced", "divided", "diced", "minced", "crushed", "to", "taste"]

top_protein_recipes = recipes_df[['title', 'protein_g', 'ingredients']].sort_values(by='protein_g', ascending=False).head(100)


ingredients_list = []
for ingredients in top_protein_recipes['ingredients']:

    ingredients_split = re.split(r'[;,]', ingredients.lower())
    for ingredient in ingredients_split:

        cleaned_ingredient = ' '.join([word for word in ingredient.split() if word not in skipwords])
        ingredients_list.append(cleaned_ingredient.strip())

ingredient_counts = Counter(ingredients_list)

ingredient_counts_df = pd.DataFrame(ingredient_counts.items(), columns=['ingredient', 'count']).sort_values(by='count', ascending=False)

ingredient_counts_df.head(100)

import pandas as pd
from collections import Counter
import re


meat_types = [
    "chicken", "beef", "pork", "lamb", "turkey", "duck", "bacon", "sausage",
    "ham", "veal", "venison", "rabbit", "goat", "salami", "prosciutto", "chorizo"
]

top_10000_protein_recipes = recipes_df[['title', 'protein_g', 'ingredients']].sort_values(by='protein_g', ascending=False).head(10000)


meat_list = []
for ingredients in top_10000_protein_recipes['ingredients']:
    ingredients_split = re.split(r'[;,]', ingredients.lower())
    for ingredient in ingredients_split:
        for meat in meat_types:
            if meat in ingredient:
                meat_list.append(meat)

meat_counts = Counter(meat_list)

meat_counts_df = pd.DataFrame(meat_counts.items(), columns=['meat', 'count']).sort_values(by='count', ascending=False)

print(meat_counts_df)

plt.figure(figsize=(12, 6))
plt.bar(meat_counts_df['meat'], meat_counts_df['count'], color='skyblue')
plt.title('Top Meats in the Top 10,000 High-Protein Recipes')
plt.xlabel('Meat')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
from collections import Counter
import re


grain_types = [
    "rice", "quinoa", "oats", "barley", "corn", "wheat", "bulgur", "millet",
    "farro", "rye", "sorghum", "couscous", "spelt", "amaranth", "teff"
]


top_10000_protein_recipes = recipes_df[['title', 'protein_g', 'ingredients']].sort_values(by='protein_g', ascending=False).head(10000)


grain_list = []
for ingredients in top_10000_protein_recipes['ingredients']:

    ingredients_split = re.split(r'[;,]', ingredients.lower())
    for ingredient in ingredients_split:

        for grain in grain_types:
            if grain in ingredient:
                grain_list.append(grain)


grain_counts = Counter(grain_list)


grain_counts_df = pd.DataFrame(grain_counts.items(), columns=['grain', 'count']).sort_values(by='count', ascending=False)


print(grain_counts_df)

plt.figure(figsize=(12, 6))
plt.bar(grain_counts_df['grain'], grain_counts_df['count'], color='skyblue')
plt.title('Top Grains in the Top 10,000 High-Protein Recipes')
plt.xlabel('Grain')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import re

# List of common meat types to search for in the ingredient lists
meat_types = [
    "chicken", "beef", "pork", "lamb", "turkey", "duck", "bacon", "sausage",
    "ham", "veal", "venison", "rabbit", "goat", "salami", "prosciutto", "chorizo"
]

# Filter to get the top 10,000 high-protein recipes
top_10000_protein_recipes = recipes_df[['title', 'protein_g', 'ingredients']].sort_values(by='protein_g', ascending=False).head(10000)

# Dictionary to store total protein and counts for each meat type
meat_protein_totals = {meat: {'total_protein': 0, 'count': 0} for meat in meat_types}

# Analyze each recipe to find which meat it contains and update protein totals
for index, row in top_10000_protein_recipes.iterrows():
    ingredients = row['ingredients'].lower()
    protein = row['protein_g']
    for meat in meat_types:
        if meat in ingredients:
            meat_protein_totals[meat]['total_protein'] += protein
            meat_protein_totals[meat]['count'] += 1

# Calculate average protein for each meat type
meat_avg_protein = {meat: (meat_protein_totals[meat]['total_protein'] / meat_protein_totals[meat]['count']
                           if meat_protein_totals[meat]['count'] > 0 else 0)
                    for meat in meat_types}

# Convert to DataFrame for easier visualization
meat_avg_protein_df = pd.DataFrame(list(meat_avg_protein.items()), columns=['meat', 'average_protein']).sort_values(by='average_protein', ascending=False)

# Display the DataFrame
print(meat_avg_protein_df)

# Plot the results
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.bar(meat_avg_protein_df['meat'], meat_avg_protein_df['average_protein'], color='salmon')
plt.title('Average Protein Content by Meat Type in Top 10,000 Recipes')
plt.xlabel('Meat')
plt.ylabel('Average Protein (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import re
import matplotlib.pyplot as plt

# List of common grain types to search for in the ingredient lists
grain_types = [
    "rice", "quinoa", "oats", "barley", "corn", "wheat", "bulgur", "millet",
    "farro", "rye", "sorghum", "couscous", "spelt", "amaranth", "teff"
]

# Filter to get the top 10,000 high-protein recipes
top_10000_protein_recipes = recipes_df[['title', 'protein_g', 'ingredients']].sort_values(by='protein_g', ascending=False).head(10000)

# Dictionary to store total protein and counts for each grain type
grain_protein_totals = {grain: {'total_protein': 0, 'count': 0} for grain in grain_types}

# Analyze each recipe to find which grain it contains and update protein totals
for index, row in top_10000_protein_recipes.iterrows():
    ingredients = row['ingredients'].lower()
    protein = row['protein_g']
    for grain in grain_types:
        if grain in ingredients:
            grain_protein_totals[grain]['total_protein'] += protein
            grain_protein_totals[grain]['count'] += 1

# Calculate average protein for each grain type
grain_avg_protein = {grain: (grain_protein_totals[grain]['total_protein'] / grain_protein_totals[grain]['count']
                             if grain_protein_totals[grain]['count'] > 0 else 0)
                    for grain in grain_types}

# Convert to DataFrame for easier visualization
grain_avg_protein_df = pd.DataFrame(list(grain_avg_protein.items()), columns=['grain', 'average_protein']).sort_values(by='average_protein', ascending=False)

# Display the DataFrame
print(grain_avg_protein_df)

# Plot the results
plt.figure(figsize=(12, 6))
plt.bar(grain_avg_protein_df['grain'], grain_avg_protein_df['average_protein'], color='lightblue')
plt.title('Average Protein Content by Grain Type in Top 10,000 Recipes')
plt.xlabel('Grain')
plt.ylabel('Average Protein (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter


# Analysis 2: Protein Content by Recipe Category
def protein_by_category(recipes_df):
    category_protein = recipes_df.groupby('category')['protein_g'].mean().sort_values(ascending=False)
    category_protein.plot(kind='bar', title="Average Protein Content by Category")
    plt.xlabel("Category")
    plt.ylabel("Average Protein (g)")
    plt.show()

# Analysis 3: Protein Content by Cuisine Type
def protein_by_cuisine(recipes_df):
    cuisine_protein = recipes_df.groupby('category')['protein_g'].mean().sort_values(ascending=False)
    cuisine_protein.plot(kind='bar', title="Average Protein Content by Cuisine")
    plt.xlabel("Cuisine")
    plt.ylabel("Average Protein (g)")
    plt.show()

# Analysis 4: Protein Density per Serving Size
def protein_density_per_serving(recipes_df):
    recipes_df['protein_per_serving'] = recipes_df['protein_g'] / recipes_df['servings']
    density = recipes_df[['title', 'protein_per_serving']].sort_values(by='protein_per_serving', ascending=False).head(10)
    return density



# Analysis 6: Protein Content vs. Recipe Rating
def protein_vs_rating(recipes_df):
    plt.scatter(recipes_df['protein_g'], recipes_df['rating'], alpha=0.5)
    plt.title("Protein Content vs. Recipe Rating")
    plt.xlabel("Protein (g)")
    plt.ylabel("Rating")
    plt.show()

# Analysis 7: Nutrient Pairing with Protein (Fiber and Fat)
def nutrient_pairing_with_protein(recipes_df):
    nutrients = ['dietary_fiber_g', 'fat_g']
    for nutrient in nutrients:
        recipes_df.plot(kind='scatter', x='protein_g', y=nutrient, title=f"Protein vs {nutrient.capitalize()}")
        plt.xlabel("Protein (g)")
        plt.ylabel(f"{nutrient.capitalize()} (g)")
        plt.show()





# Analysis 9: Comparison of Animal vs. Plant-Based Protein Sources
def animal_vs_plant_protein(recipes_df):
    animal_ingredients = ['chicken', 'beef', 'pork', 'lamb', 'turkey', 'fish', 'shrimp', 'egg']
    plant_ingredients = ['beans', 'tofu', 'lentils', 'chickpeas', 'tempeh', 'nuts', 'seitan']

    recipes_df['source'] = recipes_df['ingredients'].apply(
        lambda x: 'animal' if any(meat in x.lower() for meat in animal_ingredients)
        else 'plant' if any(plant in x.lower() for plant in plant_ingredients) else 'other'
    )
    avg_protein_source = recipes_df[recipes_df['source'] != 'other'].groupby('source')['protein_g'].mean()

    avg_protein_source.plot(kind='bar', title="Average Protein Content by Source Type")
    plt.xlabel("Source Type")
    plt.ylabel("Average Protein (g)")
    plt.show()

# Example calls for each analysis


print("\nProtein Content by Category:")
protein_by_category(recipes_df)

print("\nProtein Content by Cuisine:")
protein_by_cuisine(recipes_df)

print("\nProtein Density per Serving:")
print(protein_density_per_serving(recipes_df))


print("\nProtein Content vs. Recipe Rating:")
protein_vs_rating(recipes_df)

print("\nNutrient Pairing with Protein:")
nutrient_pairing_with_protein(recipes_df)



print("\nComparison of Animal vs. Plant-Based Protein Sources:")
animal_vs_plant_protein(recipes_df)

low_protein_threshold = 5  # Adjust as needed
low_protein_recipes = recipes_df[recipes_df['protein_g'] < low_protein_threshold]

# Define the non-ingredient words filter as before
non_ingredient_words = [
    "tablespoon", "teaspoon", "cup", "cups", "ounce", "ounces", "pound", "pounds",
    "to taste", "taste", "divided", "beaten", "chopped", "sliced", "diced", "ground",
    "large", "small", "medium", "clove", "cloves", "pinch", "½", "¼", "¾", "1", "2", "3",
    "4", "5", "6", "7", "8", "9", "10"
]

def common_ingredients_low_protein(recipes_df):
    ingredient_counts = Counter()
    for _, row in recipes_df.iterrows():
        ingredients = re.split(r'[;,]', row['ingredients'].lower())
        for ingredient in ingredients:
            cleaned_ingredient = ' '.join(
                word for word in ingredient.split() if word not in non_ingredient_words
            )
            if cleaned_ingredient:
                ingredient_counts[cleaned_ingredient] += 1
    # Convert to DataFrame and get top ingredients
    common_ingredients = pd.DataFrame(ingredient_counts.most_common(10), columns=['ingredient', 'count'])
    return common_ingredients

print("Common Ingredients in Low-Protein Recipes:")
print(common_ingredients_low_protein(low_protein_recipes))

def low_protein_by_category(recipes_df):
    category_counts = recipes_df.groupby('category').size().sort_values(ascending=False)
    category_counts.plot(kind='bar', title="Number of Low-Protein Recipes by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Recipes")
    plt.show()

print("Low-Protein Recipes by Category:")
low_protein_by_category(low_protein_recipes)

def low_protein_by_cuisine(recipes_df):
    cuisine_counts = recipes_df.groupby('category').size().sort_values(ascending=False)
    cuisine_counts.plot(kind='bar', title="Number of Low-Protein Recipes by Cuisine")
    plt.xlabel("Cuisine")
    plt.ylabel("Number of Recipes")
    plt.show()

print("Low-Protein Recipes by Cuisine:")
low_protein_by_cuisine(low_protein_recipes)

def avg_nutrients_low_protein(recipes_df):
    avg_nutrients = recipes_df[['carbohydrates_g', 'fat_g', 'dietary_fiber_g']].mean()
    print("Average Nutrient Content in Low-Protein Recipes:")
    print(avg_nutrients)

avg_nutrients_low_protein(low_protein_recipes)

def avg_nutrients_low_protein(recipes_df):
    avg_nutrients = recipes_df[['carbohydrates_g', 'fat_g', 'dietary_fiber_g']].mean()
    print("Average Nutrient Content in Low-Protein Recipes:")
    print(avg_nutrients)

avg_nutrients_low_protein(low_protein_recipes)

def low_protein_ingredient_combinations(recipes_df):
    top_ingredients = common_ingredients_low_protein(recipes_df)['ingredient'].tolist()
    combination_counts = Counter()
    for ingredients in recipes_df['ingredients']:
        ingredients_split = re.split(r'[;,]', ingredients.lower())
        cleaned_ingredients = []
        for ingredient in ingredients_split:
            cleaned_ingredient = ' '.join(
                word for word in ingredient.split() if word not in non_ingredient_words
            )
            if cleaned_ingredient:
                cleaned_ingredients.append(cleaned_ingredient)
        present_ingredients = [ingredient for ingredient in cleaned_ingredients if ingredient in top_ingredients]
        if len(present_ingredients) > 1:
            combination_counts.update(present_ingredients)
    return pd.DataFrame(combination_counts.most_common(10), columns=['combination', 'count'])

print("Top Ingredient Combinations in Low-Protein Recipes:")
print(low_protein_ingredient_combinations(low_protein_recipes))

def protein_vs_complexity(recipes_df):
    recipes_df['ingredient_count'] = recipes_df['ingredients'].apply(lambda x: len(re.split(r'[;,]', x)))
    plt.scatter(recipes_df['ingredient_count'], recipes_df['protein_g'], alpha=0.5)
    plt.title("Protein Content vs. Recipe Complexity")
    plt.xlabel("Number of Ingredients")
    plt.ylabel("Protein (g)")
    plt.show()

protein_vs_complexity(recipes_df)

low_carb_threshold = 10  # grams of carbs
low_carb_recipes = recipes_df[recipes_df['carbohydrates_g'] < low_carb_threshold]

def protein_in_low_carb(recipes_df):
    avg_protein = recipes_df['protein_g'].mean()
    print(f"Average Protein in Low-Carb Recipes (<{low_carb_threshold}g carbs): {avg_protein:.2f}g")

protein_in_low_carb(low_carb_recipes)
""")

# Title of the Streamlit App
st.title("Protein Analysis Dashboard")

# Description
st.write("This dashboard allows you to view various protein analysis visualizations and results.")

# Provide options for different analyses
analysis_option = st.selectbox(
    "Choose an analysis to view:",
    [
        "Protein Content Distribution",
        "Top Ingredients by Protein Contribution",
        "Protein Content by Category",
        "Protein Density per Serving",
        "Protein Content vs. Recipe Popularity",
        "Protein Trends Over Time (if applicable)",
        "Low Protein Recipes"
    ]
)

# Trigger different analysis based on the selected option
if analysis_option == "Protein Content Distribution":
    st.write("### Protein Content Distribution Across Recipes")
    protein_content_distribution(recipes_df)

elif analysis_option == "Top Ingredients by Protein Contribution":
    st.write("### Top Ingredients by Protein Contribution")
    top_protein = top_protein_ingredients(recipes_df)
    st.write(top_protein)

elif analysis_option == "Protein Content by Category":
    st.write("### Protein Content by Category")
    protein_by_category(recipes_df)

elif analysis_option == "Protein Density per Serving":
    st.write("### Protein Density per Serving")
    density = protein_density_per_serving(recipes_df)
    st.write(density)

elif analysis_option == "Protein Content vs. Recipe Popularity":
    st.write("### Protein Content vs. Recipe Popularity")
    protein_vs_popularity(recipes_df)

elif analysis_option == "Protein Trends Over Time (if applicable)":
    if 'date' in recipes_df.columns:
        st.write("### Protein Trends Over Time")
        protein_trend_over_time(recipes_df)
    else:
        st.write("Date column not available in the dataset.")

elif analysis_option == "Low Protein Recipes":
    st.write("### Low Protein Recipes")
    low_protein_threshold = 5  # Adjustable
    low_protein_recipes = recipes_df[recipes_df['protein_g'] < low_protein_threshold]
    st.write("Low Protein Recipes (Protein < 5g):")
    st.write(low_protein_recipes)
    st.write("Common Ingredients in Low Protein Recipes:")
    common_ingredients = common_ingredients_low_protein(low_protein_recipes)
    st.write(common_ingredients)
