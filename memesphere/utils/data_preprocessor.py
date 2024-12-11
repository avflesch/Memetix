import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
import logging

class DataPreprocessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.scaler = StandardScaler()
        self.stop_words = set(stopwords.words('english'))
        
        logging.info("Initializing DataPreprocessor")
    
    def preprocess_text(self, text: str) -> str:
        """
        Clean and normalize text data
        """
        doc = self.nlp(text.lower())
        tokens = [
            token.text for token in doc 
            if not token.is_stop and not token.is_punct
        ]
        return " ".join(tokens)
    
    def normalize_metrics(self, metrics: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize numerical metrics
        """
        return pd.DataFrame(
            self.scaler.fit_transform(metrics),
            columns=metrics.columns
        ) 