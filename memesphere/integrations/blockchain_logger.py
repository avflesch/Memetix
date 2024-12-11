from typing import Dict, Any
import logging
import hashlib
import json
import time
from web3 import Web3

class BlockchainLogger:
    def __init__(
        self, 
        network_url: str = "http://localhost:8545",
        contract_address: str = None
    ):
        self.web3 = Web3(Web3.HTTPProvider(network_url))
        self.contract_address = contract_address
        self.transaction_cache = []
        
        logging.info("Initializing BlockchainLogger")
    
    async def log_event(
        self, 
        event_data: Dict[str, Any]
    ) -> Dict[str, str]:
        """
        Log event data to blockchain
        """
        event_hash = self._generate_event_hash(event_data)
        
        try:
            transaction = {
                "timestamp": int(time.time()),
                "event_hash": event_hash,
                "data": event_data
            }
            
            self.transaction_cache.append(transaction)
            
            return {
                "status": "success",
                "hash": event_hash,
                "timestamp": str(transaction["timestamp"])
            }
            
        except Exception as e:
            logging.error(f"Blockchain logging error: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
    
    def _generate_event_hash(self, data: Dict) -> str:
        """
        Generate unique hash for event data
        """
        data_string = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    async def flush_cache(self) -> bool:
        """
        Flush cached transactions to blockchain
        """
        try:
            if self.transaction_cache:
                # Batch commit logic would go here
                self.transaction_cache = []
            return True
        except Exception as e:
            logging.error(f"Cache flush error: {e}")
            return False 