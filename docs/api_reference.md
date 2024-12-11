# API Reference

## Core Components

### SentientAgent

```python
from memesphere.core import SentientAgent

agent = SentientAgent(
    name="MyAgent",
    specialization="Meme Analysis",
    cognitive_depth=0.7
)
```

#### Methods
- `decode_meme_network(source: str, timeframe: str) -> MemeticAnalysis`
- `process_cultural_signals(data: List[Dict]) -> Dict`

### MemeAnalyzer

```python
from memesphere.agents import MemeAnalyzer

analyzer = MemeAnalyzer()
result = analyzer.analyze_meme(meme_data)
```

#### Methods
- `analyze_meme(meme_data: Dict) -> Dict`
- `analyze_meme_cluster(memes: List[Dict]) -> Dict`

## Blockchain Integration

### SolanaWallet

```python
from memesphere.integrations import SolanaWallet

wallet = SolanaWallet.create(network="devnet")
```

#### Methods
- `mint_meme(meme_data: Dict) -> str`
- `get_balance() -> float`
- `close() -> None`

## Utility Functions

### EmbeddingGenerator

```python
from memesphere.utils import EmbeddingGenerator

generator = EmbeddingGenerator()
embeddings = generator.generate(text)
```

#### Methods
- `generate(text: Union[str, List[str]], depth_level: str) -> np.ndarray` 