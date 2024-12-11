# Blockchain Integration Guide

## Overview
MemeSphere uses Solana blockchain for:
- Meme NFT minting
- Ownership tracking
- Reward distribution
- Governance participation

## Setup

### 1. Wallet Configuration
```python
from memesphere.integrations import SolanaWallet

# Create new wallet
wallet = SolanaWallet.create(network="devnet")

# Or load existing wallet
wallet = SolanaWallet.from_keypair("path/to/keypair.json")
```

### 2. Network Selection
```python
# Environment variables
SOLANA_NETWORK=devnet  # or mainnet-beta
SOLANA_RPC_URL=https://api.devnet.solana.com
```

## Minting Memes

### 1. Basic Minting
```python
meme_data = {
    "title": "My Awesome Meme",
    "description": "Description here",
    "image_url": "https://example.com/meme.jpg"
}

nft_address = await wallet.mint_meme(meme_data)
```

### 2. Advanced Features
- Royalty settings
- Metadata updates
- Transfer restrictions
- Collection grouping

## Governance

### 1. Participation
```python
# Vote on proposals
await wallet.vote(proposal_id, vote_choice)

# Create proposal
await wallet.create_proposal(proposal_data)
```

### 2. Rewards
- Viral meme rewards
- Governance participation rewards
- Curation rewards

## Security Considerations
- Private key management
- Transaction signing
- Rate limiting
- Error handling 