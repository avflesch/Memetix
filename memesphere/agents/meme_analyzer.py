from typing import Dict, List, Any
import numpy as np
import logging
from ..utils.embedding_generator import EmbeddingGenerator
from sklearn.cluster import DBSCAN

class MemeAnalyzer:
    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()
        self.cluster_model = DBSCAN(eps=0.3, min_samples=2)
        
        logging.info("Initializing MemeAnalyzer")
    
    def analyze_meme(self, meme_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze a single meme's characteristics and potential
        """
        embedding = self.embedding_generator.generate(meme_data['text'])
        
        return {
            "virality_score": self._calculate_virality(meme_data),
            "semantic_features": self._extract_semantic_features(embedding),
            "evolution_potential": self._assess_evolution_potential(meme_data)
        }
    
    def analyze_meme_cluster(
        self, 
        memes: List[Dict]
    ) -> Dict[str, Any]:
        """
        Analyze a cluster of related memes
        """
        embeddings = np.array([
            self.embedding_generator.generate(meme['text']) 
            for meme in memes
        ])
        
        clusters = self.cluster_model.fit_predict(embeddings)
        
        return {
            "cluster_analysis": self._analyze_clusters(clusters),
            "trend_trajectory": self._calculate_trend_trajectory(memes),
            "mutation_patterns": self._identify_mutation_patterns(memes)
        }
    
    def _calculate_virality(self, meme_data: Dict) -> float:
        engagement = meme_data.get('engagement', {})
        weights = {
            'shares': 0.5,
            'likes': 0.3,
            'comments': 0.2
        }
        
        score = sum(
            weights[metric] * engagement.get(metric, 0) 
            for metric in weights
        )
        return min(score / 1000, 1.0)
    
    def _extract_semantic_features(self, embedding: np.ndarray) -> Dict:
        return {
            "complexity": np.linalg.norm(embedding),
            "distinctiveness": self._calculate_distinct
} 