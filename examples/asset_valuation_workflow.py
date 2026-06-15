"""Example: Asset Valuation Workflow

Demonstrates how to use the multi-agent framework for asset valuation.
"""

import asyncio
import json
from src.core.workflow import WorkflowOrchestrator


async def example_real_estate_valuation():
    """Example: Real Estate Property Valuation"""
    
    print("\n" + "="*60)
    print("EXAMPLE 1: Real Estate Property Valuation")
    print("="*60)
    
    workflow = WorkflowOrchestrator()
    
    property_data = {
        "name": "Prime Residential Apartment",
        "type": "Real Estate - Residential",
        "value": 2500000,
        "location": "City Center, District A",
        "condition": "Excellent",
        "age": 5,
        "useful_life": 70,
        "replacement_cost": 2700000,
        "annual_income": 120000,  # Rental income
    }
    
    result = await workflow.execute_valuation_workflow(
        asset_id="RE-APT-001",
        asset_data=property_data
    )
    
    print(f"\nAsset: {property_data['name']}")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Estimated Value: ¥{result['valuation']['estimated_value']:,.2f}")


async def example_equipment_valuation():
    """Example: Industrial Equipment Valuation"""
    
    print("\n" + "="*60)
    print("EXAMPLE 2: Industrial Equipment Valuation")
    print("="*60)
    
    workflow = WorkflowOrchestrator()
    
    equipment_data = {
        "name": "CNC Machining Center",
        "type": "Equipment - Machinery",
        "value": 800000,
        "location": "Manufacturing Facility, Building B",
        "condition": "Good",
        "age": 4,
        "useful_life": 20,
        "replacement_cost": 900000,
        "annual_income": 150000,  # Revenue generated
    }
    
    result = await workflow.execute_valuation_workflow(
        asset_id="EQ-CNC-001",
        asset_data=equipment_data
    )
    
    print(f"\nAsset: {equipment_data['name']}")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Estimated Value: ¥{result['valuation']['estimated_value']:,.2f}")


async def example_vehicle_valuation():
    """Example: Vehicle Fleet Valuation"""
    
    print("\n" + "="*60)
    print("EXAMPLE 3: Vehicle Fleet Valuation")
    print("="*60)
    
    workflow = WorkflowOrchestrator()
    
    vehicle_data = {
        "name": "Commercial Truck Fleet (5 units)",
        "type": "Equipment - Vehicle",
        "value": 500000,
        "location": "Logistics Center",
        "condition": "Fair",
        "age": 6,
        "useful_life": 15,
        "replacement_cost": 550000,
        "annual_income": 80000,  # Leasing or service revenue
    }
    
    result = await workflow.execute_valuation_workflow(
        asset_id="VH-FLEET-001",
        asset_data=vehicle_data
    )
    
    print(f"\nAsset: {vehicle_data['name']}")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Estimated Value: ¥{result['valuation']['estimated_value']:,.2f}")


async def example_batch_valuation():
    """Example: Batch Asset Valuation"""
    
    print("\n" + "="*60)
    print("EXAMPLE 4: Batch Asset Valuation")
    print("="*60)
    
    workflow = WorkflowOrchestrator()
    
    assets = [
        {
            "id": "BATCH-001",
            "data": {
                "name": "Office Furniture Suite",
                "type": "Furniture",
                "value": 150000,
                "location": "Head Office",
                "condition": "Good",
                "age": 3,
                "useful_life": 10,
                "replacement_cost": 160000,
                "annual_income": 0,
            }
        },
        {
            "id": "BATCH-002",
            "data": {
                "name": "Server Room Equipment",
                "type": "IT Equipment",
                "value": 300000,
                "location": "Data Center",
                "condition": "Excellent",
                "age": 2,
                "useful_life": 8,
                "replacement_cost": 320000,
                "annual_income": 50000,
            }
        },
    ]
    
    results = []
    for asset in assets:
        result = await workflow.execute_valuation_workflow(
            asset_id=asset["id"],
            asset_data=asset["data"]
        )
        results.append(result)
    
    print(f"\nProcessed {len(results)} assets:")
    for result in results:
        if result['status'] == 'success':
            print(f"  - {result['asset_id']}: ¥{result['valuation']['estimated_value']:,.2f}")


async def main():
    """Run all examples"""
    await example_real_estate_valuation()
    await example_equipment_valuation()
    await example_vehicle_valuation()
    await example_batch_valuation()
    
    print("\n" + "="*60)
    print("All examples completed successfully!")
    print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
