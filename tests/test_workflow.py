"""Tests for workflow orchestration"""

import pytest
import asyncio
from src.core.workflow import WorkflowOrchestrator


@pytest.fixture
def workflow():
    """Create workflow instance"""
    return WorkflowOrchestrator()


@pytest.mark.asyncio
async def test_complete_workflow(workflow):
    """Test complete valuation workflow"""
    
    asset_data = {
        "name": "Test Property",
        "type": "Real Estate",
        "value": 1000000,
        "location": "Test Location",
        "condition": "Good",
        "age": 5,
        "useful_life": 50,
        "replacement_cost": 1100000,
        "annual_income": 100000,
    }
    
    result = await workflow.execute_valuation_workflow(
        asset_id="TEST-001",
        asset_data=asset_data
    )
    
    assert result["status"] == "success"
    assert result["asset_id"] == "TEST-001"
    assert "valuation" in result
    assert "estimated_value" in result["valuation"]
    assert "report" in result


@pytest.mark.asyncio
async def test_get_asset_profile(workflow):
    """Test retrieving asset profile"""
    
    asset_data = {
        "name": "Test Asset",
        "type": "Equipment",
        "value": 500000,
        "location": "Test Location",
        "condition": "Good",
        "age": 2,
        "useful_life": 10,
        "replacement_cost": 550000,
        "annual_income": 50000,
    }
    
    await workflow.execute_valuation_workflow(
        asset_id="TEST-002",
        asset_data=asset_data
    )
    
    profile = workflow.get_asset_profile("TEST-002")
    assert profile["asset"] is not None
    assert profile["asset"]["name"] == "Test Asset"


@pytest.mark.asyncio
async def test_workflow_history(workflow):
    """Test workflow history tracking"""
    
    asset_data = {
        "name": "Test Asset",
        "type": "Equipment",
        "value": 500000,
        "location": "Test Location",
        "condition": "Good",
        "age": 2,
        "useful_life": 10,
        "replacement_cost": 550000,
        "annual_income": 50000,
    }
    
    # Execute multiple workflows
    for i in range(3):
        await workflow.execute_valuation_workflow(
            asset_id=f"TEST-{i}",
            asset_data=asset_data
        )
    
    history = workflow.get_workflow_history()
    assert len(history) == 3
