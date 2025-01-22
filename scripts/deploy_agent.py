from dataclasses import dataclass
from typing import Dict, Any, Optional
import asyncio
import logging
import argparse
import yaml
from pathlib import Path

from memetix.core import SentientAgent
from memetix.integrations import SolanaWallet
from memetix.types import DeploymentResult

@dataclass
class AgentConfig:
    specialization: str = "General"
    cognitive_depth: float = 0.7
    
    @classmethod
    def from_yaml(cls, path: str) -> 'AgentConfig':
        with open(path) as f:
            config = yaml.safe_load(f)
        return cls(
            specialization=config.get("specialization", cls.specialization),
            cognitive_depth=config.get("cognitive_depth", cls.cognitive_depth)
        )

class AgentDeployer:
    def __init__(self, config: AgentConfig, network: str = "grpc"):
        self.config = config
        self.network = network
        self.logger = logging.getLogger(__name__)

    async def initialize_wallet(self) -> SolanaWallet:
        wallet = SolanaWallet.create(network=self.network)
        balance = await wallet.get_balance()
        self.logger.info(f"Wallet balance: {balance} SOL")
        return wallet

    async def create_agent(self, name: str) -> SentientAgent:
        return SentientAgent(
            name=name,
            specialization=self.config.specialization,
            cognitive_depth=self.config.cognitive_depth
        )

    async def deploy(self, agent_name: str) -> DeploymentResult:
        """
        Deploy a sentient agent to the Solana network
        
        Args:
            agent_name: Name identifier for the agent
            
        Returns:
            Dictionary containing deployment status and details
        
        Raises:
            DeploymentError: If deployment fails
        """
        self.logger.info(f"Deploying agent: {agent_name}")
        self.logger.info(f"Network: {self.network}")

        wallet = await self.initialize_wallet()
        agent = await self.create_agent(agent_name)

        try:
            # Deployment logic would go here
            self.logger.info("Agent deployed successfully")
            return {
                "status": "success",
                "agent_id": agent.name,
                "wallet_address": str(wallet.keypair.public_key)
            }
            
        except Exception as e:
            self.logger.error(f"Deployment failed: {e}")
            raise DeploymentError(f"Failed to deploy agent: {e}")
            
        finally:
            await wallet.close()

class DeploymentError(Exception):
    """Raised when agent deployment fails"""
    pass

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deploy a sentient agent to Solana")
    parser.add_argument("--config", required=True, help="Path to agent configuration file")
    parser.add_argument("--agent_name", required=True, help="Name identifier for the agent")
    parser.add_argument("--network", default="grpc", help="Network to deploy to (default: grpc)")
    return parser.parse_args()

async def main() -> None:
    args = parse_args()
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    config = AgentConfig.from_yaml(args.config)
    deployer = AgentDeployer(config, args.network)
    
    try:
        result = await deployer.deploy(args.agent_name)
        print(result)
    except DeploymentError as e:
        logging.error(e)
        exit(1)

if __name__ == "__main__":
    asyncio.run(main())
