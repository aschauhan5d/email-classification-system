from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Initialize model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000))
])

# Categories
CATEGORIES = ["Billing", "Technical", "Account", "General"]

def predict_category(text: str) -> str:
    """Predict email category with fallback logic"""
    try:
        return CATEGORIES[model.predict([text])[0]]
    except:
        text = text.lower()
        if any(x in text for x in ["bill", "payment"]):
            return "Billing"
        elif any(x in text for x in ["error", "bug"]):
            return "Technical"
        elif any(x in text for x in ["account", "login"]):
            return "Account"
        return "General"