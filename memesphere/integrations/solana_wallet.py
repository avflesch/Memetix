from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer
from solana.rpc.commitment import Confirmed
import base58
import json
import logging
from typing import Optional, Dict, Any
from pathlib import Path

class SolanaWallet:
    def __init__(
        self, 
        keypair: Optional[Keypair] = None,
        network: str = "devnet"
    ):
        self.keypair = keypair or Keypair()
        self.network = network
        self.client = AsyncClient(
            f"https://api.{network}.solana.com" 
            if network != "mainnet-beta" 
            else "https://api.mainnet-beta.solana.com"
        )
        
        logging.info(f"Initializing Solana Wallet on {network}")
    
    @classmethod
    def create(cls, network: str = "devnet") -> 'SolanaWallet':
        """
        Create new wallet with fresh keypair
        """
        return cls(Keypair(), network)
    
    @classmethod
    def from_keypair(
        cls, 
        keypair_path: str,
        network: str = "devnet"
    ) -> 'SolanaWallet':
        """
        Load wallet from keypair file
        """
        with open(keypair_path, 'r') as f:
            keypair_data = json.load(f)
        keypair = Keypair.from_secret_key(bytes(keypair_data))
        return cls(keypair, network)
    
    async def get_balance(self) -> float:
        """
        Get wallet balance in SOL
        """
        response = await self.client.get_balance(
            self.keypair.public_key,
            commitment=Confirmed
        )
        return response['result']['value'] / 1e9  # Convert lamports to SOL
    
    async def mint_meme(
        self, 
        meme_data: Dict[str, Any]
    ) -> str:
        """
        Mint meme as NFT on Solana
        """
        try:
            # NFT minting logic would go here
            # This is a placeholder for the actual implementation
            metadata = {
                "name": meme_data.get("title", "Untitled Meme"),
                "description": meme_data.get("description", ""),
                "image": meme_data.get("image_url", ""),
                "attributes": meme_data.get("attributes", {})
            }
            
            # Return mock NFT address for now
            return "NFT mint address would go here"
            
        except Exception as e:
            logging.error(f"Failed to mint meme NFT: {e}")
            raise
    
    async def close(self):
        """
        Close client connection
        """
        await self.client.close() 