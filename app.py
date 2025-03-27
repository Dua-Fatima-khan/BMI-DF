import streamlit as st

# Custom page config
st.set_page_config(
    page_title=" Ultimate BMI Tracker 🏆",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for better visuals
st.markdown("""
<style>
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #4CAF50 0%, #FFC107 50%, #F44336 100%);
    }
    .st-bb {
        background-color: #f0f2f6;
    }
    .st-at {
        background-color: #ffffff;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header with emoji animation
st.title("✨ Ultimate BMI Tracker 🏆")
st.subheader("Discover Your Health Status in Seconds! ⏱️")

# Columns for better layout
col1, col2 = st.columns(2)

with col1:
    height = st.slider(
        "📏 Select your height (in cm):",
        100, 250, 175,
        help="Drag the slider to match your height"
    )
    
    # Visual height indicator
    height_visual = st.empty()
    height_bar = "▮" * int(height / 250 * 30)
    height_visual.code(f"Height: {height} cm [{height_bar}]")

with col2:
    weight = st.slider(
        "⚖️ Select your weight (in kg):",
        40, 200, 70,
        help="Drag the slider to match your weight"
    )
    
    # Visual weight indicator
    weight_visual = st.empty()
    weight_bar = "▮" * int(weight / 200 * 30)
    weight_visual.code(f"Weight: {weight} kg [{weight_bar}]")

# Calculate BMI
bmi = weight / ((height/100) ** 2)

# Colorful BMI display
bmi_color = (
    "#4CAF50" if bmi < 24.9 else
    "#FFC107" if bmi < 29.9 else
    "#F44336"
)

st.markdown(f"""
<div style="
    background: {bmi_color}20;
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 5px solid {bmi_color};
">
    <h3 style="color: {bmi_color}; margin-top: 0;">🔥 Your BMI Score: <strong>{bmi:.2f}</strong></h3>
</div>
""", unsafe_allow_html=True)

# Personalized feedback with more details
if bmi < 16:
    st.error("🚨 Severe Thinness! Please consult a healthcare professional.")
elif 16 <= bmi < 17:
    st.warning("⚠️ Moderate Thinness! Consider nutritional counseling.")
elif 17 <= bmi < 18.5:
    st.warning("🌱 Mild Thinness! Focus on nutrient-dense foods.")
elif 18.5 <= bmi < 24.9:
    st.success("✅ Healthy Range! Perfect balance, keep it up!")
elif 25 <= bmi < 29.9:
    st.warning("⚡ Overweight! Time to amp up your activity.")
elif 30 <= bmi < 34.9:
    st.error("🔥 Class I Obesity! Small changes can make big differences.")
elif 35 <= bmi < 39.9:
    st.error("🔥 Class II Obesity! Your health is worth investing in.")
else:
    st.error("🚨 Class III Obesity! Professional guidance recommended.")

# Progress bar visualization
st.write("\n")
st.write("**Your BMI Category:**")
bmi_progress = st.progress(0)
if bmi < 18.5:
    bmi_progress.progress(int((bmi/18.5)*100))
elif bmi < 24.9:
    bmi_progress.progress(int(((bmi-18.5)/(24.9-18.5)*100)+25))
elif bmi < 29.9:
    bmi_progress.progress(int(((bmi-25)/(29.9-25)*100)+60))
else:
    bmi_progress.progress(100)

# BMI chart with emoji indicators
st.write("\n")
st.write("### 📊 BMI Categories Chart")
st.markdown("""
| Category          | BMI Range       | Emoji Indicator |
|-------------------|-----------------|-----------------|
| Severe Thinness   | < 16           | 🚨🚨🚨          |
| Moderate Thinness | 16 - 16.9      | ⚠️⚠️           |
| Mild Thinness     | 17 - 18.4      | 🌱              |
| Normal range      | 18.5 - 24.9    | ✅              |
| Overweight        | 25 - 29.9      | ⚡              |
| Obesity I         | 30 - 34.9      | 🔥              |
| Obesity II        | 35 - 39.9      | 🔥🔥            |
| Obesity III       | ≥ 40           | 🚨🚨🚨          |
""")

# Tips section that changes based on BMI
st.write("\n")
st.write("### 💡 Personalized Health Tips")
tips = st.container()

if bmi < 18.5:
    tips.write("""
    - 🥑 Increase healthy fats and proteins in your diet
    - 🏋️‍♂️ Try strength training to build muscle mass
    - 🥛 Consider nutrient-dense shakes between meals
    - ⏰ Eat smaller, more frequent meals throughout the day
    """)
elif 18.5 <= bmi < 24.9:
    tips.write("""
    - 🏃‍♀️ Maintain your current activity level
    - 🥗 Keep eating a balanced diet with variety
    - 😴 Ensure you're getting 7-9 hours of sleep
    - 🧘‍♂️ Practice stress-reduction techniques
    """)
elif 25 <= bmi < 29.9:
    tips.write("""
    - 🚶‍♂️ Start with 30-minute daily walks
    - 🍎 Replace sugary drinks with water or herbal tea
    - 🍽️ Practice mindful eating (slow down, no screens)
    - 📱 Try a step-counting or food-tracking app
    """)
else:
    tips.write("""
    - 🩺 Schedule a check-up with your doctor
    - 🥦 Focus on adding vegetables before restricting foods
    - 🚶 Start with 10-minute walks, 3 times daily
    - 📅 Set small, weekly goals rather than big targets
    """)

# Footer
st.markdown("---")
st.markdown("ℹ️ Remember, BMI is just one indicator of health. Always consult with a healthcare professional for personalized advice.")
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>Built with ❤️ by Dua Fatima</small><br>
    <small>Copyright © 2025 - All Rights Reserved</small>
</div>
""", unsafe_allow_html=True)