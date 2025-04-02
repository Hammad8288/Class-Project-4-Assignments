# Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes

import streamlit as st

# Custom CSS for better styling
st.markdown(
    """
    <style>
    body{
        background-color: #d142f5;
    }
    .title {
        color: #d142f5;
        text-align: center;
        font-size: 100px;
        font-weight: bold;
    }
    .bmi-result {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        
    }
    .bmi-category {
        font-size: 22px;
        font-weight: bold;
        margin-top: 30px;
    }
    .normal { color: green; }
    .underweight { color: blue; }
    .overweight { color: orange; }
    .obese { color: red; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 class="title"> BMI Calculator </h1>', unsafe_allow_html=True)

height = st.slider("📏 Enter your height (cm):", 100, 250, 175)
weight = st.slider("⚖️ Enter your weight (kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Determine BMI Category
if bmi < 18.5:
    category = "Underweight 😟"
    color_class = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight 🙂"
    color_class = "normal"
elif 25 <= bmi < 29.9:
    category = "Overweight 😓"
    color_class = "overweight"
else:
    category = "Obese 😱"
    color_class = "obese"

# Display BMI
if st.button("Check your BMI"):
    st.markdown(f'<p class="bmi-result {color_class}">Your BMI is {bmi:.2f} - {category}</p>', unsafe_allow_html=True)


