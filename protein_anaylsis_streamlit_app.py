# Streamlit App for Viewing Analysis

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import importlib.util
import re

module_path = '/workspaces/recipecosc445/protein_anaylsis.py'
module_name = 'protein_analysis'

spec = importlib.util.spec_from_file_location(module_name, module_path)
protein_analysis = importlib.util.module_from_spec(spec)
sys.modules[module_name] = protein_analysis
spec.loader.exec_module(protein_analysis)

@st.cache
def load_data():
    url = 'https://huggingface.co/datasets/Shengtao/recipe/resolve/main/recipe.csv'
    return pd.read_csv(url)


recipes_df = load_data()

#st.title("Protein Analysis Dashboard")

# Description
st.write("This dashboard allows you to view various protein analysis visualizations and results.")

# Provide options for different analyses
analysis_option = st.selectbox(
    "Choose an analysis to view:",
    [
        "Top 10 Ingredients by Frequency in High-Protein Recipes",
        "Top Meats by Frequency",
        "Top Grains by Frequency",
        "Average Protein by Meat Type",
        "Average Protein by Grain Type",
        "Protein Content by Category",
        "Protein Content by Complexity",
        "Low-Protein Recipes and Common Ingredients",
        "Protein in Low-Carb Recipes"
    ]
)

# Trigger different analysis based on the selected option
if analysis_option == "Top 10 Ingredients by Frequency in High-Protein Recipes":
    st.write("### Top 10 Ingredients by Frequency in High-Protein Recipes")
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
    st.write(ingredient_counts_df.head(10))

elif analysis_option == "Top Meats by Frequency":
    st.write("### Top Meats by Frequency in High-Protein Recipes")
    meat_types = ["chicken", "beef", "pork", "lamb", "turkey", "duck", "bacon", "sausage",
                  "ham", "veal", "venison", "rabbit", "goat", "salami", "prosciutto", "chorizo"]
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
    st.write(meat_counts_df)

elif analysis_option == "Top Grains by Frequency":
    st.write("### Top Grains by Frequency in High-Protein Recipes")
    grain_types = ["rice", "quinoa", "oats", "barley", "corn", "wheat", "bulgur", "millet",
                   "farro", "rye", "sorghum", "couscous", "spelt", "amaranth", "teff"]
    grain_list = []
    for ingredients in top_10000_protein_recipes['ingredients']:
        ingredients_split = re.split(r'[;,]', ingredients.lower())
        for ingredient in ingredients_split:
            for grain in grain_types:
                if grain in ingredient:
                    grain_list.append(grain)
    grain_counts = Counter(grain_list)
    grain_counts_df = pd.DataFrame(grain_counts.items(), columns=['grain', 'count']).sort_values(by='count', ascending=False)
    st.write(grain_counts_df)

elif analysis_option == "Average Protein by Meat Type":
    st.write("### Average Protein by Meat Type")
    meat_protein_totals = {meat: {'total_protein': 0, 'count': 0} for meat in meat_types}
    for _, row in top_10000_protein_recipes.iterrows():
        ingredients = row['ingredients'].lower()
        protein = row['protein_g']
        for meat in meat_types:
            if meat in ingredients:
                meat_protein_totals[meat]['total_protein'] += protein
                meat_protein_totals[meat]['count'] += 1
    meat_avg_protein = {meat: (meat_protein_totals[meat]['total_protein'] / meat_protein_totals[meat]['count']
                               if meat_protein_totals[meat]['count'] > 0 else 0) for meat in meat_types}
    meat_avg_protein_df = pd.DataFrame(list(meat_avg_protein.items()), columns=['meat', 'average_protein']).sort_values(by='average_protein', ascending=False)
    st.write(meat_avg_protein_df)

elif analysis_option == "Average Protein by Grain Type":
    st.write("### Average Protein by Grain Type")
    grain_protein_totals = {grain: {'total_protein': 0, 'count': 0} for grain in grain_types}
    for _, row in top_10000_protein_recipes.iterrows():
        ingredients = row['ingredients'].lower()
        protein = row['protein_g']
        for grain in grain_types:
            if grain in ingredients:
                grain_protein_totals[grain]['total_protein'] += protein
                grain_protein_totals[grain]['count'] += 1
    grain_avg_protein = {grain: (grain_protein_totals[grain]['total_protein'] / grain_protein_totals[grain]['count']
                                 if grain_protein_totals[grain]['count'] > 0 else 0) for grain in grain_types}
    grain_avg_protein_df = pd.DataFrame(list(grain_avg_protein.items()), columns=['grain', 'average_protein']).sort_values(by='average_protein', ascending=False)
    st.write(grain_avg_protein_df)

elif analysis_option == "Protein Content by Category":
    st.write("### Protein Content by Category")
    protein_by_category = recipes_df.groupby('category')['protein_g'].mean().sort_values(ascending=False)
    st.bar_chart(protein_by_category)

elif analysis_option == "Protein Content by Complexity":
    st.write("### Protein Content by Complexity")
    recipes_df['ingredient_count'] = recipes_df['ingredients'].apply(lambda x: len(re.split(r'[;,]', x)))
    st.scatter_chart(recipes_df, x='ingredient_count', y='protein_g')

elif analysis_option == "Low-Protein Recipes and Common Ingredients":
    st.write("### Low-Protein Recipes and Common Ingredients")
    low_protein_threshold = 5
    low_protein_recipes = recipes_df[recipes_df['protein_g'] < low_protein_threshold]
    common_ingredients = Counter()
    for _, row in low_protein_recipes.iterrows():
        ingredients_split = re.split(r'[;,]', row['ingredients'].lower())
        for ingredient in ingredients_split:
            cleaned_ingredient = ' '.join(word for word in ingredient.split() if word not in skipwords)
            if cleaned_ingredient:
                common_ingredients[cleaned_ingredient] += 1
    common_ingredients_df = pd.DataFrame(common_ingredients.items(), columns=['ingredient', 'count']).sort_values(by='count', ascending=False)
    st.write(common_ingredients_df.head(10))

elif analysis_option == "Protein in Low-Carb Recipes":
    st.write("### Protein in Low-Carb Recipes")
    low_carb_threshold = 10
    low_carb_recipes = recipes_df[recipes_df['carbohydrates_g'] < low_carb_threshold]
    avg_protein = low_carb_recipes['protein_g'].mean()
    st.write(f"Average Protein in Low-Carb Recipes: {avg_protein:.2f} g")