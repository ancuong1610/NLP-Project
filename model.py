from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

vectorizer = TfidfVectorizer()
model = LogisticRegression()

def train_model(X_train, y_train):
    X_train_tfidf = vectorizer.fit_transform(X_train)
    model.fit(X_train_tfidf, y_train)
    return vectorizer, model

def evaluate_model(X_test, y_test, vectorizer, model):
    X_test_tfidf = vectorizer.transform(X_test)
    predictions = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)
