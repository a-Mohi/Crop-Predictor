# Crop Recommendation System
> A machine learning web application that predicts the most suitable crop to cultivate based on soil and weather conditions using an ML model(XGBoost).

## To Run:
```bash
python -m venv cropR
cropR\Scripts\activate 
pip install -r requirements.txt
```
```bash
streamlit run app.py
```
## Features
1. Predicts crop from seven parameters:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)
2. Interactive UI using Streamlit