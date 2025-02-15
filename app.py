import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

# Set Page Configuration
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

# Load Data and Model
df = pickle.load(open("data.pkl", "rb"))
model = pickle.load(open("model2.pkl", "rb"))

# Sidebar Design
with st.sidebar:
    st.image("lap.png", width=250)
    st.header("💻 Laptop Price Predictor")
    st.markdown("Predict the price of a laptop based on its specifications.")
    st.markdown("---")

# Main Title
st.title("🔮 Predict Your Laptop's Price")

# User Inputs (UI Enhancements)
col1, col2 = st.columns(2)
with col1:
    company = st.selectbox("🖥️ Brand", df["Company"].unique())
    types = st.selectbox("💼 Type", df["TypeName"].unique())
    ram = st.selectbox("🛠️ RAM (GB)", sorted(df["Ram"].value_counts().index.values))
    weight = st.number_input("⚖️ Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
    screen_size = st.number_input("📏 Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1)

with col2:
    resolution = st.selectbox("🖥️ Resolution", ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    touchscreen = st.radio("📱 TouchScreen", ["YES", "NO"], horizontal=True)
    ips = st.radio("💡 IPS Panel", ["YES", "NO"], horizontal=True)
    cpu_brand = st.selectbox("🔧 CPU Brand", df["CPU Brand"].unique())
    cpu_ghz = st.selectbox("⚡ CPU GHz", sorted(df["CPU GHz"].value_counts().index.values))

# Storage & GPU
col3, col4 = st.columns(2)
with col3:
    ssd = st.selectbox("💾 SSD (GB)", sorted(df["SSD"].value_counts().index.values))
    hdd = st.selectbox("💾 HDD (GB)", sorted(df["HDD"].value_counts().index.values))

with col4:
    gpu_brand = st.selectbox("🎮 GPU Brand", df["Gpu brand"].unique())
    os = st.selectbox("🖥️ Operating System", df["os"].unique())

# Prediction Button
if st.button("💰 Predict Price"):
    # Convert categorical inputs
    touchscreen = 1 if touchscreen == "YES" else 0
    ips = 1 if ips == "YES" else 0

    # Calculate PPI
    X_res, Y_res = map(float, resolution.split("x"))
    ppi = (((X_res**2) + (Y_res**2))**0.5) / screen_size
    
    # Create DataFrame
    query = pd.DataFrame([[company, types, ram, weight, ppi, touchscreen, ips, cpu_brand, cpu_ghz, ssd, hdd, gpu_brand, os]],
                          columns=['Company', 'TypeName', 'Ram', 'Weight', 'PPI', 'TouchScreen', 'IPS',
                                   'CPU Brand', 'CPU GHz', 'SSD', 'HDD', 'Gpu brand', 'os'])

    # Predict Price
    predicted_price = np.exp(model.predict(query)[0])
    
    # Display Result
    st.success(f"💰 **Estimated Price: ₹{int(predicted_price):,}**")
