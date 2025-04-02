import streamlit as st
import pandas as pd

def calculate_bmi(weight, height):
    if height > 0:
        return round(weight / ((height / 100) ** 2), 2)
    return None

st.set_page_config(page_title="AI Recipe Maker", layout="wide")
st.title("AI Recipe Maker Dashboard")

# Load Recipe Dataset
def load_recipe_data():
    try:
        return pd.read_csv("C:\\Users\\prane\\Downloads\\Stremlit")
    except Exception as e:
        st.error(f"Error loading recipe data: {e}")
        return None

recipe_data = load_recipe_data()

# Sidebar Toggle Feature
if "show_details" not in st.session_state:
    st.session_state.show_details = True
if "details_filled" not in st.session_state:
    st.session_state.details_filled = False

def toggle_details():
    st.session_state.show_details = not st.session_state.show_details

# Always show edit button at the top
st.sidebar.button("✏️ Edit Details", on_click=toggle_details)

if st.session_state.show_details or not st.session_state.details_filled:
    st.sidebar.header("Account Details")
    name = st.sidebar.text_input("Name")
    email = st.sidebar.text_input("Email")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

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
    
    if st.sidebar.button("Save Details"):
        st.session_state.details_filled = True
        st.session_state.show_details = False

# AI Recipe Maker
st.header("AI Recipe Maker")
st.markdown("<style>.block-container{max-width: 80%;}</style>", unsafe_allow_html=True)

ingredients = st.text_area("Enter ingredients (comma separated)")
recipe_name = st.text_input("Or enter the name of a recipe")
num_people = st.number_input("Number of people", min_value=1, step=1, value=1)

def generate_recipe(ingredients, recipe_name, num_people):
    if recipe_data is None:
        return "Recipe data not available."
    
    if recipe_name:
        matched_recipe = recipe_data[recipe_data['recipe_name'].str.lower() == recipe_name.lower()]
        if not matched_recipe.empty:
            recipe_details = matched_recipe.iloc[0]
            base_servings = recipe_details['servings']
            scale_factor = num_people / base_servings if base_servings > 0 else 1
            ingredients_list = recipe_details['ingredients'].split("\n")
            scaled_ingredients = "\n".join([f"{round(float(i.split()[0]) * scale_factor, 2)} {' '.join(i.split()[1:])}" if i[0].isdigit() else i for i in ingredients_list])
            instructions = recipe_details['instructions']
            return f"### {recipe_name} (Serves {num_people} people)\n\n**Ingredients:**\n{scaled_ingredients}\n\n**Instructions:**\n{instructions}"
        else:
            return "Recipe not found. Try entering ingredients instead."
    elif ingredients:
        return "Feature to generate recipes based on ingredients is under development."
    return "Please provide ingredients or a recipe name."

if st.button("Generate Recipe"):
    result = generate_recipe(ingredients, recipe_name, num_people)
    st.markdown(result)

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
