"""Valuation Agent - Calculates asset value using multiple methods"""

from typing import Dict, Any, Optional
import logging

from src.agents.base_agent import BaseAgent
from src.core.knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


class ValuatorAgent(BaseAgent):
    """Performs asset valuation using multiple methods"""
    
    def __init__(self, knowledge_base: KnowledgeBase):
        super().__init__(knowledge_base, "Valuator")
    
    async def valuate(
        self,
        asset_id: str,
        asset_data: Dict[str, Any],
        analysis: Dict[str, Any],
        config: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Calculate asset valuation"""
        self.log_action("Starting asset valuation", {"asset_id": asset_id})
        
        # Extract base value
        base_value = asset_data.get("value", 0)
        
        # Apply different valuation methods
        valuation = {
            "asset_id": asset_id,
            "market_method": self._market_method(base_value, analysis),
            "income_method": self._income_method(base_value, asset_data),
            "cost_method": self._cost_method(base_value, asset_data),
        }
        
        # Calculate average valuation
        values = [
            valuation["market_method"]["value"],
            valuation["income_method"]["value"],
            valuation["cost_method"]["value"],
        ]
        
        # Weighted average (you can adjust weights based on context)
        valuation["estimated_value"] = sum(values) / len(values)
        valuation["value_range"] = {
            "min": min(values),
            "max": max(values),
            "avg": valuation["estimated_value"],
        }
        
        # Store valuation results
        self.knowledge_base.add_valuation(asset_id, valuation)
        
        self.log_action("Asset valuation completed", {
            "asset_id": asset_id,
            "estimated_value": valuation["estimated_value"]
        })
        
        return valuation
    
    async def execute(
        self,
        asset_id: str,
        asset_data: Dict[str, Any],
        analysis: Dict[str, Any],
        config: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute agent task"""
        return await self.valuate(asset_id, asset_data, analysis, config)
    
    def _market_method(self, base_value: float, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Market comparison method"""
        # Apply market adjustments
        adjustment = 1.0
        if analysis.get("market_analysis", {}).get("market_trend") == "stable":
            adjustment = 1.0
        
        return {
            "method": "Market Comparison",
            "value": base_value * adjustment,
            "adjustment_factor": adjustment,
        }
    
    def _income_method(self, base_value: float, asset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Income capitalization method"""
        annual_income = asset_data.get("annual_income", 0)
        cap_rate = 0.08  # 8% capitalization rate
        
        if cap_rate > 0:
            income_value = annual_income / cap_rate
        else:
            income_value = base_value
        
        return {
            "method": "Income Capitalization",
            "value": income_value,
            "annual_income": annual_income,
            "cap_rate": cap_rate,
        }
    
    def _cost_method(self, base_value: float, asset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cost approach method"""
        replacement_cost = asset_data.get("replacement_cost", base_value)
        age = asset_data.get("age", 0)
        useful_life = asset_data.get("useful_life", 50)
        
        # Straight-line depreciation
        depreciation_rate = min(age / useful_life, 1.0)
        depreciated_value = replacement_cost * (1 - depreciation_rate)
        
        return {
            "method": "Cost Approach",
            "value": depreciated_value,
            "replacement_cost": replacement_cost,
            "depreciation_rate": depreciation_rate,
        }
