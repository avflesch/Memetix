import pytest
from memesphere.core import LanguageProcessor
from memesphere.utils import DataPreprocessor

@pytest.fixture
def language_processor():
    return LanguageProcessor()

@pytest.fixture
def data_preprocessor():
    return DataPreprocessor()

def test_text_processing(language_processor):
    test_text = "This is a test sentence for NLP processing."
    result = language_processor.process_text(test_text)
    
    assert "tokens" in result
    assert "entities" in result
    assert "summary" in result
    assert "syntax_tree" in result

def test_entity_extraction(language_processor):
    test_text = "Google and Microsoft are tech companies."
    entities = language_processor._extract_entities(test_text)
    
    assert len(entities) > 0
    assert any(entity["entity"] == "ORG" for entity in entities)

def test_text_preprocessing(data_preprocessor):
    test_text = "THIS is A TEST sentence!!!"
    processed = data_preprocessor.preprocess_text(test_text)
    
    assert processed.islower()
    assert "!!!" not in processed

def test_summary_generation(language_processor):
    long_text = " ".join(["This is a test sentence."] * 20)
    summary = language_processor._generate_summary(long_text)
    
    assert len(summary) < len(long_text)
    assert isinstance(summary, str) 