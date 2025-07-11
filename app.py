import streamlit as st
import joblib
import pandas as pd
import numpy as np
import datetime

# Load saved model, encoder, selector, and column order
model = joblib.load("./model/model.pkl")
oe = joblib.load("./model/oe.pkl")
selector = joblib.load("./model/selector.pkl")
column_order = joblib.load("./model/columns.pkl")

def averageScore(score1, score2):
    return (score1 + score2) / 2

def bucket_exp(x):
    if x <= 2:
        return '0-2'
    elif x <= 5:
        return '3-5'
    elif x <= 10:
        return '6-10'
    else:
        return '11-20'

def calculate_experience_combined(experience,cgpa, work_year):
    experience_grade = experience * cgpa
    experience_year = experience * work_year
    experience_combined = experience_year * experience_grade
    return experience_combined
    
st.set_page_config(page_title="Skill2Salary", page_icon="images/logo.png", layout="centered")

# ---------------- Title ----------------
col1, col2 = st.columns([1, 6])

with col1:
    st.image("images/logo.png", width=100)

with col2:
    st.markdown("<h1 style='padding-top: 20px;'>Skill2Salary</h1>", unsafe_allow_html=True)

st.markdown("Predict your expected salary based on your background and job details.")

# ---------------- Section: Education & Experience ----------------
st.subheader("🌍 Where are you from?")
location = st.selectbox("Location", ["USA", "India", "Germany", "Canada"])

st.subheader("📘 Education & Work Background")

col1, col2 = st.columns(2)
with col1:
    education = st.selectbox("Highest Education", ["Bachelor's", "Master's", "PhD", "High School"])
    cgpa = st.number_input("College CGPA (out of 10)", min_value=0.0, max_value=10.0, step=0.1)
    score_12th = st.number_input("12th Grade Score (%)", min_value=0.0, max_value=100.0, step=0.1)
   

with col2:
    score_10th = st.number_input("10th Grade Score (%)", min_value=0.0, max_value=100.0, step=0.1)
    experience = st.number_input("Total Work Experience (Years)", min_value=0, step=1)
    work_year = st.number_input(
        "Year of First Employment",
        min_value=1900,
        max_value=datetime.datetime.now().year,
        step=1,
        help="Enter the year you started your professional career."
    )

# ---------------- Section: Job Details ----------------
st.subheader("🏢 Job Preferences & Company Info")

col3, col4 = st.columns(2)
with col3:
    experience_level = st.selectbox("Experience Level", ["Entry-level", "Mid-level", "Senior", "Executive"])
    job_seniority_level = st.selectbox("Seniority Level in Job Title", ["Intern", "Junior", "Mid", "Senior", "Lead", "Manager", "Principal"])

with col4:
    company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
    company_location = st.selectbox("Company Location", ["USA", "India", "Germany", "Canada"])

# ---------------- Action ----------------
st.markdown("---")

# Calculate derived features
experience_bucket = bucket_exp(experience)
experience_combined = calculate_experience_combined(experience, cgpa, work_year)
avg_school_score = averageScore(score_10th, score_12th)  
 
if st.button("🔍 Predict Salary"):
    
    input_data = pd.DataFrame([{
        "education": education,
        "location": location,
        "experience_level": experience_level,
        "company_size": company_size,
        "company_location": company_location,
        "avg_school_score": avg_school_score,
        "job_seniority_level": job_seniority_level,
        "experience_bucket": experience_bucket,
        "work_year": work_year,
        "college_cgpa": cgpa,
    }])

    # Categorical and numeric separation
    cat_cols = list(oe.feature_names_in_)
    num_cols = [col for col in input_data.columns if col not in cat_cols]

    # Encode categoricals
    encoded_array = oe.transform(input_data[cat_cols])
    encoded_df = pd.DataFrame(encoded_array, columns=oe.get_feature_names_out(cat_cols))

    # Combine all features
    final_input = pd.concat([encoded_df, input_data[num_cols].reset_index(drop=True)], axis=1)

    # Ensure final column order
    for col in column_order:
        if col not in final_input.columns:
            final_input[col] = 0
    final_input = final_input[column_order]

   
    predicted_log_salary = model.predict(final_input)[0]
    salary = np.expm1(predicted_log_salary) 
    
    st.success(f"💰 Estimated Salary: ${salary:,.2f}")