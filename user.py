import streamlit as st

def get_user_info():
    st.subheader("📝 Please fill your details")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    dob = st.date_input("Date of Birth")
    region = st.selectbox("Select your Region", ["USA", "Bangladesh", "Korea", "Japan", "Other"])
    return {
        "name": name,
        "phone": phone,
        "email": email,
        "dob": str(dob),
        "region": region
    }
