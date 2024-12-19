
# **NLP Project: Detecting Non-Academic Language in Texts**

This project uses **Natural Language Processing (NLP)** techniques to detect and highlight **non-academic language** in text data, such as filler words, colloquial expressions, and subjective phrases.

---

## **Project Structure**

```
nlp_projekt/
│
├── data/                     # Folder for datasets
│   └── akademische_texte.csv  # Input dataset (labeled)
├── main.py                   # Main script to run the project
├── preprocessing.py          # Text preprocessing functions
├── model.py                  # Model training and evaluation
├── issue_highlighting.py     # Highlighting filler words
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/ancuong1610/NLP-Project.git
```

### 2. Install Dependencies
Install the required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## **Dataset Format**

Place your input dataset in the `data/` folder. The dataset should be a CSV file named `akademische_texte.csv` with the following format:

| **text**                                      | **label** |
|----------------------------------------------|-----------|
| "Diese Analyse zeigt bedeutende Ergebnisse." | 0         |
| "Naja, das ist halt irgendwie spannend, oder?"| 1         |

- **label = 0** → Wissenschaftlicher Text  
- **label = 1** → Nicht-wissenschaftlicher Text  

---

## **How to Run**

Run the project using the following command:
```bash
python main.py
```

---

## **What the Project Does**

1. **Text Preprocessing**:
   - Converts text to lowercase.
   - Removes stopwords and irrelevant tokens.

2. **Feature Extraction**:
   - Uses **TF-IDF** (Term Frequency-Inverse Document Frequency) to convert text into numerical features.

3. **Model Training**:
   - Trains a **Logistic Regression** model to classify texts as **academic** or **non-academic**.

4. **Highlighting Issues**:
   - Detects and highlights filler words like *"halt"*, *"irgendwie"*, and *"naja"* in non-academic text.

5. **Evaluation**:
   - Outputs model accuracy and highlights issues in example texts.

---

## **Sample Output**

Beispiel-Text:
```
"Naja, das ist halt irgendwie spannend, oder?"
```

Ausgabe:
```
Hervorgehobene Probleme: ['halt', 'irgendwie']
```

---

## **Dependencies**

The project requires the following libraries:
```
pandas
scikit-learn
spacy
```

Install them using:
```bash
pip install -r requirements.txt
```

---

## **Project Structure at a Glance**

1. **main.py** → Runs the project end-to-end.  
2. **preprocessing.py** → Handles text preprocessing.  
3. **model.py** → Trains and evaluates the classification model.  
4. **issue_highlighting.py** → Detects non-academic filler words.  
5. **data/** → Folder for the input dataset.   

---

## **How to Interpret the Results**

- **Accuracy**: The percentage of texts correctly classified as academic or non-academic.  
- **Highlighted Issues**: List of problematic words like *"halt"* or *"irgendwie"* in non-academic text.  

---

## **Run and Test**

1. Ensure your dataset (`akademische_texte.csv`) is placed in the `data/` folder.  
2. Run the `main.py` script to train the model and test it.  
3. Test custom text samples to detect non-academic issues.

```bash
python main.py
```

---
