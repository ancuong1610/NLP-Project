import spacy
filler_words = ["like", "kinda", "well", "you know", "maybe"]

nlp = spacy.load("en_core_web_sm")

def highlight_issues(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if token.text in filler_words]
