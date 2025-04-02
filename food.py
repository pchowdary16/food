import streamlit as st

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2) if height_m > 0 else 0

def main():
    st.sidebar.title("Dashboard")
    menu = ["Account Details", "Personal Details"]
    choice = st.sidebar.radio("Navigation", menu)
    
    if choice == "Account Details":
        st.title("Account Details")
        name = st.text_input("Name")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
    
    elif choice == "Personal Details":
        st.title("Personal Details")
        weight_kg = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
        weight_lb = round(weight_kg * 2.20462, 2)
        st.write(f"Weight in pounds: {weight_lb} lb")
        
        height_cm = st.number_input("Height (cm)", min_value=0.0, format="%.2f")
        height_in = round(height_cm * 0.393701, 2)
        st.write(f"Height in inches: {height_in} in")
        
        if weight_kg > 0 and height_cm > 0:
            bmi = calculate_bmi(weight_kg, height_cm)
            st.write(f"Calculated BMI: {bmi}")
        
        allergies = st.radio("Do you have any allergies?", ["Select an option", "No", "Yes"], index=0)
        if allergies == "Yes":
            allergy_list = st.text_area("List your allergies")
        
        lifestyle_options = ["Select an option", "Sedentary", "Active", "Moderately Active", "Moderately Sedentary", "Mix of Both"]
        lifestyle = st.selectbox("What is your lifestyle?", lifestyle_options, index=0)
        
        goal = st.multiselect("What is your goal?", [
            "Increase weight", "Decrease weight", "Maintain weight", "Intake specific calories"])
        
        diet_following = st.radio("Are you following any diet?", ["Select an option", "No", "Yes"], index=0)
        if diet_following == "Yes":
            diet_type = st.text_input("What type of diet are you following?")
        elif diet_following == "No":
            preferred_diet = st.text_input("Do you have any particular diet you want to follow?")

if __name__ == "__main__":
    main()
