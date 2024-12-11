import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig
from typing import Dict, Any
import logging

class CustomTransformerModel(nn.Module):
    def __init__(
        self, 
        base_model: str = "bert-base-uncased",
        num_labels: int = 3
    ):
        super().__init__()
        self.config = AutoConfig.from_pretrained(base_model)
        self.transformer = AutoModel.from_pretrained(base_model)
        self.classifier = nn.Linear(self.config.hidden_size, num_labels)
        
        logging.info(f"Initializing CustomTransformerModel with {base_model}")
    
    def forward(
        self, 
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor
    ) -> Dict[str, torch.Tensor]:
        outputs = self.transformer(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        
        pooled_output = outputs.last_hidden_state[:, 0, :]
        logits = self.classifier(pooled_output)
        
        return {
            "logits": logits,
            "hidden_states": outputs.last_hidden_state,
            "embeddings": pooled_output
        }
    
    def save_pretrained(self, path: str):
        self.transformer.save_pretrained(path)
        torch.save(self.classifier.state_dict(), f"{path}/classifier.pt") 