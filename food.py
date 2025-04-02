import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Streamlit Dashboard
st.set_page_config(page_title="AI Recipe Dashboard", page_icon="🍽️", layout="wide")
st.title("🍽️ AI-Powered Recipe Generator Dashboard")

# User Profile Section
st.sidebar.header("👤 Account Details")
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email ID")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if name and email and username and password:
    st.success("Profile Created Successfully! 🎉")
    
    # Personal Details Section
    st.subheader("📝 Personal Details")
    weight_unit = st.radio("Select Weight Unit", ("Kg", "Lb"))
    weight = st.number_input(f"Weight ({weight_unit})", min_value=0.0, step=0.1)
    height_unit = st.radio("Select Height Unit", ("cm", "inches", "ft"))
    height = st.number_input(f"Height ({height_unit})", min_value=0.0, step=0.1)
    
    allergies = st.radio("Do you have any allergies?", ("No", "Yes"))
    if allergies == "Yes":
        allergy_list = st.text_area("List your allergies")
    
    diet_pref = st.multiselect("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
    lactose_intolerant = st.radio("Are you lactose intolerant?", ("No", "Yes"))
    
    lifestyle = st.multiselect("Describe Your Lifestyle", [
        "Active", "Sedentary", "Moderately Active", "Moderately Sedentary", "Mix of Active and Sedentary"
    ])
    
    goal = st.multiselect("Your Health Goal", ["Increase Weight", "Decrease Weight", "Maintain Weight"])
    
    following_diet = st.radio("Are you following any specific diet?", ("No", "Yes"))
    if following_diet == "Yes":
        diet_description = st.text_area("Describe your diet")
    
    st.subheader("🍳 AI-Powered Recipe Generator")
    num_people = st.number_input("How many people are you cooking for?", min_value=1, step=1)
    ingredients = st.text_area("Enter ingredients available (comma separated)")
    
    if st.button("Generate Recipes 🍲"):
        if ingredients:
            # Placeholder for AI recipe generation logic
            st.success(f"Generating recipes for {num_people} people using {ingredients}... 🍛")
            st.image("https://source.unsplash.com/600x400/?food", caption="Delicious Meal", use_column_width=True)
        else:
            st.warning("Please enter ingredients to generate recipes.")
else:
    st.warning("Please fill in account details to proceed.")
