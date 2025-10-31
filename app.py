import streamlit as st

# Move page config to the very top, right after importing streamlit
st.set_page_config(page_title="AI Job Risk Analyzer", page_icon="🤖", layout="centered")

import joblib
import json
import numpy as np
import pandas as pd

# ===========================
# Load models and assets
# ===========================
@st.cache_resource
def load_model():
    model = joblib.load("models/automation_risk_model.pkl")
    encoder = joblib.load("models/label_encoder.pkl")
    return model, encoder

@st.cache_data
def load_skills():
    with open("data/job_skill_map.json", "r") as f:
        return json.load(f)

model, encoder = load_model()
job_skill_map = load_skills()

# ===========================
# Streamlit UI setup
# ===========================
st.title("🤖 AI Job Market Insight & Skill Recommender")
st.markdown("Predict **Automation Risk**, see estimated **timeline**, and discover **upskilling suggestions** to stay future-ready.")

# ===========================
# User Input
# ===========================
with st.form("job_form"):
    job_title = st.text_input("Job Title", placeholder="e.g., Data Analyst")
    industry = st.text_input("Industry", placeholder="e.g., Finance, Technology")
    company_size = st.selectbox("Company Size", ["Small", "Medium", "Large", "Unknown"])
    remote_friendly = st.selectbox("Remote Friendly", ["Yes", "No", "Unknown"])
    required_skills = st.text_area("Job Skills", placeholder="e.g., Python, SQL, Power BI, Machine Learning")
    submitted = st.form_submit_button("Analyze Job Risk")

# ===========================
# On submission
# ===========================
if submitted:
    if job_title.strip() == "" and required_skills.strip() == "":
        st.warning("Please provide at least a Job Title or Required Skills.")
    else:
        # Prepare input dataframe
        sample = pd.DataFrame([{
            "Job_Title": job_title,
            "Industry": industry,
            "Company_Size": company_size,
            "Remote_Friendly": remote_friendly,
            "Required_Skills": required_skills
        }])

        # Predict automation risk
        pred = model.predict(sample)[0]
        risk_label = encoder.inverse_transform([pred])[0]

        # Derive timeline heuristic
        timeline_map = {
            "High": "1–3 years (High likelihood of automation)",
            "Medium": "3–5 years (Moderate automation risk)",
            "Low": "5–10+ years (Relatively safe for now)"
        }
        timeline = timeline_map.get(risk_label, "Unknown")

        # Display results
        st.subheader("📊 Automation Risk Prediction")
        st.metric(label="Predicted Risk Level", value=risk_label)
        st.info(f"⏳ **Estimated Timeline:** {timeline}")

        # Recommend skills (simple match-based retrieval)
        st.subheader("💡 Recommended Upskilling Areas")
        rec_jobs = []
        for job, skills in job_skill_map.items():
            if any(s.lower() in required_skills.lower() for s in skills):
                rec_jobs.append(job)

        if rec_jobs:
            top_jobs = rec_jobs[:3]
            st.write("Based on your current skillset, you could explore:")
            for job in top_jobs:
                st.markdown(f"- **{job}** → Recommended skills: `{', '.join(job_skill_map[job][:10])}`")
        else:
            st.write("No close matches found. Consider learning:")
            st.markdown("**→ Python, Machine Learning, AI Ethics, MLOps, Prompt Engineering, Data Visualization**")

        st.success("✅ Analysis complete! Use this insight to plan your AI upskilling journey.")

# ===========================
# Footer
# ===========================
st.markdown("---")
st.caption("Built by Musab Wasiuddin")
