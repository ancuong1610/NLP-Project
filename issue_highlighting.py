import spacy

# Load spaCy model
nlp = spacy.load("de_core_news_sm")

# Dictionaries for common issues
filler_words = ["gewisse", "letztendlich", "schlussendlich", "bei Bedarf", "in der Tat"]
vague_words = ["man", "es", "ich"]
colloquialisms = ["ins Spiel kommen", "auf Herz und Nieren testen"]
complex_phrases = {"mittels": "mit", "nebst": "neben", "zu guter Letzt": "am Schluss"}

# Highlighting issues based on rules
def highlight_issues(text):
    doc = nlp(text.lower())
    issues = []

    # Check for filler words
    for token in doc:
        if token.text in filler_words:
            issues.append((token.text, "Filler Word"))

    # Check for vague words
    for token in doc:
        if token.text in vague_words:
            issues.append((token.text, "Vague Word"))

    # Check for colloquialisms
    for phrase in colloquialisms:
        if phrase in text:
            issues.append((phrase, "Colloquialism"))

    # Check for complex phrases
    for phrase, suggestion in complex_phrases.items():
        if phrase in text:
            issues.append((phrase, f"Complex Expression (suggestion: {suggestion})"))

    return issues
