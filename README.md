# AI Performance & Risk Prediction System

An end-to-end Machine Learning project that analyzes student academic and behavioral factors to predict final grades and assess academic risk.

## 📌 Project Overview

This project develops an AI-powered student performance prediction system using demographic, academic, attendance, and study-related features.

The system predicts a student's final grade from **A to F**, provides prediction probabilities, and classifies the student's academic risk level.

An interactive **Streamlit web application** was also developed to allow users to enter student information and receive real-time predictions.

## 🎯 Objectives

- Predict students' final academic grades.
- Analyze factors influencing student performance.
- Identify students who may be academically at risk.
- Compare multiple machine learning algorithms.
- Perform feature engineering and hyperparameter tuning.
- Develop an interactive prediction application.

## 📊 Dataset

The dataset contains student demographic, academic, and behavioral information.

### Features

- Age
- Gender
- School Type
- Parent Education
- Study Hours
- Attendance Percentage
- Internet Access
- Travel Time
- Extra Activities
- Study Method
- Mathematics Score
- Science Score
- English Score
- Overall Score

### Target

`final_grade`

Classes:

- A
- B
- C
- D
- E
- F

After data cleaning and duplicate removal, the dataset contained **15,000 unique student records**.

## 🔍 Exploratory Data Analysis

The project includes:

- Grade distribution analysis
- Study hours distribution
- Study hours vs. overall score analysis
- Correlation analysis
- Numerical feature correlation heatmap

A strong positive relationship was observed between study hours and overall score.

## ⚙️ Feature Engineering

Additional features were created to improve model performance, including:

- Study-attendance interaction
- Age groups
- Encoded categorical variables
- Numerical transformations

## 🤖 Machine Learning Models

The following models were evaluated:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting

Hyperparameter tuning was performed using cross-validation.

### Best Model

**Tuned Logistic Regression**

- Accuracy: **63.03%**
- Cross-Validation Macro F1: **0.6313**
- Best C: **10**

## 📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Cross-validation Macro F1

## 🔮 Prediction System

The system provides:

- Predicted final grade
- Prediction confidence
- Top predicted grades
- Academic risk level

Example:

```text
Predicted Grade       : C
Prediction Confidence : 74.78%
Academic Risk Level   : Medium Risk

## 🌐 Streamlit Application

An interactive Streamlit application was developed for real-time student performance prediction.

Users can enter student information and receive:

- Predicted grade
- Prediction probabilities
- Academic risk assessment

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Google Colab
- GitHub

## 📁 Project Structure

```text
AI-Performance-Risk-Prediction/
│
├── AI_Performance_Risk_Prediction.ipynb
├── app.py
├── requirements.txt
├── student_grade_prediction_model.pkl
└── README.md

🚀 How to Run
1. Clone the repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd AI-Performance-Risk-Prediction
2. Install dependencies
pip install -r requirements.txt
3. Run the Streamlit application
streamlit run app.py
🔮 Future Improvements
Improve prediction accuracy using advanced ensemble models.
Address class imbalance between grade categories.
Add explainable AI techniques.
Deploy the application using a cloud platform.
Add student performance trend analysis.
Develop early-warning notifications for high-risk students.
👩‍💻 Author

Sadia khanom Moume

Computer Science & Engineering Student

⭐ If you find this project useful, consider giving the repository a star.
