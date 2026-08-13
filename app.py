
import streamlit as st
import pandas as pd
import joblib

# Load trained model
MODEL_PATH = "student_grade_prediction_model.pkl"

model = joblib.load(MODEL_PATH)


# Page configuration
st.set_page_config(
    page_title="AI Performance & Risk Prediction",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 AI Performance & Risk Prediction System")

st.write(
    "Predict a student's final grade and academic risk "
    "using demographic, behavioral, and study-related information."
)


# Risk function
def get_risk_level(grade):

    grade = grade.lower()

    if grade in ["a", "b"]:
        return "Low Risk"

    elif grade == "c":
        return "Medium Risk"

    else:
        return "High Risk"


# Input section
st.header("Student Information")


age = st.number_input(
    "Age",
    min_value=10,
    max_value=30,
    value=17
)


gender = st.selectbox(
    "Gender",
    ["female", "male", "other"]
)


school_type = st.selectbox(
    "School Type",
    ["public", "private"]
)


parent_education = st.selectbox(
    "Parent Education",
    [
        "no formal",
        "high school",
        "diploma",
        "graduate",
        "post graduate",
        "phd"
    ]
)


study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=15.0,
    value=5.0,
    step=0.1
)


attendance_percentage = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=85.0,
    step=0.1
)


internet_access = st.selectbox(
    "Internet Access",
    ["yes", "no"]
)


travel_time = st.selectbox(
    "Travel Time",
    ["<15 min", "15-30 min", "30-60 min", ">60 min"]
)


extra_activities = st.selectbox(
    "Extra Activities",
    ["yes", "no"]
)


study_method = st.selectbox(
    "Study Method",
    ["textbook", "notes", "group study", "coaching", "mixed"]
)


# Prediction button
if st.button("🔮 Predict Performance"):

    student = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "school_type": school_type,
        "parent_education": parent_education,
        "study_hours": study_hours,
        "attendance_percentage": attendance_percentage,
        "internet_access": internet_access,
        "travel_time": travel_time,
        "extra_activities": extra_activities,
        "study_method": study_method
    }])


    # Prediction
    prediction = model.predict(student)[0]

    probabilities = model.predict_proba(student)[0]

    classes = model.named_steps["classifier"].classes_


    probability_df = pd.DataFrame({
        "Grade": classes,
        "Probability": probabilities
    }).sort_values(
        "Probability",
        ascending=False
    )


    confidence = probability_df.iloc[0]["Probability"] * 100

    risk = get_risk_level(prediction)


    # Results
    st.header("Prediction Result")

    st.success(
        f"Predicted Grade: {prediction.upper()}"
    )


    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )


    if risk == "Low Risk":

        st.success(
            f"Academic Risk Level: {risk}"
        )

    elif risk == "Medium Risk":

        st.warning(
            f"Academic Risk Level: {risk}"
        )

    else:

        st.error(
            f"Academic Risk Level: {risk}"
        )


    st.subheader("Prediction Probabilities")

    st.dataframe(
        probability_df.style.format(
            {"Probability": "{:.2%}"}
        ),
        use_container_width=True
    )
