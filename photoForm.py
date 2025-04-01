import streamlit as st
import requests

st.title("Photo Upload Form")

# Add labels and fields for user information
st.header("User Information")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
state = st.text_input("State")
city = st.text_input("City")

# File upload control for photo
uploaded_file = st.file_uploader("Choose a photo to upload", type=["jpg", "jpeg", "png"])

# Add a submit button
if st.button("Submit"):
    if first_name and last_name and state and city and uploaded_file:
        # Prepare the data to send to the web service
        files = {"file": uploaded_file.getvalue()}
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "state": state,
            "city": city
        }

        # Replace 'http://example.com/api/upload' with the actual web service URL
        response = requests.post("http://example.com/api/upload", data=data, files=files)

        if response.status_code == 200:
            st.success("Form submitted successfully!")
        else:
            st.error(f"Failed to submit form: {response.status_code}")
    else:
        st.warning("Please fill out all fields and upload a photo before submitting.")