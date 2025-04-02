import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Streamlit UI
st.title("🍽️ AI-Powered Recipe Dashboard")
st.subheader("Personalized Meal Planning Based on Your Profile")

# User Profile Section
st.sidebar.header("👤 Account Details")
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email ID")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Personal Details Section
st.sidebar.header("📌 Personal Details")
weight_unit = st.sidebar.radio("Weight Unit", ["kg", "lb"])
weight = st.sidebar.number_input(f"Weight ({weight_unit})", min_value=0.0, step=0.1)

height_unit = st.sidebar.radio("Height Unit", ["cm", "inches", "ft"])
height = st.sidebar.number_input(f"Height ({height_unit})", min_value=0.0, step=0.1)

allergies = st.sidebar.radio("Do you have any allergies?", ["Yes", "No"])
allergy_list = st.sidebar.text_area("List your allergies") if allergies == "Yes" else "None"

diet_preference = st.sidebar.multiselect("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"], default=[])
lactose_intolerant = st.sidebar.radio("Are you lactose intolerant?", ["Yes", "No"])

lifestyle = st.sidebar.multiselect("Lifestyle Type", ["Active", "Sedentary", "Moderately Active", "Moderately Sedentary", "Mix of Active and Sedentary"], default=[])

goal = st.sidebar.multiselect("Your Goal", ["Increase Weight", "Decrease Weight", "Maintain Weight"], default=[])

following_diet = st.sidebar.radio("Are you following any diet?", ["Yes", "No"])
diet_description = st.sidebar.text_area("Describe your diet") if following_diet == "Yes" else "Not following a specific diet"

# Recipe Generation Section
st.subheader("🍲 AI-Powered Recipe Suggestions")
num_people = st.number_input("Number of People Eating", min_value=1, step=1, value=1)
ingredients = st.text_area("Enter Ingredients You Have (comma separated)")

if st.button("Generate Recipes"):
    if ingredients:
        ingredient_list = ingredients.split(",")
        recipe = {
            "name": "Healthy Mixed Vegetable Stir-Fry",
            "ingredients": {ing: f"{num_people * 50}g" for ing in ingredient_list},
            "steps": [
                "1. Chop all the vegetables.",
                "2. Cook in a pan for 20 minutes.",
                "3. Add spices and stir well.",
                "4. Serve hot and enjoy!"
            ]
        }
        
        st.subheader("🥗 Your AI-Generated Recipe")
        st.write(f"**Recipe Name:** {recipe['name']}")
        st.write("**Ingredients:**")
        for ing, qty in recipe["ingredients"].items():
            st.write(f"- {ing}: {qty}")
        
        st.write("**Instructions:**")
        for step in recipe["steps"]:
            st.write(f"- {step}")
    else:
        st.warning("Please enter ingredients to generate a recipe!")

# Display Food Images
st.image("https://source.unsplash.com/800x400/?food,healthy", caption="Delicious AI-Generated Meals!", use_column_width=True)

st.caption("🍴 Personalized meal plans just for you!")
