
# 💻🧑‍💻 Predicting Laptop Prices Using Machine Learning
<!---
## 👉Table of Contents
- [Introduction](#👉Introduction)
- [Problem Statement](#👉Problem_Statement)
- [Data Description](#Data_Description)
- [Installation](#👉Installation)
- [Usage](#👉Usage)
- [Technologies_Used](#👉Technologies_Used)
- [Screenshots](#👉Screenshots)
- [Contact_Information](#👉Contact_Information)
- [Conclusion](#👉Conclusion) --->

## 👉Introduction
This project uses machine learning to predict laptop prices based on brand, specifications, and market trends. It helps stakeholders make informed decisions on purchasing, pricing, inventory management, and product development.



## 👉Problem_Statement
The laptop market is influenced by brand reputation, hardware specifications, demand, and technological advancements, making price forecasting complex. Traditional methods often lack precision and adaptability. A data-driven approach using machine learning can develop robust predictive models for accurate laptop price forecasts, improving our understanding and adaptation to market dynamics.

## Data_Description

- **Company :** Name of the Company

- **TypeName :** Type of laptop('Notebook', 'Gaming', 'Ultrabook', '2 in 1 Convertible', 'Workstation', 'Netbook')

- **Inches :** Size of the laptop(floating value)

- **ScreenResolution :** The resolution of the laptop screen.

- **Cpu :** The processor (CPU) specifications of the laptop.

- **Ram :** The amount of RAM (random-access memory) in the laptop.

- **Memory :** The storage capacity or type of memory (e.g., SSD, HDD) in the laptop.

- **Gpu :** The graphics processor (GPU) specifications of the laptop.

- **OpSys :** The operating system installed on the laptop.

- **Weight :** The weight of the laptop, usually in kilograms or pounds.

- **Price :** The price of the laptop, which is the target variable for prediction.






## 👉Installation

To install required libraries:

```bash
  pip install -r requirements.txt
```
 
## 👉Usage
To run the Streamlit application:

```bash
  streamlit run app.py
```
Select the features for prediction and get the estimated laptop price.


## 👉Technologies_Used
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
## 👉Screenshots

<div style="display:flex; justify-content:space-between;">
  <img src="https://github.com/Bineet117/Laptop-Price-Prediction/assets/118985862/8a41b119-1914-46cf-b24d-6ae779ca9517" alt="Screenshot 1" width="400"/>
  <img src="https://github.com/Bineet117/Laptop-Price-Prediction/assets/118985862/12cfd0c6-40b8-45de-90ad-459f7ace49d7" alt="Screenshot 2" width="400"/>
</div>


## 👉Contact_Information
For any questions or feedback, please contact me at bineetgupta117@gmail.com📧.


## 👉Conclusion
This project aims to provide a user-friendly interface for predicting laptop prices, leveraging machine learning techniques.
