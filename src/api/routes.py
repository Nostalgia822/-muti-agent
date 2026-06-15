"""API routes for asset valuation service"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import asyncio

from src.core.workflow import WorkflowOrchestrator


app = FastAPI(
    title="Asset Valuation API",
    description="Multi-Agent Asset Valuation System",
    version="0.1.0"
)

# Global workflow instance
workflow = WorkflowOrchestrator()


class AssetDataModel(BaseModel):
    """Asset data model"""
    name: str
    type: str
    value: float
    location: Optional[str] = None
    condition: Optional[str] = None
    age: Optional[int] = None
    useful_life: Optional[int] = None
    replacement_cost: Optional[float] = None
    annual_income: Optional[float] = None


class ValuationRequestModel(BaseModel):
    """Valuation request model"""
    asset_id: str
    asset_data: AssetDataModel
    config: Optional[Dict[str, Any]] = None


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/valuate")
async def valuate_asset(request: ValuationRequestModel):
    """Execute asset valuation workflow"""
    try:
        result = await workflow.execute_valuation_workflow(
            asset_id=request.asset_id,
            asset_data=request.asset_data.dict(),
            config=request.config
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/assets/{asset_id}")
async def get_asset_profile(asset_id: str):
    """Get asset profile"""
    profile = workflow.get_asset_profile(asset_id)
    if profile["asset"] is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return profile


@app.get("/history")
async def get_workflow_history():
    """Get workflow execution history"""
    return {"history": workflow.get_workflow_history()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
