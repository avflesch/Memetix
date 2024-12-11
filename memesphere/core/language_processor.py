import spacy
import nltk
from typing import List, Dict, Any
import logging
from transformers import pipeline

class LanguageProcessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.summarizer = pipeline("summarization")
        self.ner = pipeline("ner")
        
        logging.info("Initializing LanguageProcessor")
        
    def process_text(self, text: str) -> Dict[str, Any]:
        """
        Comprehensive text processing
        """
        doc = self.nlp(text)
        
        return {
            "tokens": [token.text for token in doc],
            "entities": self._extract_entities(text),
            "summary": self._generate_summary(text),
            "syntax_tree": self._parse_syntax(doc)
        }
    
    def _extract_entities(self, text: str) -> List[Dict]:
        return self.ner(text)
    
    def _generate_summary(self, text: str) -> str:
        if len(text.split()) > 50:
            return self.summarizer(text, max_length=130, min_length=30)[0]['summary_text']
        return text
    
    def _parse_syntax(self, doc) -> List[Dict]:
        return [{
            "text": token.text,
            "pos": token.pos_,
            "dep": token.dep_
        } for token in doc] 