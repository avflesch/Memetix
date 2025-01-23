from dataclasses import dataclass
from typing import Dict, Any, Optional
import asyncio
import logging

from memetix.agents import MemeAnalyzer 
from memetix.core import SentientAgent
from memetix.integrations import SolanaWallet

@dataclass
class MemeData:
   url: str
   text: str 
   platform: str
   timestamp: str

class MemeAnalyzer:
   def __init__(self):
       self.analyzer = MemeAnalyzer()
       self.agent = SentientAgent("MemeExplorer", specialization="Viral Content")
       self.wallet = SolanaWallet.create()
       self.logger = logging.getLogger(__name__)

   async def mint_viral_meme(self, meme: MemeData, analysis: Dict) -> Optional[str]:
       if analysis["virality_score"] <= 0.8:
           return None
           
       nft_data = {
           "title": "Viral Programming Meme",
           "description": meme.text,
           "image_url": meme.url,
           "attributes": analysis
       }
       
       address = await self.wallet.mint_meme(nft_data)
       self.logger.info(f"Minted viral meme as NFT: {address}")
       return address

   async def analyze(self, meme: MemeData) -> Dict[str, Any]:
       analysis = self.analyzer.analyze_meme(meme.__dict__)
       
       cultural_insight = self.agent.decode_meme_network(
           source=meme.platform,
           timeframe="24h"
       )

       nft_address = await self.mint_viral_meme(meme, analysis)
       
       return {
           "analysis": analysis,
           "cultural_context": cultural_insight,
           "nft_address": nft_address
       }

async def main():
   sample_meme = MemeData(
       url="https://example.com/meme.png",
       text="When the code works on first try",
       platform="reddit", 
       timestamp="2024-01-15T12:00:00Z"
   )
   
   analyzer = MemeAnalyzer()
   result = await analyzer.analyze(sample_meme)
   print(result)

if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)
   asyncio.run(main())
