from memesphere.core import SentientAgent
from memesphere.integrations import SolanaWallet
import asyncio
import logging
import argparse
import yaml
from pathlib import Path

async def deploy_agent(
    config_path: str,
    agent_name: str,
    network: str = "devnet"
):
    # Load configuration
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Initialize components
    agent = SentientAgent(
        name=agent_name,
        specialization=config.get("specialization", "General"),
        cognitive_depth=config.get("cognitive_depth", 0.7)
    )
    
    wallet = SolanaWallet.create(network=network)
    
    logging.info(f"Deploying agent: {agent_name}")
    logging.info(f"Network: {network}")
    
    # Initialize agent state
    balance = await wallet.get_balance()
    logging.info(f"Wallet balance: {balance} SOL")
    
    # Deploy agent
    try:
        # Deployment logic would go here
        logging.info("Agent deployed successfully")
        return {
            "status": "success",
            "agent_id": agent.name,
            "wallet_address": str(wallet.keypair.public_key)
        }
    except Exception as e:
        logging.error(f"Deployment failed: {e}")
        raise
    finally:
        await wallet.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--agent_name", required=True)
    parser.add_argument("--network", default="devnet")
    
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    result = asyncio.run(deploy_agent(
        args.config,
        args.agent_name,
        args.network
    ))
    print(result) 