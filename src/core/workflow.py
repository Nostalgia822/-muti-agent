"""Workflow orchestration for asset valuation"""

from typing import Dict, Any, Optional
import logging
from datetime import datetime

from src.core.knowledge_base import KnowledgeBase
from src.agents.data_collector import DataCollectorAgent
from src.agents.asset_analyzer import AssetAnalyzerAgent
from src.agents.valuator import ValuatorAgent
from src.agents.report_generator import ReportGeneratorAgent

logger = logging.getLogger(__name__)


class WorkflowOrchestrator:
    """Orchestrates the asset valuation workflow"""
    
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.data_collector = DataCollectorAgent(self.knowledge_base)
        self.asset_analyzer = AssetAnalyzerAgent(self.knowledge_base)
        self.valuator = ValuatorAgent(self.knowledge_base)
        self.report_generator = ReportGeneratorAgent(self.knowledge_base)
        self.workflow_history = []
    
    async def execute_valuation_workflow(
        self, 
        asset_id: str, 
        asset_data: Dict[str, Any],
        config: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute complete asset valuation workflow"""
        
        logger.info(f"Starting valuation workflow for asset: {asset_id}")
        start_time = datetime.now()
        
        try:
            # Step 1: Data Collection
            logger.info("Step 1: Data Collection")
            collected_data = await self.data_collector.collect(
                asset_id, 
                asset_data
            )
            
            # Step 2: Asset Analysis
            logger.info("Step 2: Asset Analysis")
            analysis = await self.asset_analyzer.analyze(
                asset_id,
                collected_data
            )
            
            # Step 3: Valuation Calculation
            logger.info("Step 3: Valuation Calculation")
            valuation = await self.valuator.valuate(
                asset_id,
                collected_data,
                analysis,
                config or {}
            )
            
            # Step 4: Report Generation
            logger.info("Step 4: Report Generation")
            report = await self.report_generator.generate(
                asset_id,
                collected_data,
                analysis,
                valuation
            )
            
            # Compile results
            result = {
                "asset_id": asset_id,
                "status": "success",
                "collected_data": collected_data,
                "analysis": analysis,
                "valuation": valuation,
                "report": report,
                "duration_seconds": (datetime.now() - start_time).total_seconds(),
            }
            
            # Record workflow
            self.workflow_history.append({
                "asset_id": asset_id,
                "timestamp": start_time.isoformat(),
                "status": "completed",
            })
            
            logger.info(f"Workflow completed successfully for asset: {asset_id}")
            return result
            
        except Exception as e:
            logger.error(f"Workflow failed for asset {asset_id}: {str(e)}")
            result = {
                "asset_id": asset_id,
                "status": "failed",
                "error": str(e),
                "duration_seconds": (datetime.now() - start_time).total_seconds(),
            }
            self.workflow_history.append({
                "asset_id": asset_id,
                "timestamp": start_time.isoformat(),
                "status": "failed",
            })
            return result
    
    def get_asset_profile(self, asset_id: str) -> Dict[str, Any]:
        """Get complete asset profile from knowledge base"""
        return self.knowledge_base.get_all_asset_data(asset_id)
    
    def get_workflow_history(self) -> list:
        """Get workflow execution history"""
        return self.workflow_history
