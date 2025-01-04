# Installation Guide

## Prerequisites

Before installing MemeSphere, ensure you have:
- Python 3.8 or higher
- Solana Tool Suite
- CUDA-compatible GPU (recommended)
- Node.js and npm (for blockchain interactions)

## Installation Methods

### 1. From PyPI
```bash
pip install memesphere
```

### 2. From Source
```bash
git clone https://github.com/memesphere/memesphere.git
cd memesphere
pip install -e .
```

### 3. Docker
```bash
docker pull memesphere/memesphere:latest
docker run -d --name memesphere memesphere/memesphere
```

## Environment Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Set environment variables:
```bash
export SOLANA_NETWORK=grpc
export SOLANA_RPC_URL=https://api.grpc.solana.com
```

## Verification
Verify installation:
```python
from memesphere import MemeAnalyzer
analyzer = MemeAnalyzer()
print("Installation successful!")
``` 
