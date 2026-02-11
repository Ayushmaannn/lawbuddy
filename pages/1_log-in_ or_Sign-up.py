import streamlit as st
import hashlib

# from firebase_admin import credentials, auth, firestore

# cred = credentials.Certificate('law_buddhi-main\law_buddhi-main\law-buddy-2526b-296bbb210146.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# def signup_user(email, password):
#     try:
#         user = auth.create_user(email=email, password=password)
#         st.success("User created successfully!")
#         return user
#     except Exception as e:
#         st.error(f"Error: {e}")

# def login_user(email, password):
#     try:
#         user = auth.get_user_by_email(email)

#         st.success(f"Logged in as: {user.email}")
#         return user
#     except Exception as e:
#         st.error(f"Login failed: {e}")

# def save_user_to_firestore(user_id, user_data):
#     try:
#         db.collection('users').document(user_id).set(user_data)
#         st.success("User data saved!")
#     except Exception as e:
#         st.error(f"Error saving data: {e}")


# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to authenticate user credentials
def authenticate(username, password):
    if username in st.session_state['users']:
        hashed_password = hash_password(password)
        if st.session_state['users'][username]['password'] == hashed_password:
            return True
    return False

# Initialize session state for users and authentication
if 'users' not in st.session_state:
    st.session_state['users'] = {}

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'login'  # Default to login page

# Function to switch between pages
def switch_page(page):
    st.session_state['current_page'] = page  # No need for experimental_rerun, Streamlit will re-render

# Sign-up page
def sign_up_page():
    st.title("Sign Up")
    
    # Input fields for sign-up form
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")

    if st.button("Sign Up"):
        if username in st.session_state['users']:
            st.error("Username already exists! Please choose a different one.")
        elif password != confirm_password:
            st.error("Passwords do not match!")
        else:
            # Hash the password and store it
            st.session_state['users'][username] = {
                'password': hash_password(password)
            }
            st.success("User signed up successfully!")

            st.session_state['authenticated'] = True
            switch_page('main_app')

    st.write("Already have an account? [Sign In](#)", unsafe_allow_html=True)
    if st.button("Go to Sign In"):
        switch_page('login')

# Login page
def login_page():
    st.title("Login")
    # Input fields for login form
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In"):
        if authenticate(username, password):
            st.success("Logged in successfully!")
            st.session_state['authenticated'] = True
            switch_page('main_app')
        else:
            st.error("Invalid username or password")

    st.write("Don't have an account? [Sign Up](#)", unsafe_allow_html=True)
    if st.button("Go to Sign Up"):
        switch_page('signup')

# Main app after login
def main_app():
    st.title("Welcome to the Lawyer Interaction Platform")
    st.write("You are now logged in.")
    
    if st.button("Log Out"):
        st.session_state['authenticated'] = False
        switch_page('login')

# Main logic to render appropriate page based on session state
if st.session_state['authenticated']:
    main_app()
else:
    if st.session_state['current_page'] == 'login':
        login_page()
    elif st.session_state['current_page'] == 'signup':
        sign_up_page()

