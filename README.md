# HEART-DISEASE-PREDICTION
## Project description
This project aims to predict the likelihood of heart disease in patients using machine learning techniques. Specifically, it employs a genetic algorithm for feature selection and TPOT (Tree-based Pipeline Optimization Tool) for model selection and optimization. A user-friendly interface is provided to make predictions based on user input.

### Features
Genetic Algorithm for Feature Selection: Identifies the most relevant features from the dataset.
TPOT Classifier: Automatically designs and optimizes machine learning pipelines using genetic programming.
User Interface: Simple web-based interface for users to input their data and receive predictions.

#### Dataset
Ensure you have a heart disease dataset (e.g., from the UCI Machine Learning Repository). The dataset should include features such as age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, resting ECG results, maximum heart rate achieved, exercise-induced angina, ST depression induced by exercise, the slope of the peak exercise ST segment, number of major vessels, and thalassemia.

##### Model Explanation
**Genetic Algorithm**
A genetic algorithm is used for feature selection. It iteratively selects subsets of features that contribute most to predicting heart disease, optimizing the feature set to improve model performance.

**TPOT Classifier**
TPOT automates the process of machine learning pipeline design by using genetic programming. It evaluates various models and preprocessing steps to find the best combination for predicting heart disease.

**User Interface**
The user interface is built using Flask, a lightweight web framework for Python. It allows users to input their medical data and receive predictions about their heart disease risk.


###### Screenshots
Login Page : This is used to login to page
![Screenshot 2024-05-27 220040](https://github.com/Zoro0010/HEART-DISEASE-PREDICTION/assets/126344782/34494f2d-67b1-4167-a14b-6b998abcf5d9)
Home Page: A simple form where users can enter their medical information.
![Screenshot 2024-05-27 220234](https://github.com/Zoro0010/HEART-DISEASE-PREDICTION/assets/126344782/6c8a9f1e-773d-4113-9f30-24d2d4fd629e)
Results Page: Displays the prediction results and the likelihood of heart disease.
![Screenshot 2024-05-27 220417](https://github.com/Zoro0010/HEART-DISEASE-PREDICTION/assets/126344782/4e81196c-2cb3-43b2-a478-5757e0428858)
