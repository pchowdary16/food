import streamlit as st
import pandas as pd
from PIL import Image
import random

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def generate_recipe(ingredients=None, user_details=None, servings=1):
    recipes = {
        "Pasta": ["pasta", "tomato", "cheese", "garlic"],
        "Salad": ["lettuce", "tomato", "cucumber", "olive oil"],
        "Smoothie": ["banana", "milk", "honey"],
    }
    if not ingredients:
        ingredients = random.choice(list(recipes.values()))
    return {"Recipe Name": random.choice(list(recipes.keys())), "Ingredients": ingredients, "Servings": servings}

# Set up the dashboard
st.set_page_config(page_title="AI Recipe Maker", layout="wide")
st.title("AI Recipe Maker Dashboard")

# Account Details
st.header("Account Details")
name = st.text_input("Name")
email = st.text_input("Email")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Personal Details
st.header("Personal Details")
weight_kg = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)
weight_lb = weight_kg * 2.205
st.write(f"Weight in lb: {round(weight_lb, 2)}")

height_cm = st.number_input("Height (cm)", min_value=100.0, max_value=250.0)
height_m = height_cm / 100
height_ft = height_cm / 30.48
st.write(f"Height in ft: {round(height_ft, 2)}")

bmi = calculate_bmi(weight_kg, height_m)
st.write(f"Calculated BMI: {bmi}")

allergy = st.radio("Do you have any allergies?", ["Yes", "No"])
if allergy == "Yes":
    allergies_list = st.text_area("List your allergies")

goal = st.multiselect("Select your health goal", ["Increase weight", "Lose weight", "Maintain weight", "Caloric intake control"])

lifestyle = st.selectbox("What is your lifestyle?", ["Sedentary", "Active", "Moderately Active", "Moderately Sedentary", "Mix of both"])

diet_following = st.radio("Are you following any diet?", ["Yes", "No"])
if diet_following == "Yes":
    diet_type = st.text_input("Enter the type of diet you are following")
else:
    preferred_diet = st.text_input("Do you have any particular diet you want to follow?")

# AI Recipe Maker
st.header("AI Recipe Maker")
ingredients = st.text_area("Enter ingredients (comma separated)")
recipe_request = st.text_input("Or enter a recipe name you want")
servings = st.number_input("Number of servings", min_value=1, max_value=10, step=1)

if st.button("Generate Recipe"):
    recipe = generate_recipe(ingredients.split(",") if ingredients else None, None, servings)
    st.subheader(f"Recipe: {recipe['Recipe Name']}")
    st.write("Ingredients:", ", ".join(recipe['Ingredients']))
    st.write(f"Servings: {recipe['Servings']}")

# Display food images (Placeholder)
st.header("Food Images")
image_placeholder = Image.new("RGB", (200, 200), color=(255, 255, 255))
st.image(image_placeholder, caption="Example Food Image", use_column_width=True)
