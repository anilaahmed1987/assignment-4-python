# BMI_Calculator.py
import streamlit as st

def calculate_bmi(weight, height):
    return weight / ((height/100) ** 2)

def bmi_category(bmi):
    if bmi < 16:
        return "Severe Thinness", "red", "⚠️ Immediate medical attention suggested"
    elif 16 <= bmi < 17:
        return "Moderate Thinness", "orange", "⚕️ Consult a healthcare provider"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness", "#FFCC00", "🍎 Consider nutritional counseling"
    elif 18.5 <= bmi < 25:
        return "Normal", "green", "🎉 Great! Maintain healthy habits"
    elif 25 <= bmi < 30:
        return "Overweight", "#FF9900", "🏃♂️ Regular exercise recommended"
    elif 30 <= bmi < 35:
        return "Obese Class I", "red", "⚕️ Consult a healthcare provider"
    elif 35 <= bmi < 40:
        return "Obese Class II", "red", "🩺 Medical intervention advised"
    else:
        return "Obese Class III", "darkred", "🚨 Urgent medical consultation needed"

# Configure page
st.set_page_config(
    page_title="Smart BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Main interface
st.title("⚖️ Smart BMI Calculator")
st.subheader("Your Health Dashboard")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", 
                               min_value=30.0, 
                               max_value=300.0,
                               value=70.0,
                               step=0.5)
    with col2:
        height = st.number_input("Height (cm)", 
                               min_value=100.0, 
                               max_value=250.0,
                               value=170.0,
                               step=0.5)

if st.button("Calculate BMI", type="primary"):
    bmi = calculate_bmi(weight, height)
    category, color, advice = bmi_category(bmi)
    
    # Display results
    st.divider()
    
    with st.container():
        st.markdown(f"<h2 style='text-align: center; color: {color};'>{bmi:.1f}</h2>", 
                    unsafe_allow_html=True)
        st.progress(min(bmi/40, 1.0))
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader(f"Category: {category}")
        with col_b:
            st.markdown(f"<p style='color:{color};font-size:20px;'>{advice}</p>", 
                       unsafe_allow_html=True)
    
    # Health recommendations
    with st.expander("📌 Personalized Health Tips"):
        if bmi < 18.5:
            st.write("""
            - Increase calorie intake with nutrient-dense foods
            - Consider weight training to build muscle mass
            - Have frequent small meals throughout the day
            """)
        elif 18.5 <= bmi < 25:
            st.write("""
            - Maintain balanced diet with regular exercise
            - Monitor weight monthly
            - Get adequate sleep (7-9 hours)
            """)
        else:
            st.write("""
            - Start with 30 minutes daily exercise
            - Reduce processed food intake
            - Track food consumption
            - Consider professional dietary consultation
            """)

st.caption("Disclaimer: This calculator is for informational purposes only. Always consult a healthcare professional for medical advice.")
