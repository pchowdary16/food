import streamlit as st
import random
import openai
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def calculate_bmi(weight, height):
    if height > 0:
        return round(weight / ((height / 100) ** 2), 2)
    return None

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or set directly: openai.api_key = "your_api_key"

st.set_page_config(page_title="AI Recipe Maker", layout="wide")
st.title("AI Recipe Maker Dashboard")

# Account Details
st.sidebar.header("Account Details")
name = st.sidebar.text_input("Name")
email = st.sidebar.text_input("Email")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Personal Details
st.sidebar.header("Personal Details")
weight_kg = st.sidebar.number_input("Weight (kg)", min_value=0.0, format="%.2f")
weight_lb = weight_kg * 2.20462
st.sidebar.write(f"Weight (lb): {weight_lb:.2f}")

height_cm = st.sidebar.number_input("Height (cm)", min_value=0.0, format="%.2f")
height_inches = height_cm * 0.393701
height_feet = height_inches / 12
st.sidebar.write(f"Height (inches): {height_inches:.2f}")
st.sidebar.write(f"Height (feet): {height_feet:.2f}")

bmi = calculate_bmi(weight_kg, height_cm)
st.sidebar.write(f"Calculated BMI: {bmi if bmi else 'N/A'}")

allergy_status = st.sidebar.radio("Do you have any allergies?", ("Yes", "No"))
if allergy_status == "Yes":
    allergies = st.sidebar.text_area("List your allergies")

goals = st.sidebar.multiselect(
    "What is your goal?",
    ["Increase weight", "Decrease weight", "Maintain weight", "Control calorie intake"]
)

lifestyle = st.sidebar.selectbox(
    "What is your lifestyle?",
    ["Sedentary", "Moderately sedentary", "Moderately active", "Active", "Mix of both"]
)

diet_status = st.sidebar.radio("Are you following a specific diet?", ("Yes", "No"))
if diet_status == "Yes":
    diet_type = st.sidebar.text_input("What type of diet are you following?")
else:
    preferred_diet = st.sidebar.text_input("Do you have any particular diet you want to follow?")

# AI Recipe Maker
st.header("AI Recipe Maker")

ingredients = st.text_area("Enter ingredients (comma separated)")
recipe_name = st.text_input("Or enter the name of a recipe")
num_people = st.number_input("Number of people", min_value=1, step=1, value=1)

def generate_ai_recipe(ingredients, recipe_name, num_people, preferences):
    prompt = """
    Generate a detailed recipe with step-by-step instructions, ingredient measurements adjusted for {num_people} people, and based on the following details:
    Ingredients: {ingredients}
    Recipe Name: {recipe_name}
    Dietary Preferences: {preferences}
    Provide an elaborate cooking process from start to end, including preparation steps like washing and cutting vegetables, heating oil, and adding ingredients sequentially.
    """.format(num_people=num_people, ingredients=ingredients, recipe_name=recipe_name, preferences=preferences)
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a professional chef providing detailed recipes."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"].strip()

if st.button("Generate Recipe"):
    result = generate_ai_recipe(ingredients, recipe_name, num_people, goals)
    st.success(result)

# Sample Recipe Images
st.header("Recipe Images")
st.image("https://source.unsplash.com/600x400/?food", caption="Example Dish", use_column_width=True)

# Apply Black and White Theme
st.markdown(
    """
    <style>
        body { 
            background-color: black; 
            color: white; 
        }
        .stTextInput, .stNumberInput, .stSelectbox, .stRadio, .stMultiselect, .stButton {
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

