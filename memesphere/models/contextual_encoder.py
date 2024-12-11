import torch
import torch.nn as nn
from typing import Dict, Tuple
import logging
from transformers import AutoTokenizer

class ContextualEncoder(nn.Module):
    def __init__(
        self, 
        embedding_dim: int = 768,
        hidden_dim: int = 512,
        num_layers: int = 2
    ):
        super().__init__()
        
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        
        self.encoder = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            bidirectional=True
        )
        
        self.attention = nn.MultiheadAttention(
            embed_dim=hidden_dim * 2,
            num_heads=8
        )
        
        logging.info("Initializing ContextualEncoder")
    
    def forward(
        self, 
        x: torch.Tensor,
        mask: torch.Tensor = None
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        # Encode sequence
        encoded, (hidden, cell) = self.encoder(x)
        
        # Apply attention
        if mask is not None:
            attention_output, attention_weights = self.attention(
                encoded, encoded, encoded,
                key_padding_mask=mask
            )
        else:
            attention_output, attention_weights = self.attention(
                encoded, encoded, encoded
            )
        
        return attention_output, {
            "hidden_state": hidden,
            "cell_state": cell,
            "attention_weights": attention_weights
        }
    
    def encode_text(self, text: str, tokenizer: AutoTokenizer) -> torch.Tensor:
        tokens = tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True
        )
        
        with torch.no_grad():
            output, _ = self.forward(tokens["input_ids"])
            
        return output.mean(dim=1)  # Average pooling over sequence length 