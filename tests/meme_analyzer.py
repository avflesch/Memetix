import pytest
import numpy as np
from unittest.mock import Mock, patch
from typing import List, Dict

from your_project.meme_analyzer import MemeAnalyzer, ViralityMetrics
from your_project.utils.embedding_generator import EmbeddingGenerator

@pytest.fixture
def meme_analyzer():
    return MemeAnalyzer(eps=0.3, min_samples=2, engagement_threshold=1000)

@pytest.fixture
def sample_meme_data():
    return {
        'text': 'Sample meme text',
        'engagement': {
            'shares': 500,
            'likes': 1000,
            'comments': 200,
            'saves': 300
        },
        'timestamp': 1672531200,  # Jan 1, 2023
        'platform': 'twitter'
    }

@pytest.fixture
def sample_meme_cluster():
    return [
        {
            'text': 'Original meme',
            'engagement': {'shares': 100, 'likes': 200, 'comments': 50, 'saves': 75}
        },
        {
            'text': 'Variation 1',
            'engagement': {'shares': 150, 'likes': 300, 'comments': 75, 'saves': 100}
        },
        {
            'text': 'Variation 2',
            'engagement': {'shares': 200, 'likes': 400, 'comments': 100, 'saves': 125}
        }
    ]

class TestMemeAnalyzer:
    def test_initialization(self, meme_analyzer):
        assert isinstance(meme_analyzer, MemeAnalyzer)
        assert meme_analyzer.engagement_threshold == 1000
        assert meme_analyzer.cluster_model.eps == 0.3
        assert meme_analyzer.cluster_model.min_samples == 2

    def test_virality_metrics_calculation(self, meme_analyzer, sample_meme_data):
        metrics = meme_analyzer._calculate_virality(sample_meme_data)
        
        assert isinstance(metrics, ViralityMetrics)
        assert 0 <= metrics.score <= 1.0
        assert hasattr(metrics, 'engagement_ratio')
        assert hasattr(metrics, 'velocity')
        assert hasattr(metrics, 'peak_performance')

    @patch.object(EmbeddingGenerator, 'generate')
    def test_analyze_meme(self, mock_generate, meme_analyzer, sample_meme_data):
        mock_generate.return_value = np.random.rand(768)  # Typical embedding size
        
        result = meme_analyzer.analyze_meme(sample_meme_data)
        
        assert isinstance(result, dict)
        assert 'virality_metrics' in result
        assert 'semantic_features' in result
        assert 'evolution_potential' in result
        assert 'temporal_patterns' in result
        assert 'risk_score' in result

    def test_empty_cluster_analysis(self, meme_analyzer):
        result = meme_analyzer.analyze_meme_cluster([])
        
        assert isinstance(result, dict)
        assert 'error' in result
        assert result['error'] == 'Empty meme list provided'

    @patch.object(EmbeddingGenerator, 'generate')
    def test_cluster_analysis(self, mock_generate, meme_analyzer, sample_meme_cluster):
        # Mock embeddings for cluster analysis
        mock_generate.side_effect = [
            np.array([0, 0, 0]),
            np.array([0.1, 0.1, 0.1]),
            np.array([0.2, 0.2, 0.2])
        ]
        
        result = meme_analyzer.analyze_meme_cluster(sample_meme_cluster)
        
        assert isinstance(result, dict)
        assert 'cluster_analysis' in result
        assert 'trend_trajectory' in result
        assert 'mutation_patterns' in result
        assert 'cluster_health' in result
        assert 'virality_distribution' in result

    def test_virality_metrics_dataclass(self):
        metrics = ViralityMetrics(
            score=0.75,
            engagement_ratio=0.85,
            velocity=0.5,
            peak_performance=0.9
        )
        
        assert metrics.score == 0.75
        assert metrics.engagement_ratio == 0.85
        assert metrics.velocity == 0.5
        assert metrics.peak_performance == 0.9

    def test_engagement_threshold_limits(self, meme_analyzer, sample_meme_data):
        # Test with engagement exceeding threshold
        sample_meme_data['engagement'] = {
            'shares': 1000,
            'likes': 2000,
            'comments': 500,
            'saves': 800
        }
        
        metrics = meme_analyzer._calculate_virality(sample_meme_data)
        assert metrics.score == 1.0  # Should be capped at 1.0

    @pytest.mark.parametrize("engagement,expected_score", [
        ({'shares': 0, 'likes': 0, 'comments': 0, 'saves': 0}, 0.0),
