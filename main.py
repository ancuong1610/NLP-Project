import pandas as pd
from sklearn.model_selection import train_test_split
from preprocessing import preprocess_text
from model import train_model, evaluate_model
from issue_highlighting import highlight_issues

# Load and preprocess data
data = pd.read_csv("data/academic_texts.csv")
data['cleaned'] = data['text'].apply(preprocess_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(data['cleaned'], data['label'], test_size=0.2, random_state=42)

# Train and evaluate the model
vectorizer, model = train_model(X_train, y_train)
evaluate_model(X_test, y_test, vectorizer, model)

# Highlight issues in a sample text
sample_text = "Well, like, this is kinda interesting, you know?"
issues = highlight_issues(sample_text)
print("Highlighted Issues:", issues)
