"""Main entry point for asset valuation workflow"""

import asyncio
import logging
from src.core.workflow import WorkflowOrchestrator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


async def main():
    """Run a sample asset valuation workflow"""
    
    # Initialize workflow
    workflow = WorkflowOrchestrator()
    
    # Sample asset data
    sample_asset = {
        "name": "Commercial Office Building",
        "type": "Real Estate",
        "value": 5000000,
        "location": "Downtown Business District",
        "condition": "Good",
        "age": 8,
        "useful_life": 50,
        "replacement_cost": 5500000,
        "annual_income": 400000,
    }
    
    # Execute workflow
    result = await workflow.execute_valuation_workflow(
        asset_id="ASSET-001",
        asset_data=sample_asset
    )
    
    # Print results
    print("\n" + "="*60)
    print("WORKFLOW EXECUTION RESULTS")
    print("="*60)
    
    print(f"\nStatus: {result['status']}")
    print(f"Duration: {result['duration_seconds']:.2f} seconds")
    
    if result['status'] == 'success':
        print(f"\nEstimated Value: ¥{result['valuation']['estimated_value']:,.2f}")
        print(f"Value Range: ¥{result['valuation']['value_range']['min']:,.2f} - ¥{result['valuation']['value_range']['max']:,.2f}")
        print(f"\n--- Generated Report ---\n{result['report']}")
    else:
        print(f"\nError: {result.get('error', 'Unknown error')}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    asyncio.run(main())
