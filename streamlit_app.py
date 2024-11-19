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

   
elif menu == "About":
    
    file_path = 'frontend/about.txt'

    with open(file_path, 'r') as file:
        content = file.read()

    st.markdown(content)
    

