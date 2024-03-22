import streamlit as st
import pandas as pd
import pickle
st.title("Laptop Price Prediction")

# import the model
# pipe = pickle.load(open("model1.pkl" ,"rb"))
df = pickle.load(open("data.pkl" ,"rb"))

# # Brand
# Company = st.selectbox("Brand",df["Company"].unique())

# # type of laptop
# TypeName = st.selectbox("TypeName",df["TypeName"].unique())
# RAM = st.selectbox("Ram(in GB)",df["Ram"].unique())
# Weight = st.number_input("Weight of the Laptop")
# TouchScreen = st.selectbox("TouchScreen",["No","Yes"])
# IPS = st.selectbox("IPS",["No","Yes"])


# CPU Brand
# RAM = st.selectbox("TypeName",df["TypeName"].unique())


# import streamlit as st
# import pandas as pd
# import pickle

# st.title("Laptop Price Prediction")

# # Load the DataFrame
# df = pickle.load(open("data.pkl" ,"rb"))

# # Brand
# company_options = df["Company"].unique()
# company = st.selectbox("Brand", company_options)

# # Type of laptop
# type_options = df["TypeName"].unique()
# laptop_type = st.selectbox("Type", type_options)

# # RAM
# ram_options = df["Ram"].unique()
# ram = st.selectbox("RAM (in GB)", ram_options)

# # Weight
# weight = st.number_input("Weight of the Laptop")

# # Touchscreen
# touchscreen_options = ["No", "Yes"]
# touchscreen = st.selectbox("TouchScreen", touchscreen_options)

# # IPS
# ips_options = ["No", "Yes"]
# ips = st.selectbox("IPS", ips_options)

# # Add more input fields as necessary for your model

# # Button to trigger prediction
# if st.button("Predict"):
#     # Perform prediction using your model and selected features
#     # prediction = pipe.predict([[company, laptop_type, ram, weight, touchscreen, ips]])
#     # st.write("Predicted price:", prediction)
#     st.write("Prediction button clicked!")
