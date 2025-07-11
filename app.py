import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Label mapping (replace these with your actual crop names in correct order)
crop_labels = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean',
    'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon',
    'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'
]

# Streamlit app layout
st.title("Crop Recommendation System")

st.write("Enter the following details to predict the most suitable crop for cultivation:")

# Collecting user input
N = st.number_input("Nitrogen content (N)", 0.0, 150.0, step=1.0)
P = st.number_input("Phosphorous content (P)", 0.0, 150.0, step=1.0)
K = st.number_input("Potassium content (K)", 0.0, 200.0, step=1.0)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, step=0.1)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, step=0.1)
ph = st.number_input("Soil pH value", 0.0, 14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, step=1.0)

if st.button("Predict Crop"):
    # Format input data
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    # Predict
    prediction = model.predict(input_data)
    crop_name = crop_labels[prediction[0]]
    st.success(f" Recommended Crop: **{crop_name.capitalize()}**")
