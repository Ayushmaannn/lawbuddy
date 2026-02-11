import streamlit as st
import pandas as pd
import json
import os

# File paths
LAWYERS_FILE = 'lawyers.json'
APPOINTMENTS_FILE = 'appointments.json'

def initialize_files():
    if not os.path.exists(LAWYERS_FILE):
        with open(LAWYERS_FILE, 'w') as f:
            json.dump([], f)
    
    if not os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, 'w') as f:
            json.dump([], f)

def get_lawyers():
    with open(LAWYERS_FILE, 'r') as f:
        return json.load(f)

def add_lawyer(lawyer):
    lawyers = get_lawyers()
    lawyers.append(lawyer)
    with open(LAWYERS_FILE, 'w') as f:
        json.dump(lawyers, f)

def get_appointments():
    with open(APPOINTMENTS_FILE, 'r') as f:
        return json.load(f)

def add_appointment(appointment):
    appointments = get_appointments()
    appointments.append(appointment)
    with open(APPOINTMENTS_FILE, 'w') as f:
        json.dump(appointments, f)

# Initialize files (Run this once to create empty files)
initialize_files()

# Sidebar for Navigation
st.sidebar.title("Lawyer Interaction Platform")
menu = st.sidebar.radio("Go to", ["Book Appointment", "View Appointments"])

# Book Appointment
if menu == "Book Appointment":
    st.title("Book an Appointment")
    st.write("Choose a lawyer and time slot to book your appointment.")

    # Fetch lawyers from backend
    lawyers = get_lawyers()

    for lawyer in lawyers:
        lawyer_html = f"""
        <div style='border: 1px solid #ddd; padding: 10px; margin-bottom: 10px;'>
            <img src='https://w7.pngwing.com/pngs/193/660/png-transparent-computer-icons-woman-avatar-avatar-girl-thumbnail.png' style='float: left; margin-right: 20px; width: 100px; height: 100px; object-fit: cover;' />
            <h3>{lawyer['Name']}</h3>
            <p><strong>Specialty:</strong> {lawyer['Specialty']}</p>
            <p><strong>Rating:</strong> {lawyer['Rating']} ⭐</p>
            <p><strong>Available Times:</strong> {lawyer['Available Times']}</p>
        </div>
        """
        st.markdown(lawyer_html, unsafe_allow_html=True)

    lawyer_choice = st.selectbox("Select lawyer", [lawyer['Name'] for lawyer in lawyers])
    selected_lawyer = next(lawyer for lawyer in lawyers if lawyer['Name'] == lawyer_choice)

    patient_name = st.text_input("Your Name")
    patient_email = st.text_input("Your Email")
    appointment_time = st.selectbox("Select Time Slot", selected_lawyer['Available Times'].split(", "))

    if st.button("Book Appointment"):
        add_appointment({
            "client's Name": patient_name,
            "client's Email": patient_email,
            'Lawyer': lawyer_choice,
            'Time Slot': appointment_time
        })
        st.success("Your appointment has been booked!")

# View Appointments
elif menu == "View Appointments":
    st.title("Your Appointments")

    # Fetch appointments from backend
    appointments = get_appointments()
    if len(appointments) > 0:
        appointments_df = pd.DataFrame(appointments)
        st.table(appointments_df)
    else:
        st.write("You have no appointments booked.")
