import streamlit as st
import pickle
import numpy as np
import requests

API_KEY = "24603fceab3e89eb912ebec4fb76e4a1"  # Replace with your actual Weatherstack API key


def get_weather(city):
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("success", True) is False:
            return None
        current = data["current"]
        location = data["location"]
        return {
            "city": location["name"],
            "country": location["country"],
            "temperature": current["temperature"],
            "humidity": current["humidity"],
            "wind_speed": current["wind_speed"],
            "wind_dir": current["wind_dir"],
            "cloudcover": current["cloudcover"],
            "description": current["weather_descriptions"][0],


        }
    return None


# Streamlit UI
st.header("🌤️ Live Weather Window")

city = st.text_input("Enter city name:", "")

if city:
    weather = get_weather(city)
    if weather:
        st.subheader(f"Weather in {weather['city']}, {weather['country']}")

        st.markdown(f"""
  
        - 🌡️ **Temperature**: {weather['temperature']} °C  
        - 💧 **Humidity**: {weather['humidity']} %  
        - 🌬️ **Wind**: {weather['wind_speed']} km/h {weather['wind_dir']}  
        - ☁️ **Cloud Cover**: {weather['cloudcover']} %  
        - 🌥️ **Condition**: {weather['description']}
        """)
    else:
        st.error("Could not fetch weather data. Check city name or API key.")

# Load the trained model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)


def float_input(label, placeholder):
    val = st.text_input(label, placeholder=placeholder)
    try:
        return float(val)
    except:
        return None


# Label mapping (replace these with your actual crop names in correct order)
crop_labels = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean',
    'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon',
    'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'
]

# Streamlit app layout
st.title("🌽 Crop Recommendation System")

st.write("Enter the following details to predict the most suitable crop for cultivation:")

# Collecting user input
N = float_input("Nitrogen (N)", "")
P = float_input("Phosphorous (P)", "")
K = float_input("Potassium (K)", "")
temperature = float_input("Temperature (°C)", "")
humidity = float_input("Humidity (%)", "")
ph = float_input("Soil pH", "")
rainfall = float_input("Rainfall (mm)", "")

if st.button("Predict Crop"):
    if None in [N, P, K, temperature, humidity, ph, rainfall]:
        st.warning("Please fill all the fields with valid numeric values.")
    else:
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)
        crop_name = crop_labels[prediction[0]]
        st.success(f"Recommended Crop: **{crop_name.capitalize()}**")
