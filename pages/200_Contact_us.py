import streamlit as st
import pandas as pd
import os

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Contact Us",
    page_icon="../pictures/logo.png",
    layout="centered",
)

# Define columns layout
cols = st.columns([1, 2])

with cols[0]:
    st.image("./pictures/logo.png", width=170)
with cols[1]:
    st.markdown("""
    ## Law Buddy 
    ### Your AI Legal Assistant
    """)

# Sidebar information
st.sidebar.header("Contact Us")
st.sidebar.write("Feel free to reach out to us using the form below!")

# Main content
st.title("Contact Us")

st.write("We would love to hear from you! Please fill out the form below and we'll get back to you as soon as possible.")

# Form for contact
with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.selectbox("Subject", ["Get Listed as a Lawyer","General Inquiry", "Support", "Feedback", "Other"])
    message = st.text_area("Your Message")
    file_upload = st.file_uploader("Attach a file (optional)", type=["pdf", "docx", "jpg", "png"])
    
    submit_button = st.form_submit_button(label="Submit")

# Process form submission
if submit_button:
    if name and email and message:
        st.success(f"Thank you for your message, {name}! We will get back to you at {email} regarding '{subject}'.")
        
        # Save form data to CSV
        file_exists = os.path.isfile('contact_data.csv')
        with open('contact_data.csv', 'a') as f:
            if not file_exists:
                f.write("Name,Email,Subject,Message,File Upload\n")
            file_upload_name = file_upload.name if file_upload else ""
            f.write(f"{name},{email},{subject},{message},{file_upload_name}\n")
        
        if file_upload:
            st.write("You've uploaded a file:", file_upload.name)
    else:
        st.error("Please fill in all the fields.")

# Additional contact information
st.write("You can also reach us at:")
st.write("📧 Email: amankaharbusiness@gmail.com")
st.write("📞 Phone: +91 8839628882")

# Social Media Links

# Embed Google Map
st.write("Visit us at our office location:")

# Map location data
map_data = pd.DataFrame({
    'lat': [23.249838920677735],  # Replace with your latitude
    'lon': [77.52827558372536]  # Replace with your longitude
})

st.map(map_data, zoom=11)
st.write("### LNCT Group Of College, Raisen Road, Bhopal, Madhya Pradesh, India")
