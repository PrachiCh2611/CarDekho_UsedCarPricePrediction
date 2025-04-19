🚗 Car Dekho – Used Car Price Prediction:
A machine learning project designed to predict the prices of used cars using advanced regression models and deployed with an interactive Streamlit web app.

📌 Project Summary:
This project focuses on building a robust machine learning model to accurately estimate used car prices based on key features. The solution is delivered through a user-friendly Streamlit interface, allowing seamless interaction and real-time predictions.

🎯 Problem Statement & Objective:
Determining a fair price for used cars is challenging due to various influencing factors such as age, brand, mileage, fuel type, etc. The goal of this project is to create a reliable and accurate predictive model to assist buyers and sellers in making informed pricing decisions.

🧹 Data Preprocessing:
Key steps in preparing the dataset:

Price normalization and currency conversion
Encoding of categorical variables
Dropping irrelevant or redundant columns
Handling missing values and outliers using IQR techniques

📊 Exploratory Data Analysis (EDA):
EDA was conducted to understand feature relationships and data distribution:

Visualizations: Histograms, box plots, and heatmaps
Correlation analysis to find influential features
Outlier detection using statistical methods
Feature scaling and transformation

🤖 Model Building:
The following regression models were evaluated:

Linear Regression (Baseline)
Decision Tree Regressor
Random Forest Regressor ✅ (Best Performer)
Gradient Boosting Regressor

Models were optimized using cross-validation and hyperparameter tuning.

📈 Model Evaluation:
Metrics used:

MSE (Mean Squared Error)
MAE (Mean Absolute Error)
R² Score (Coefficient of Determination)

🏆 Random Forest Regressor was chosen for its high accuracy, stability, and performance across metrics.

🌐 Web App Deployment (Streamlit):
Deployed using Streamlit, the app includes:

Dropdowns and sliders for user input
Real-time price prediction output
Visual insights explaining prediction factors
Option to download search results for reference

🧠 Why Random Forest?::
Excellent generalization and accuracy

Handles both numeric and categorical variables well
Reduces risk of overfitting
Superior overall performance

🔮 Conclusion & Future Scope:
This project delivers a practical tool for pricing used cars and improves decision-making for users. Future upgrades may include:

Integration of insurance and seller history data
Custom models for different cities/regions
Continuous learning from newly collected data

🎥 Project Demo::
Watch a short video documentation of the project:
📎 Click here

🚀 Tech Stack:
Python
Pandas, NumPy, Matplotlib, Seaborn
Scikit-learn
Streamlit


