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
    
    st.write("""
             ## Common Ingredient Analysis
             The main question that was investigated in this part of the project was "What are the ingredients that are used most commonly between recipes?"
             The answer to this question is interesting for a number of reasons. One is that knowing what ingredients are most common can help beginning home cooks,
             that want to stick to a budget but also practice several recipes, choose their ingredients more efficiently. Through this analysis, we were able to find
             15 ingredients that were used most commonly. Fittingly, the most commonly used ingredient was salt, which was used in almost 10000 recipes.
             """)
    st.image('images/Top 15 Most Commonly Used Ingredients.png')
    st.write("""
             ### Common Ingredients, Common Recipes
             Taking this analysis a step further, we took the top 15 most common ingredients and found which recipes used the most of these ingredients. 
             Doing this would allow for a user to be able to buy all of these ingredients and know ahead of time that they could make several recipes with most of those ingredients.
             One interesting conclusion that we were able to draw from this relates to the kind of ingredients that were most common, which were the kind of ingredients that were most common.
             From the figure below, we can see that most of the recipes that can be made with the top 15 ingredients were baked goods.
             """)
    st.image('images/Top 30 Recipes Using Most Common Ingredients.png')
    st.write("""
             ### Less Baked Goods Please
             To help make this analysis useful to more people, we included an analysis that excluded some ingredients to help veer the analysis away from baked goods.
             Although there are much less baked goods with this result, some still remain, indicating that some baked goods could not be filtered out this way.
             """)
    st.image('images/Top 30 Recipes Excluding xyz.png')
    st.write("""
             ### Specifying Ingredients
             One benefit of this analysis is that it can also be used to determine potential recipes based on rating and specific ingredients. 
             The following three figures show the results of filtering for the top 10 rated recipes that use specific ingredients.
             Users can then use this project to specify an ingredient that they might have already to then receive any number of recommended recipes using that ingredient. 
             """)
    st.image('images/Top 10 Recipes Using x.png')
    st.image('images/Top 10 Recipes Using xy.png')
    st.image('images/Top 10 Recipes Using xyz.png')
    st.write("""
             ## Protein Analysis
             """)
    st.write("To start I decided to look into the meats that showed up most often.")
    st.image('images/JM1.png')
    st.image('images/JM2.png')
    st.write("I think this result is interesting, I had assumed rice would have been the clear cut favorite and instead corn is.")
    st.image('images/JM3.png')
    st.image('images/JM4.png')
    st.image('images/JM5.png')
    st.write("To no ones surprise, animal based proteins have more protein than plant based.")
    st.image('images/JM6.png')
    st.image('images/JM7.png')
    
    st.write("""
             ## Calories Analysis
             We analyzed the correlation between the ingredients and calories.
             The following scatterplot and heatmap show the correlation between the number of ingredients and calories. 
             We were able to conclude that most recipes in our dataset had 50~100 ingredients. 
             We also found out that among the recipes that are very high in calories, there were a few outliers not correspond to many ingredients. 
             This suggests that the calorie content is not directly proportional to the number of ingredients. 
             The correlation between calories and ingredients number is 20%, meaning there is not much correlation between the number of ingredients and calories. 
             """)    
    st.image('images/SA1.png')
    st.image('images/SA2.png')

    st.write("""
             ### Recipes with the highest calories 
             To find if recipes with high calories have ingredients used in common, 
             we decided to search for the top recipes with the highest calories.  
             """)
    
    st.image('images/SA3.png')
    
    st.write("""
             ### Ingredients with the highest calories 
             After getting the data of the top 10 recipes with the highest calories, 
             we searched for common ingredients used among the high-calorie recipes. 
             As a result, we were able to conclude that butter, minced garlic, sesame oil, and other common ingredients like salt were commonly used in the recipes. 
             There were some calorie-dense ingredients like butter and sesame oil, but some ingredients like minced garlic were not really calorie-dense. 
             """)
    st.image('images/SA4.png')

elif menu == "About":
    
    file_path = 'frontend/about.txt'

    with open(file_path, 'r') as file:
        content = file.read()

    st.markdown(content)
    

