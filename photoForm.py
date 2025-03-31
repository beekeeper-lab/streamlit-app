import streamlit as st

st.title("Photo Upload Form")

# Add labels and fields for user information
st.header("User Information")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
state = st.text_input("State")
city = st.text_input("City")

# File upload control for photo
uploaded_file = st.file_uploader("Choose a photo to upload", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded photo
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)
    st.success("Photo uploaded successfully!")