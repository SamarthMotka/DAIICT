import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import string

stopword_list = stopwords.words('english') # Import english stopwords

with open('lab1-data.json') as f:
    documents = json.load(f)

def preprocess_text(doc_text):

    # Lowecasing text
    doc_text_lowercase = doc_text.lower()

    # Remove non ascii chars
    doc_text_clean = re.sub(r'[^\x00-\x7F]+', '', doc_text_lowercase)

    # Remove html entity code
    doc_text_clean = re.sub(r'&#(\d+);', '', doc_text_clean)

    # Word tokenization
    doc_words = word_tokenize(doc_text_lowercase)

    # Remove stopwords
    doc_words_clean = [w for w in doc_words if w not in stopword_list]

    # Remove numbers 
    doc_words_clean = [w for w in doc_words_clean if not w.isdigit() and w not in string.punctuation]

    return doc_words_clean

