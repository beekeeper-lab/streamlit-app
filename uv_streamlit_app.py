import streamlit as st
import requests

def fetch_uv_index(location):
    # Replace with a real API endpoint and API key
    api_url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={location}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('current', {}).get('uv', 'No UV data available')
    else:
        return "Error fetching UV data"

st.title("UV Index Checker")

location = st.text_input("Enter a location (e.g., city or coordinates):")

if location:
    uv_index = fetch_uv_index(location)
    st.write(f"The UV index for {location} is: {uv_index}")