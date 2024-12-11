import asyncio
import httpx
from typing import List, Dict, Any
import logging
from urllib.parse import urlparse
import pandas as pd

class NetworkCrawler:
    def __init__(self, max_concurrent: int = 10):
        self.max_concurrent = max_concurrent
        self.client = httpx.AsyncClient(
            timeout=30.0,
            limits=httpx.Limits(max_connections=max_concurrent)
        )
        
        logging.info(f"Initializing NetworkCrawler with {max_concurrent} concurrent connections")
    
    async def crawl_network(
        self, 
        seed_urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Crawl network starting from seed URLs
        """
        tasks = [
            self._process_url(url) 
            for url in seed_urls[:self.max_concurrent]
        ]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r is not None]
    
    async def _process_url(self, url: str) -> Dict[str, Any]:
        try:
            response = await self.client.get(url)
            return {
                "url": url,
                "status": response.status_code,
                "content_type": response.headers.get("content-type"),
                "data": response.text
            }
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")
            return None 