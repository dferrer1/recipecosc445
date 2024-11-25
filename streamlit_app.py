import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.sidebar.title("Menu")
menu = st.sidebar.radio("Select a page:", ["Home", "Results", "About"])

if menu == "Home":
    file_path = 'frontend/home.txt'

    with open(file_path, 'r') as file:
        content = file.read()

    st.markdown(content)    


if menu == "Results":
    st.title("Results")
    st.write(
        "This page is dedicated to showcasing our results and charts."
    )
    st.image('images/Top 15 Most Commonly Used Ingredients.png')
    st.image('images/Top 30 Recipes Using xyz.png')
    st.image('images/Top 30 Recipes Excluding xyz.png')
    st.image('images/Top 10 Recipes Using x.png')
    st.image('images/Top 10 Recipes Using xy.png')
    st.image('images/Top 10 Recipes Using xyz.png')
    st.image('images/JM1.png')
    st.image('images/JM2.png')
    st.image('images/JM3.png')
    st.image('images/JM4.png')
    st.image('images/JM5.png')
    st.image('images/JM6.png')
    st.image('images/JM7.png')
    
    st.write("Scatterplot and a heatmap results.")
    code = """
    !pip install datasets pandas matplotlib seaborn

    from datasets import load_dataset
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    dataset = load_dataset("AkashPS11/recipes_data_food.com", split="train")
    df = dataset.to_pandas()

    print("Column Names in Dataset:")
    print(df.columns)

    ingredients_column = 'RecipeIngredientParts'
    calories_column = 'Calories'

    df = df.dropna(subset=[calories_column])

    print(f"\nIngredients and {calories_column} Columns:")
    print(df[[ingredients_column, calories_column]].head())

    df['ingredient_count'] = df[ingredients_column].apply(lambda x: len(x))

    correlation = df[['ingredient_count', calories_column]].corr()
    print("Correlation Matrix:")
    print(correlation)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='ingredient_count', y=calories_column)
    plt.title("Ingredient Count vs. Calories")
    plt.xlabel("Number of Ingredients")
    plt.ylabel("Calories")
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()
    """
    st.code(code, language='python')  
    st.image('images/SA1.png')
    st.image('images/SA2.png')

    code = """
    !pip install datasets matplotlib
    
    import load_dataset 
    import matplotlib.pyplot as plt

    dataset = load_dataset("Shengtao/recipe", split="train")

    import pandas as pd
    df = pd.DataFrame(dataset)

    top_10_highest_calories = df.nlargest(10, 'calories')[['title', 'calories']]

    plt.figure(figsize=(10, 6))
    plt.bar(top_10_highest_calories['title'], top_10_highest_calories['calories'], color='salmon')
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("title")
    plt.ylabel("Calories")
    plt.title("Top 10 Foods with Highest Calories")
    plt.tight_layout()
    plt.show()
    """

    st.code(code, language='python')  
    st.image('images/SA3.png')


    code = """ 
    top_10_ingredients = df.nlargest(10, 'calories')['ingredients']

    all_ingredients = []
    for ingredients_list in top_10_ingredients:
        ingredients = [ingredient.strip().lower() for ingredient in ingredients_list.split(';')]
        all_ingredients.extend(ingredients)

    from collections import Counter
    ingredient_counts = Counter(all_ingredients)

    ingredient_data = ingredient_counts.most_common(10)

    ingredients, counts = zip(*ingredient_data)

    plt.figure(figsize=(10, 6))
    plt.bar(ingredients, counts, color='lightcoral')
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Ingredients")
    plt.ylabel("Frequency")
    plt.title("Top 10 Most Common Ingredients in High-Calorie Foods")
    plt.tight_layout()
    plt.show()
    """
    st.code(code, language='python') 
    st.image('images/SA4.png')

elif menu == "About":
    
    file_path = 'frontend/about.txt'

    with open(file_path, 'r') as file:
        content = file.read()

    st.markdown(content)
    

