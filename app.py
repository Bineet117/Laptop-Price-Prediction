import streamlit as st
import pandas as pd
import pickle
st.title("Laptop Price Prediction")

# import the model
# pipe = pickle.load(open("model1.pkl" ,"rb"))
df = pickle.load(open("data.pkl" ,"rb"))

# Brand
Company = st.selectbox("Brand",df["Company"].unique())

# type of laptop
TypeName = st.selectbox("TypeName",df["TypeName"].unique())
RAM = st.selectbox("Ram(in GB)",df["Ram"].unique())
Weight = st.number_input("Weight of the Laptop")
TouchScreen = st.selectbox("TouchScreen",["No","Yes"])
IPS = st.selectbox("IPS",["No","Yes"])


# CPU Brand
# RAM = st.selectbox("TypeName",df["TypeName"].unique())
