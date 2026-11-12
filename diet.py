import streamlit as st

st.set_page_config(
    page_title="Healthy Diet Planner",
    page_icon="🥗"
)

st.title("🥗 Healthy Diet Planner")
st.write("Welcome! Let's explore healthy food choices.")

st.divider()

# Personal details
st.header("Personal Information")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=5,
    max_value=100,
    value=18
)

# Food preference
st.header("Food Preferences")

food = st.selectbox(
    "Choose your food preference",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

# Activity
activity = st.radio(
    "Choose your activity level",
    ["Low", "Moderate", "High"]
)

# Meal selection
st.header("Select Your Meals")

breakfast = st.selectbox(
    "Breakfast",
    ["Idli", "Dosa", "Oats", "Poha", "Upma"]
)

lunch = st.selectbox(
    "Lunch",
    ["Rice and Dal", "Roti and Vegetables",
     "Vegetable Pulao", "Curd Rice"]
)

dinner = st.selectbox(
    "Dinner",
    ["Chapati and Dal", "Vegetable Khichdi",
     "Rice and Vegetables", "Dosa"]
)

# Water intake
st.header("Water Intake")

water = st.slider(
    "How many glasses of water do you usually drink?",
    1, 15, 6
)

# Submit button
if st.button("Generate My Meal Plan"):

    st.success("Your meal plan is ready!")

    st.subheader("Your Details")
    st.write("Name:", name)
    st.write("Food Preference:", food)
    st.write("Activity Level:", activity)

    st.subheader("Your Meal Suggestions")

    st.write("🌅 Breakfast:", breakfast)
    st.write("☀️ Lunch:", lunch)
    st.write("🌙 Dinner:", dinner)

    st.write("💧 Water glasses:", water)

    st.balloons()

st.divider()

st.caption(
    "Eat a variety of foods and enjoy balanced meals!"
)