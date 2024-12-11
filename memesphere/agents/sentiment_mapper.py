from transformers import pipeline
import numpy as np
from typing import Dict, List, Union
import logging
from scipy.special import softmax

class SentimentMapper:
    def __init__(self):
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        self.emotion_analyzer = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base"
        )
        
        logging.info("Initializing SentimentMapper")
    
    async def analyze_sentiment(
        self, 
        text: Union[str, List[str]]
    ) -> Dict[str, float]:
        """
        Analyze sentiment and emotions in text
        """
        sentiment = self.sentiment_analyzer(text)
        emotions = self.emotion_analyzer(text)
        
        return {
            "sentiment_score": sentiment[0]["score"],
            "sentiment_label": sentiment[0]["label"],
            "emotions": self._process_emotions(emotions[0])
        }
    
    def _process_emotions(self, emotion_data: Dict) -> Dict[str, float]:
        scores = softmax(emotion_data["scores"])
        return dict(zip(emotion_data["labels"], scores)) 