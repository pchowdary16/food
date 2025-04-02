import streamlit as st

def calculate_bmi(weight, height):
    if height > 0:
        return round(weight / ((height / 100) ** 2), 2)
    return None

st.set_page_config(page_title="AI Recipe Maker", layout="wide")
st.title("AI Recipe Maker Dashboard")

# Sidebar Toggle Feature
if "show_details" not in st.session_state:
    st.session_state.show_details = True

def toggle_details():
    st.session_state.show_details = not st.session_state.show_details

st.sidebar.button("✏️ Edit Details", on_click=toggle_details)

if st.session_state.show_details:
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

def generate_recipe(ingredients, recipe_name, num_people):
    if not ingredients and not recipe_name:
        return "Please provide ingredients or a recipe name."
    recipe = f"Generated Recipe for {recipe_name if recipe_name else 'your ingredients'} (Serves {num_people} people)"
    return recipe

if st.button("Generate Recipe"):
    result = generate_recipe(ingredients, recipe_name, num_people)
    st.success(result)

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

