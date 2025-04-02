import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_bmi(weight_kg, height_cm):
    if height_cm > 0:
        return round(weight_kg / ((height_cm / 100) ** 2), 2)
    return 0

def main():
    st.sidebar.title("Dashboard")
    menu = ["Account Details", "Personal Details", "AI Recipe Generator"]
    choice = st.sidebar.radio("Navigation", menu)
    
    if choice == "Account Details":
        st.title("👤 Account Details")
        name = st.text_input("Name")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
    
    elif choice == "Personal Details":
        st.title("📋 Personal Details")
        
        # Weight Input
        weight_unit = st.radio("Choose weight unit", ["kg", "lb"])
        weight = st.number_input("Weight", min_value=0.0, format="%.2f")
        
        # Height Input
        height_unit = st.radio("Choose height unit", ["cm", "inches", "ft"])
        height = st.number_input("Height", min_value=0.0, format="%.2f")
        
        # BMI Calculation
        if weight > 0 and height > 0:
            weight_kg = weight if weight_unit == "kg" else weight * 0.453592
            height_cm = height if height_unit == "cm" else height * 2.54 if height_unit == "inches" else height * 30.48
            bmi = calculate_bmi(weight_kg, height_cm)
            st.write(f"Calculated BMI: **{bmi}**")
        
        # Allergy Input
        allergies = st.radio("Do you have any allergies?", ["No", "Yes"])
        if allergies == "Yes":
            allergy_list = st.text_area("List your allergies")
        
        # Diet Preference
        diet_pref = st.multiselect("Select your diet preference", ["Vegetarian", "Non-Vegetarian", "Vegan"], default=[])
        if not diet_pref:
            st.warning("Please select at least one dietary preference.")
        
        # Lactose Intolerance
        lactose_intolerant = st.radio("Are you lactose intolerant?", ["No", "Yes"])
        
        # Lifestyle Selection
        lifestyle = st.multiselect("What is your lifestyle?", ["Active", "Sedentary", "Moderately Active", "Moderately Sedentary", "Mix of Active and Sedentary"])
        
        # Goal Selection
        goal = st.multiselect("What is your goal?", ["Increase weight", "Decrease weight", "Maintain weight"])
        
        # Diet Description
        diet_following = st.radio("Are you following any diet?", ["No", "Yes"])
        if diet_following == "Yes":
            diet_description = st.text_area("Describe your diet")
        
    elif choice == "AI Recipe Generator":
        st.title("🍽️ AI Recipe Generator")
        
        # Ingredients Input
        ingredients = st.text_area("Enter the ingredients you have (comma-separated)")
        people = st.number_input("How many people are eating?", min_value=1, step=1)
        
        if st.button("Generate Recipe"):
            if ingredients:
                ingredients_list = [i.strip() for i in ingredients.split(",") if i.strip()]
                
                if ingredients_list:
                    st.success("Here is a customized recipe based on your input:")
                    st.write(f"👨‍🍳 Using ingredients: **{', '.join(ingredients_list)}** for **{people}** people.")
                    st.write("### Steps:")
                    st.write("1. Mix all ingredients together.")
                    st.write("2. Cook in a pan for 20 minutes.")
                    st.write("3. Serve hot and enjoy!")
                else:
                    st.warning("Please enter at least one valid ingredient.")
            else:
                st.warning("Please enter some ingredients.")

        # Display a Food Image
        st.image("https://source.unsplash.com/800x400/?healthy-food", caption="Delicious Meal", use_column_width=True)

if __name__ == "__main__":
    main()
