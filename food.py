import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title and icon
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍽️")

# --- Profile Section ---
st.sidebar.header("👤 Create Your Profile")
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email ID")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if not (name and email and username and password):
    st.warning("Please complete your profile details to proceed!")
    st.stop()

# --- Personal Details Section ---
st.sidebar.header("📌 Personal Details")
weight_unit = st.sidebar.radio("Weight Unit", ["kg", "lb"])
weight = st.sidebar.number_input(f"Weight ({weight_unit})", min_value=1.0, step=0.5)

height_unit = st.sidebar.radio("Height Unit", ["cm", "inches", "ft"])
height = st.sidebar.number_input(f"Height ({height_unit})", min_value=1.0, step=0.5)

allergy = st.sidebar.radio("Do you have any allergies?", ["No", "Yes"])
allergy_list = st.sidebar.text_area("List your allergies", "", disabled=(allergy == "No"))

diet_type = st.sidebar.multiselect("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"], default=["Vegetarian"])
lactose_intolerant = st.sidebar.radio("Are you lactose intolerant?", ["No", "Yes"])

lifestyle = st.sidebar.multiselect("Lifestyle", ["Active", "Sedentary", "Moderately Active", "Moderately Sedentary", "Mix of Active & Sedentary"], default=["Active"])

goal = st.sidebar.multiselect("Your Goal", ["Increase Weight", "Decrease Weight", "Maintain Weight"], default=["Maintain Weight"])

diet_following = st.sidebar.radio("Are you following any specific diet?", ["No", "Yes"])
diet_description = st.sidebar.text_area("Describe Your Diet", "", disabled=(diet_following == "No"))

# --- Recipe Generation Section ---
st.title("🍽️ AI Recipe Generator")
st.subheader("Personalized Recipes Based on Your Preferences")

num_people = st.number_input("Number of People to Cook For", min_value=1, step=1, value=1)
ingredients = st.text_area("Enter Ingredients You Have", "e.g., rice, chicken, spinach, tomatoes")

def generate_recipe(ingredients, num_people):
    # Dummy recipe generator (replace with an AI model for real recipes)
    recipe = {
        "Title": "Healthy Meal Plan",
        "Ingredients": ingredients.split(","),
        "Instructions": [
            "1. Wash and prep ingredients.",
            "2. Cook in a pan for 20 minutes
