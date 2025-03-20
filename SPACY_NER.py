import spacy
from spacy import displacy
import pandas as pd
import PyPDF2

# Extraction du texte depuis un fichier PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Chargement du modèle pré-entraîné spaCy
nlp = spacy.load("en_core_web_trf")

# Traitement du texte pour NER
def extract_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

# Exemple d'application
pdf_text = extract_text_from_pdf("Exemple_contrat-de-pret-frauduleux.pdf")
entities = extract_entities(pdf_text)

# Affichage des entités extraites
print(entities)
