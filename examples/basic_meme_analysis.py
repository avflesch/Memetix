from memesphere.agents import MemeAnalyzer
from memesphere.core import SentientAgent
from memesphere.integrations import SolanaWallet
import asyncio
import logging

async def analyze_single_meme():
    # Initialize components
    analyzer = MemeAnalyzer()
    agent = SentientAgent("MemeExplorer", specialization="Viral Content")
    wallet = SolanaWallet.create()
    
    # Sample meme data
    meme_data = {
        "url": "https://example.com/meme.png",
        "text": "When the code works on first try",
        "platform": "reddit",
        "timestamp": "2024-01-15T12:00:00Z"
    }
    
    # Analyze meme
    analysis = analyzer.analyze_meme(meme_data)
    
    # Get cultural context
    cultural_insight = agent.decode_meme_network(
        source="reddit",
        timeframe="24h"
    )
    
    # Mint as NFT if highly viral
    if analysis["virality_score"] > 0.8:
        nft_address = await wallet.mint_meme({
            "title": "Viral Programming Meme",
            "description": meme_data["text"],
            "image_url": meme_data["url"],
            "attributes": analysis
        })
        print(f"Minted as NFT: {nft_address}")
    
    return {
        "analysis": analysis,
        "cultural_context": cultural_insight
    }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = asyncio.run(analyze_single_meme())
    print(result) 
