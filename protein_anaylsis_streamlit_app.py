# Streamlit App for Viewing Analysis

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import importlib.util

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
    protein_analysis.protein_content_distribution(recipes_df)

elif analysis_option == "Top Ingredients by Protein Contribution":
    st.write("### Top Ingredients by Protein Contribution")
    top_protein = protein_analysis.top_protein_ingredients(recipes_df)
    st.write(top_protein)

elif analysis_option == "Protein Content by Category":
    st.write("### Protein Content by Category")
    protein_analysis.protein_by_category(recipes_df)

elif analysis_option == "Protein Density per Serving":
    st.write("### Protein Density per Serving")
    density = protein_analysis.protein_density_per_serving(recipes_df)
    st.write(density)

elif analysis_option == "Protein Content vs. Recipe Popularity":
    st.write("### Protein Content vs. Recipe Popularity")
    protein_analysis.protein_vs_popularity(recipes_df)

elif analysis_option == "Protein Trends Over Time (if applicable)":
    if 'date' in recipes_df.columns:
        st.write("### Protein Trends Over Time")
        protein_analysis.protein_trend_over_time(recipes_df)
    else:
        st.write("Date column not available in the dataset.")

elif analysis_option == "Low Protein Recipes":
    st.write("### Low Protein Recipes")
    low_protein_threshold = 5  # Adjustable
    low_protein_recipes = recipes_df[recipes_df['protein_g'] < low_protein_threshold]
    st.write("Low Protein Recipes (Protein < 5g):")
    st.write(low_protein_recipes)
    st.write("Common Ingredients in Low Protein Recipes:")
    common_ingredients = protein_analysis.common_ingredients_low_protein(low_protein_recipes)
    st.write(common_ingredients)
