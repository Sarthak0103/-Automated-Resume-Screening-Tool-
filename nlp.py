import spacy
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Load the spaCy NLP model (you can use 'en_core_web_sm' or 'en_core_web_md')
nlp = spacy.load('en_core_web_sm')

# Sample keyword list for job skills (expand this with job-specific keywords)
keywords = ['python', 'data analysis', 'nlp', 'flask', 'pandas', 'sql', 'machine learning']

def extract_keywords(text):
    """Extract keywords from the text using NLP and return them."""
    doc = nlp(text.lower())
    return [token.text for token in doc if token.text in keywords]

def score_resume(resume_text, job_description):
    """Score the resume by matching the extracted keywords with the job description."""
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    
    # Calculate match score (e.g., percentage of matching keywords)
    matched_keywords = set(resume_keywords) & set(job_keywords)
    score = len(matched_keywords) / len(keywords) * 100 if keywords else 0
    
    return score, matched_keywords
