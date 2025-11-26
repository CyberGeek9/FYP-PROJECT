import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Step 1: Sample job descriptions and resume text ---
data = {
    "job_description": [
        "Looking for a Python Developer skilled in Flask, APIs, and Machine Learning",
        "We need a Data Analyst experienced in Excel, Power BI, and SQL",
        "Hiring Web Developer proficient in HTML, CSS, and JavaScript"
    ],
    "skills": [
        "Python Flask Machine Learning",
        "Excel PowerBI SQL",
        "HTML CSS JavaScript"
    ]
}

# --- Step 2: Train TF-IDF model ---
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["skills"])

# --- Step 3: Save model ---
joblib.dump(vectorizer, "trained_model.pkl")

print("✅ Model trained and saved successfully!")

