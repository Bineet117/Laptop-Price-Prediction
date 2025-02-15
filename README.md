
# 💻🧑‍💻 Predicting Laptop Prices Using Machine Learning
<!---
## 👉 Table of Contents
- [Introduction](#👉Introduction)
- [Problem Statement](#👉Problem_Statement)
- [Data Description](#Data_Description)
- [Installation](#👉Installation)
- [Usage](#👉Usage)
- [Technologies_Used](#👉Technologies_Used)
- [Screenshots](#👉Screenshots)
- [Contact_Information](#👉Contact_Information)
- [Conclusion](#👉Conclusion) --->

## 👉 Try it 
Test this app:- https://laptop--price.streamlit.app/

## 👉 Introduction
This project uses machine learning to predict laptop prices based on brand, specifications, and market trends. It helps stakeholders make informed decisions on purchasing, pricing, inventory management, and product development.



## 👉 Problem_Statement
The laptop market is influenced by brand reputation, hardware specifications, demand, and technological advancements, making price forecasting complex. Traditional methods often lack precision and adaptability. A data-driven approach using machine learning can develop robust predictive models for accurate laptop price forecasts, improving our understanding and adaptation to market dynamics.

## 👉 Data_Description

🚀 **Company :** Name of the Company

🚀 **TypeName :** Type of laptop('Notebook', 'Gaming', 'Ultrabook', '2 in 1 Convertible', 'Workstation', 'Netbook')

🚀 **Inches :** Size of the laptop(floating value)

🚀 **ScreenResolution :** The resolution of the laptop screen.

🚀 **Cpu :** The processor (CPU) specifications of the laptop.

🚀 **Ram :** The amount of RAM (random-access memory) in the laptop.

🚀 **Memory :** The storage capacity or type of memory (e.g., SSD, HDD) in the laptop.

🚀 **Gpu :** The graphics processor (GPU) specifications of the laptop.

🚀 **OpSys :** The operating system installed on the laptop.

🚀 **Weight :** The weight of the laptop, usually in kilograms or pounds.

🚀 **Price :** The price of the laptop, which is the target variable for prediction.






## 👉 Installation

Clone the repository:

```bash
   git clone https://github.com/Bineet117/Laptop-Price-Prediction.git
```

To install required libraries:

```bash
  pip install -r requirements.txt
```
 
## 👉 Usage
To run the Streamlit application:

```bash
  streamlit run app.py
```
Select the features for prediction and get the estimated laptop price.


## 👉 Technologies_Used
* Pandas
* Numpy
* math
* Matplotlib
* Seaborn
* Warnings
* Scikit-learn:
    * Linear Regression, Ridge, Lasso
    * KNeighborsRegressor
    * DecisionTreeRegressor
    * RandomForestRegressor
    * GradientBoostingRegressor
    * AdaBoostRegressor
    * ExtraTreesRegressor
    * SVR
* XGBoost (XGBRegressor)
* Metrics:
    * mean_absolute_error
    * mean_squared_error
    * r2_score
* train_test_split
* Pickle

## 👉 Insights
![Dell, Lenovo & HP has the most number of laptop (around 300)](https://github.com/Bineet117/Laptop-Price-Prediction/assets/118985862/9ee53efb-1591-46c1-926b-7ddd20768e77)
- Dell, Lenovo & HP has the most number of laptop (around 300)

![output](https://github.com/Bineet117/Laptop-Price-Prediction/assets/118985862/17a020c7-4a9c-4786-be34-5c07ae460bc0)
- By the above Scatterplot and Barplot we can clearly see that `Razer` Company has the highest price of the laptop
- Price of the laptop expect Razer company are below 1,20,000 


## 👉 Streamlit App
<img width="949" alt="image" src="https://github.com/user-attachments/assets/84945499-3e3a-4d15-bb74-81597f057659" />



## 👉 Contact_Information
For any questions or feedback, please contact me at bineetgupta117@gmail.com📧.


## 👉 Conclusion
This project aims to provide a user-friendly interface for predicting laptop prices, leveraging machine learning techniques.
