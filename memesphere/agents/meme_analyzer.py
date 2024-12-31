from typing import Dict, List, Any, Optional
import numpy as np
import logging
from ..utils.embedding_generator import EmbeddingGenerator
from sklearn.cluster import DBSCAN
from dataclasses import dataclass

@dataclass
class ViralityMetrics:
    score: float
    engagement_ratio: float
    velocity: float
    peak_performance: float

class MemeAnalyzer:
    def __init__(
        self, 
        eps: float = 0.3, 
        min_samples: int = 2,
        engagement_threshold: float = 1000
    ):
        self.embedding_generator = EmbeddingGenerator()
        self.cluster_model = DBSCAN(eps=eps, min_samples=min_samples)
        self.engagement_threshold = engagement_threshold
        
        logging.info(
            f"Initializing MemeAnalyzer with eps={eps}, "
            f"min_samples={min_samples}, "
            f"engagement_threshold={engagement_threshold}"
        )
    
    def analyze_meme(self, meme_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze a single meme's characteristics and potential
        
        Args:
            meme_data: Dictionary containing meme metadata and content
            
        Returns:
            Dictionary containing analysis metrics and predictions
        """
        embedding = self.embedding_generator.generate(meme_data['text'])
        temporal_features = self._extract_temporal_features(meme_data)
        
        return {
            "virality_metrics": self._calculate_virality(meme_data),
            "semantic_features": self._extract_semantic_features(embedding),
            "evolution_potential": self._assess_evolution_potential(meme_data),
            "temporal_patterns": temporal_features,
            "risk_score": self._calculate_risk_score(temporal_features)
        }
    
    def analyze_meme_cluster(
        self, 
        memes: List[Dict],
        min_cluster_size: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Analyze a cluster of related memes with enhanced metrics
        
        Args:
            memes: List of meme dictionaries
            min_cluster_size: Minimum size for valid clusters
            
        Returns:
            Dictionary containing cluster analysis and trends
        """
        if not memes:
            return {"error": "Empty meme list provided"}
            
        embeddings = np.array([
            self.embedding_generator.generate(meme['text']) 
            for meme in memes
        ])
        
        clusters = self.cluster_model.fit_predict(embeddings)
        
        return {
            "cluster_analysis": self._analyze_clusters(clusters, min_cluster_size),
            "trend_trajectory": self._calculate_trend_trajectory(memes),
            "mutation_patterns": self._identify_mutation_patterns(memes),
            "cluster_health": self._assess_cluster_health(clusters),
            "virality_distribution": self._analyze_virality_distribution(memes)
        }
    
    def _calculate_virality(self, meme_data: Dict) -> ViralityMetrics:
        """Calculate comprehensive virality metrics"""
        engagement = meme_data.get('engagement', {})
        weights = {
            'shares': 0.5,
            'likes': 0.3,
            'comments': 0.2,
            'saves': 0.4  # New metric
        }
        
        raw_score = sum(
            weights[metric] * engagement.get(metric, 0) 
            for metric in weights
        )
        
        normalized_score = min(raw_score / self.engagement_threshold, 1.0)
        
        return ViralityMetrics(
            score=normalized_score,
            engagement_ratio=self._calculate_engagement_ratio(engagement),
            velocity=self._calculate_velocity(meme_data),
            peak_performance=self._calculate_peak_metrics(engagement)
        )
