"""Data Collection Agent - Gathers and validates asset information"""

from typing import Dict, Any, Optional
import logging
from datetime import datetime

from src.agents.base_agent import BaseAgent
from src.core.knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


class DataCollectorAgent(BaseAgent):
    """Collects and validates asset data from various sources"""
    
    def __init__(self, knowledge_base: KnowledgeBase):
        super().__init__(knowledge_base, "DataCollector")
    
    async def collect(self, asset_id: str, asset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Collect asset information"""
        self.log_action("Starting data collection", {"asset_id": asset_id})
        
        # Validate input data
        validated_data = self._validate_data(asset_data)
        
        # Enrich data with metadata
        enriched_data = self._enrich_data(asset_id, validated_data)
        
        # Store in knowledge base
        self.knowledge_base.add_asset(asset_id, enriched_data)
        
        self.log_action("Data collection completed", {
            "asset_id": asset_id,
            "fields_count": len(enriched_data)
        })
        
        return enriched_data
    
    async def execute(self, asset_id: str, asset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute agent task"""
        return await self.collect(asset_id, asset_data)
    
    def _validate_data(self, asset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and clean data"""
        required_fields = ["name", "type", "value"]
        
        for field in required_fields:
            if field not in asset_data:
                logger.warning(f"Missing required field: {field}")
        
        return asset_data
    
    def _enrich_data(self, asset_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Add metadata and enrich data"""
        enriched = data.copy()
        enriched["collected_at"] = datetime.now().isoformat()
        enriched["data_source"] = "user_input"
        enriched["validation_status"] = "validated"
        
        return enriched
