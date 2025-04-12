# simple_website.py
import streamlit as st
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Tech Solutions Inc.",
    page_icon="💻",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>
    .main {background: #f8f9fa;}
    .stButton>button {background-color: #4CAF50; color: white;}
    .stTextInput>div>div>input {border-radius: 5px;}
    .highlight {background-color: #e9f5ff; padding: 15px; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Page content
with st.container():
    st.title("🚀 Tech Solutions Inc.")
    st.subheader("Your Digital Transformation Partner")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800", 
            caption="Innovation at its Best")

# Services section
with st.container():
    st.header("Our Services")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("### 🔐 Cybersecurity")
        st.write("Enterprise-grade security solutions")
    with cols[1]:
        st.markdown("### ☁️ Cloud Solutions")
        st.write("AWS/Azure migration & management")
    with cols[2]:
        st.markdown("### 🤖 AI Integration")
        st.write("Custom ML solutions implementation")

# Interactive demo
with st.expander("💡 Try Our ROI Calculator", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        employees = st.slider("Number of Employees", 10, 1000, 100)
        current_cost = st.number_input("Current IT Costs ($)", 10000, 1000000, 50000)
    with col2:
        st.metric("Estimated Savings", f"${employees*150:,.0f}")
        st.progress(employees/1000)

# Contact form
with st.form("contact_form"):
    st.header("📬 Contact Us")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    message = st.text_area("Message")
    
    if st.form_submit_button("Send Message"):
        st.success(f"Thank you {name}! We'll respond within 24 hours.")

# Dynamic content
with st.container():
    st.header("📍 Our Locations")
    locations = pd.DataFrame({
        'lat': [37.7749, 40.7128],
        'lon': [-122.4194, -74.0060],
        'city': ['San Francisco', 'New York']
    })
    st.map(locations, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 Tech Solutions Inc. • All rights reserved")
