import streamlit as st
import pickle
import numpy as np

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
