import streamlit as st

# Set page title
st.title("Fitness Calculator")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Speed Score Calculator", "BMI Calculator", "Jumping Score Calculator"])

# Tab 1: Speed Score Calculator
with tab1:
    st.header("Speed Score Calculator")

    # Input fields for weight and 40-yard dash time
    weight_speed = st.number_input("Enter your weight (in pounds):", min_value=0.0, value=200.0, step=0.1, key="weight_speed")
    dash_time = st.number_input("Enter your 40-yard dash time (in seconds):", min_value=0.0, value=5.0, step=0.01, key="dash_time")

    # Calculate Speed Score
    if st.button("Calculate Speed Score", key="speed_score_button"):
        if dash_time == 0:
            st.error("40-yard dash time cannot be zero.")
        else:
            speed_score = (weight_speed * 200) / (dash_time ** 4)
            st.success(f"Your Speed Score is: **{speed_score:.2f}**")

st.write("The formula for speed score is (weight * 200) / (40-yd time ^ 4)")
    # Explanation of the formula
st.markdown("""
    - **Weight**: Your weight in pounds.
    - **40-Yard Dash Time**: Your 40-yard dash time in seconds.
    """)

# Tab 2: BMI Calculator
with tab2:
    st.header("BMI Calculator")

    # Input fields for weight and height
    weight_bmi = st.number_input("Enter your weight (in pounds):", min_value=0.0, value=150.0, step=0.1, key="weight_bmi")
    height = st.number_input("Enter your height (in inches):", min_value=0.0, value=65.0, step=0.1, key="height")

    # Calculate BMI
    if st.button("Calculate BMI", key="bmi_button"):
        if height == 0:
            st.error("Height cannot be zero.")
        else:
            bmi = (weight_bmi / (height ** 2)) * 703
            st.success(f"Your BMI is: **{bmi:.2f}**")

st.write("The formula for BMI (Body Mass Index) is (weight) / (height ^ 2) * 703")
    # Explanation of the formula
st.markdown("""
    - **Weight**: Your weight in pounds.
    - **Height**: Your height in inches.
    """)

# Tab 3: Jumping Score Calculator
with tab3:
    st.header("Jumping Score Calculator")

    # Input fields for vertical jump and broad jump
    vertical_jump = st.number_input("Enter your vertical jump (in inches):", min_value=0.0, value=20.0, step=0.1, key="vertical_jump")
    broad_jump = st.number_input("Enter your broad jump (in inches):", min_value=0.0, value=100.0, step=0.1, key="broad_jump")

    # Calculate Jumping Score
    if st.button("Calculate Jumping Score", key="jumping_score_button"):
        jumping_score = (vertical_jump * 4.25) + broad_jump
        st.success(f"Your Jumping Score is: **{jumping_score:.2f}**")

st.write("The formula for Jumping Score is vertical jump * 4.25 + broad jump")
    # Explanation of the formula
st.markdown("""
    - **Vertical Jump**: Your vertical jump height in inches.
    - **Broad Jump**: Your broad jump distance in inches.
    """)