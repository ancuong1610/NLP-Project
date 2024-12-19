import spacy

# Load the German language model
nlp = spacy.load("de_core_news_sm")  # Use spaCy's German model

# Function to preprocess German text
def preprocess_text(text):
    """
    Preprocesses input German text by:
    - Converting the text to lowercase
    - Removing stopwords (e.g., "und", "oder")
    - Removing non-alphabetic tokens (e.g., numbers, punctuation)
    - Returning the cleaned text as a single string
    """
    doc = nlp(text.lower())  # Lowercase and process text with spaCy
    tokens = [token.text for token in doc if token.is_alpha and not token.is_stop]  # Filter tokens
    return " ".join(tokens)  # Join tokens into a cleaned string
