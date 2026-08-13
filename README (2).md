# AI-Powered Performance & Risk Prediction System

An end-to-end Machine Learning project for predicting student final grades
and identifying academic risk using demographic, behavioral, and study-related features.

## Project Overview

This project predicts a student's final grade (A-F) using early-stage information
such as study hours, attendance, school type, parental education, internet access,
travel time, extracurricular activities, and study method.

The project intentionally excludes final subject scores and overall score to
avoid data leakage and simulate an early academic risk prediction scenario.

## Dataset

- Original records: 25,000
- Unique students after cleaning: 15,000
- Features: 11 predictive features
- Target: Final Grade (A-F)
- Missing values: 0
- Duplicate rows after cleaning: 0

## Machine Learning Models

The following models were evaluated:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting
4. Feature-Engineered Logistic Regression
5. Tuned Logistic Regression

## Best Model

Tuned Logistic Regression

- Accuracy: 63.03%
- Macro F1-score: 0.63
- Best C parameter: 10

## Key Findings

Study hours and attendance percentage were the most influential
predictive features in the trained Logistic Regression model.

The model also showed that adjacent grades such as B/C and D/E
were the most commonly confused classes.

## Academic Risk Prediction

The system maps predicted grades to academic risk levels:

- A / B → Low Risk
- C → Medium Risk
- D / E / F → High Risk

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Google Colab
- Streamlit

## Project Structure

AI_Performance_Risk_Prediction/
│
├── AI_Performance_Risk_Prediction.ipynb
├── Student_Performance_Cleaned.csv
├── student_grade_prediction_model.pkl
├── requirements.txt
├── README.md
└── app.py

## Prediction Output

The system provides:

- Predicted final grade
- Prediction confidence
- Academic risk level
- Top predicted grades with probabilities

## Future Improvements

- Hyperparameter optimization
- Advanced class imbalance techniques
- More diverse student datasets
- Explainable AI techniques
- Interactive Streamlit dashboard
- Model deployment

## Author

CSE Student | Machine Learning & AI Enthusiast