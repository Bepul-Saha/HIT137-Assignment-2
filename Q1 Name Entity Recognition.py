import spacy

# Load scispaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")

# Hugging Face BioBERT
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline

biobert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
biobert_model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
ner_biobert = pipeline("ner", model=biobert_model, tokenizer=biobert_tokenizer)

def extract_entities(text_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # scispaCy NER (diseases and drugs)
    doc_sm = nlp_sci_sm(text)
    doc_bc5cdr = nlp_bc5cdr_md(text)
    
    sci_sm_entities = [(ent.text, ent.label_) for ent in doc_sm.ents]
    bc5cdr_entities = [(ent.text, ent.label_) for ent in doc_bc5cdr.ents]
    
    # BioBERT NER
    bio_entities = ner_biobert(text)

    return sci_sm_entities, bc5cdr_entities, bio_entities

# Usage
sci_sm_entities, bc5cdr_entities, bio_entities = extract_entities('all_texts.txt')

# Compare and analyze entities
print("scispaCy sm model entities:", sci_sm_entities[:10])
print("scispaCy BC5CDR model entities:", bc5cdr_entities[:10])
print("BioBERT entities:", bio_entities[:10])
