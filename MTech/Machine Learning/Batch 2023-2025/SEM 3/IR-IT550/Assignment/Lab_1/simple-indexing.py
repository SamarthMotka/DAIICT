from preprocessing import preprocess_text
import math

def create_vocab_and_tf_idf_scores(documents):
    
    idf = {} # Inverse document frequency
    df = {} # Document Frequency
    term2id = {} # Term to id mapping + Vocabulary
    id2term = {} # Id to term mapping
    tf = {}

    for doc in documents:

        doc_id = doc['id']
        
        if not isinstance(doc['text'], str): # Skip documents with missing text
            continue

        preprocessed_doc = preprocess_text(doc['text'])

        for word in preprocessed_doc:
            if word not in term2id:
                id2term[len(term2id)] = word
                term2id[word] = len(term2id)

            word_id = term2id[word]

            if word_id not in tf:
                tf[word_id] = {} # Add empty mapping when term is encountered for the first time

            tf[word_id][doc_id] = tf[word_id].get(doc_id, 0) + 1  # Update term freuency

        for unique_word in set(preprocessed_doc):
            word_id = term2id[unique_word]
            df[word_id] = df.get(word_id,0) + 1 # Update document freuency only once

    # Compute idf
    for word_id in df:
        idf[word_id] = math.log(len(documents) / float(df.get(word_id, 0) + 1))
        
    return tf, df, idf, term2id, id2term
