# **House Price Prediction (Bangalore)**

## **Overview**

This project predicts house prices in Bangalore using machine learning. A web application is built using HTML, CSS, JavaScript, and Flask to make it interactive and production-ready. The backend is powered by a Linear Regression model trained on the Bangalore housing dataset, with an accuracy of 84%-86%.

## **Problem Statement**

House buyers and sellers often find it hard to estimate a fair price for a property. This project solves that problem by using real data and a trained ML model to make quick, reliable price predictions based on a few input features.

## **Dataset**

The dataset used is the [Bangalore House Price Dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data), which includes:

- Area type
- Availability  
- Location
- Size
- Society
- Total_sqft
- Bath
- Balcony
- Price 

## **Approach**

1. **Data Cleaning**: Removed outliers, handled missing values, and converted categorical data.
2. **Feature Engineering**: Simplified location data, normalized inputs, and created new features.
3. **Model Training**: Trained a Linear Regression model on the processed data.
4. **Web App Integration**: Integrated the trained model with a Flask backend and created a simple UI using HTML, CSS, and JS.

## **Model Performance**

- **Algorithm**: Linear Regression  
- **Accuracy**: Between 84% and 86% (based on R² score and test results)  

## **Technologies Used**

- Python  
- Pandas
- NumPy
- Matplotlib
- Scikit-learn  
- Flask  
- HTML
- CSS
- JavaScript


## **How to Run**

1. **Clone the Repository**
```bash
git clone git@github.com:ar-shenoy/House_price_prediction.git
```
2. **Navigate to the Project Folder**
```bash
cd House_price_prediction
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the App**
```bash
python app.py
```
5. **Open in Browser**
```bash
Visit http://127.0.0.1:5000 
```
to use the web app.
## **Features**
-Predicts house prices in Bangalore based on user input

-Simple and fast interface using Flask

-Real-time model prediction without refreshing the page

## **Contact**
For any questions or feedback, feel free to reach out:

Name: Adarsh R Shenoy

Email: adarshrshenoy1@gmail.com

LinkedIn: https://www.linkedin.com/in/ar-shenoy

GitHub: https://github.com/ar-shenoy?tab=repositories

https://github.com/user-attachments/assets/f8d8a00c-e295-4e3d-b137-ae68e5baa45e
