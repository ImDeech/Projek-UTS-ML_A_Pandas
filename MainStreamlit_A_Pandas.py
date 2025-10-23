import pandas as pd
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

#Navigasi sidebar
with st.sidebar:
    selected = option_menu ('UTS Machine Learning 25/26',
['Klasifikasi',
'Regresi'],
default_index=0)

#Load model
model = pickle.load(open('BestModel_CLF_GB_Pandas.pkl', 'rb'))

#Halaman Klasifikasi
if selected == 'Klasifikasi':
    st.title("Prediksi Klasifikasi Gempa dan Tsunami")

    #Upload dataset
    file = st.file_uploader("Upload Dataset Gempa (CSV)", type=["csv"])

    #Input manual fitur
    st.write('Input data')
    magnitude = st.number_input("Magnitudo", min_value=0.0, step=0.1)
    cdi = st.number_input("CDI (Community Determined Intensity)", min_value=0.0, step=0.1)
    mmi = st.number_input("MMI (Modified Mercalli Intensity)", min_value=0.0, step=0.1)
    sig = st.number_input("Significance (Skor Signifikansi Gempa)", min_value=0.0, step=1.0)
    depth = st.number_input("Depth (Kedalaman)", min_value=0.0, step=1.0)
    latitude = st.number_input("Latitude (Jarak)", min_value=-90.0, max_value=90.0, step=0.1)
    longitude = st.number_input("Longitude (Bujur)", min_value=-180.0, max_value=180.0, step=0.1)

    #Prediksi
    if st.button("Prediksi"):
        input_data = np.array([[magnitude, cdi, mmi, sig, depth, latitude, longitude]])
        prediction = model.predict(input_data)
        result = "Berpotensi Tsunami 🌊" if prediction[0] == 1 else "Tidak Berpotensi Tsunami ✅"
        st.success(f"Hasil Prediksi: **{result}**")

#Halaman Regresi
if selected == 'Regresi':
    st.title("📈 Estimasi Dampak Gempa")

    magnitude = st.slider("Magnitude (Skala Richter)", 0.0, 10.0, 5.0, 0.1)
    depth = st.slider("Depth (Kedalaman, km)", 0.0, 700.0, 50.0, 1.0)

    if st.button("Hitung Estimasi Dampak"):
        impact_score = magnitude * (100 - (depth / 10))
        st.write(f"Estimasi Dampak: **{impact_score:.2f}**")
