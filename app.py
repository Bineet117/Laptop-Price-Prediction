import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Laptop Price Predictor")
st.image('lap.png')



df = pickle.load(open("data.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))


company = st.selectbox("Brand" , df["Company"].unique())
types = st.selectbox("Type" , df["TypeName"].unique())
ram = st.selectbox("RAM", sorted(df["Ram"].value_counts().index.values))
weight = st.number_input("Weights")

# PPI
screen_size = st.number_input("Screen size")
resolution = st.selectbox("Resolution" , ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])


touchscreen = st.selectbox("TouchScreen", ["YES" , "NO"])
Ips = st.selectbox("IPS", ["YES" , "NO"])
cpu_brand = st.selectbox("CPU Brand", df["CPU Brand"].unique())
Cpu_GHz	 = st.selectbox("CPU GHz", sorted(df["CPU GHz"].value_counts().index.values))
Ssd = st.selectbox("SSD(in GB)", sorted(df["SSD"].value_counts().index.values))
hdd  = st.selectbox("HDD(in GB)", sorted(df["HDD"].value_counts().index.values))
Gpu_brand = st.selectbox("Gpu brand", df["Gpu brand"].unique())
os = st.selectbox("OS", df["os"].unique())


if st.button("Predict Price"):
    # pass
    ppi = None
    if touchscreen == 'YES':
        touchscreen = 1
    else:
        touchscreen = 0

    if Ips == 'YES':
        Ips = 1
    else:
        Ips = 0

    X_res = float(resolution.split("x")[0])
    Y_res = float(resolution.split("x")[1])
    ppi = (((X_res**2) + (Y_res**2))**0.5)/screen_size
    query = pd.DataFrame(data = [[company, types, ram, weight, ppi, touchscreen, Ips, cpu_brand ,Cpu_GHz, Ssd, hdd, Gpu_brand, os ]], columns=['Company', 'TypeName', 'Ram', 'Weight', 'PPI', 'TouchScreen', 'IPS',
       'CPU Brand', 'CPU GHz', 'SSD', 'HDD', 'Gpu brand', 'os'])

    st.title("Predicted Price: " + str(int(np.exp(model.predict(query)[0]))))