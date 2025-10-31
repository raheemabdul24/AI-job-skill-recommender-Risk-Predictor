import pickle

files = [
    "risk_model.pkl",
    "timeline_model.pkl",
    "tfidf_vectorizer.pkl",
    "label_encoder.pkl",
    "le_timeline.pkl"
]

for f in files:
    try:
        with open(f, "rb") as file:
            obj = pickle.load(file)
        print(f"✅ {f} loaded successfully.")
    except Exception as e:
        print(f"❌ {f} failed to load: {e}")
