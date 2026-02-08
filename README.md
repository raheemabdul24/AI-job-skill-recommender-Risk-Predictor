# AI-Job-market-insight-skill-recommender
# 🤖 AI Job Market Insight & Skill Recommender

An intelligent web application built with **Streamlit** that helps users:
- Predict **Automation Risk** for any job title  
- Estimate **AI impact timelines**  
- Get **personalized skill recommendations** for future-proofing their careers  

This system combines **machine learning**, **AI job trend analysis**, and **career recommendation modeling** to deliver real-time, actionable insights.

---

## 🚀 Features

- 🔍 Predict the likelihood of job automation  
- 🧠 Understand skill importance in the AI era  
- 💡 Get personalized **upskilling recommendations**  
- 📊 Interactive, minimal UI powered by Streamlit  

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Frontend/UI** | Streamlit (Dark-themed interactive dashboard) |
| **Modeling** | Scikit-learn pipelines, XGBoost |
| **Data Handling** | Pandas, NumPy |
| **Serialization** | Joblib |
| **Visualization** | Matplotlib, Seaborn |
| **NLP** | NLTK (for text preprocessing, skill normalization) |

---

## 🧠 Algorithms & Models Used

1. **Logistic Regression / Random Forest Classifier**  
   Used to predict the **Automation Risk** score for a given job based on job title, skills, industry, and company attributes.

2. **XGBoost Model (optional upgrade)**  
   Improves prediction accuracy on large job-market datasets by leveraging gradient boosting.

3. **OneHotEncoder + ColumnTransformer Pipeline**  
   Encodes categorical job data (industry, size, remote) into numeric form for ML compatibility.

4. **Skill Recommendation Engine**  
   Built from a **Job–Skill mapping JSON**, recommending skills aligned with the AI future landscape.

---

## 📘 Example Inputs (Try These in App)

| Job Title | Industry | Company Size | Remote | Job Skills |
|------------|-----------|---------------|----------|-------------|
| Marketing Manager | Advertising | Small | Yes | Social Media, SEO, Analytics |
| Data Analyst | Finance | Medium | No | Python, SQL, Power BI, Excel |
| HR Specialist | Human Resources | Large | Yes | Communication, Recruitment, Excel |
| Software Engineer | Technology | Medium | Yes | Python, Machine Learning, APIs |
| Graphic Designer | Creative | Small | No | Photoshop, Illustrator, Branding |

---

## ⚙️ Installation

Clone this repository and set up your environment:

```bash
git clone https://github.com/your-username/ai-job-market-insight.git
cd ai-job-market-insight
```
Install dependencies:
```
pip install -r requirements.txt
```

▶️ Run the App

Run the Streamlit application locally:
```
streamlit run app.py
```

The app will open in your browser at:
👉 http://localhost:8501

📂 Project Structure
```
ai-job-market-insight/
│
├── app.py                          # Main Streamlit app
├── models/
│   ├── automation_risk_model.pkl    # Trained ML model
│   └── encoder.pkl                  # Column transformer encoder
│
├── data/
│   ├── ai_job_market_insights.csv
│   └── AI-based Career Recommendation System.csv
│
├── job_skill_map.json              # Job-to-skill mapping
├── requirements.txt
└── README.md
```

💡 Future Enhancements:
=Integrate real-time job trend APIs
=Add Llama 3.1 / GPT-based skill recommendation
=Visualize AI risk heatmaps by job category
=Export personalized upskilling reports (PDF)


🧾 License:
This project is licensed under the MIT License – you’re free to use, modify, and distribute with attribution.


👨‍💻 Author:
Developed by Abdul Raheem
💼 Passionate about AI, automation, and skill intelligence systems.
📧 Feel free to reach out for collaboration or feedback!
