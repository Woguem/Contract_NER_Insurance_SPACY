import spacy
import PyPDF2

# Extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Loading the spaCy pre-trained model
nlp = spacy.load("en_core_web_trf")

# Text processing for NER
def extract_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

# Application example
pdf_text = extract_text_from_pdf("Exemple_contrat-de-pret-frauduleux.pdf")
entities = extract_entities(pdf_text)

# Displaying extracted entities
print(entities)
