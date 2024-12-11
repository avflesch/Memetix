import pytest
from memesphere.core import SentientAgent
from memesphere.agents import MemeAnalyzer
import asyncio

@pytest.fixture
def agent():
    return SentientAgent(
        name="TestAgent",
        specialization="Testing",
        cognitive_depth=0.5
    )

@pytest.fixture
def meme_analyzer():
    return MemeAnalyzer()

def test_agent_initialization(agent):
    assert agent.name == "TestAgent"
    assert agent.specialization == "Testing"
    assert agent.cognitive_model is not None

@pytest.mark.asyncio
async def test_meme_network_decoding(agent):
    analysis = agent.decode_meme_network(
        source="test_platform",
        timeframe="1h",
        depth="surface"
    )
    
    assert analysis is not None
    assert hasattr(analysis, 'generate_cultural_intelligence_report')

def test_memetic_data_processing(agent):
    test_data = [
        {
            "content": "Test meme content",
            "platform": "test_platform",
            "timestamp": "2024-01-01"
        }
    ]
    
    processed = agent._process_memetic_signals(test_data, "surface")
    assert len(processed) == len(test_data)
    assert "semantic_embedding" in processed[0]

@pytest.mark.asyncio
async def test_meme_analysis(meme_analyzer):
    test_meme = {
        "text": "Test meme",
        "platform": "test_platform",
        "timestamp": "2024-01-01"
    }
    
    analysis = meme_analyzer.analyze_meme(test_meme)
    assert "virality_score" in analysis
    assert "semantic_features" in analysis 