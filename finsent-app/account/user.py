# import streamlit as st
# import requests

# def login(username, password):
#     response = requests.post('http://your-flask-api/login', json={'username': username, 'password': password})
#     if response.status_code == 200:
#         st.success("Login successful!")
#     else:
#         st.error("Invalid username/password")

# def signup(username, password):
#     response = requests.post('http://your-flask-api/signup', json={'username': username, 'password': password})
#     if response.status_code == 200:
#         st.success("Signup successful!")
#     else:
#         st.error("Signup failed. Username may already exist.")

# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     login(username, password)

# if st.button("Signup"):
#     signup(username, password)
