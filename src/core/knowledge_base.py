"""Knowledge base for storing and retrieving asset information"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json


class KnowledgeBase:
    """In-memory knowledge base for asset information"""
    
    def __init__(self):
        self.assets: Dict[str, Dict[str, Any]] = {}
        self.analysis_results: Dict[str, Dict[str, Any]] = {}
        self.valuation_results: Dict[str, Dict[str, Any]] = {}
        self.reports: Dict[str, str] = {}
    
    def add_asset(self, asset_id: str, asset_data: Dict[str, Any]) -> None:
        """Add asset information to knowledge base"""
        asset_data["created_at"] = datetime.now().isoformat()
        self.assets[asset_id] = asset_data
    
    def get_asset(self, asset_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve asset information"""
        return self.assets.get(asset_id)
    
    def add_analysis(self, asset_id: str, analysis: Dict[str, Any]) -> None:
        """Store analysis results"""
        if asset_id not in self.analysis_results:
            self.analysis_results[asset_id] = {}
        self.analysis_results[asset_id]["timestamp"] = datetime.now().isoformat()
        self.analysis_results[asset_id].update(analysis)
    
    def get_analysis(self, asset_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve analysis results"""
        return self.analysis_results.get(asset_id)
    
    def add_valuation(self, asset_id: str, valuation: Dict[str, Any]) -> None:
        """Store valuation results"""
        if asset_id not in self.valuation_results:
            self.valuation_results[asset_id] = {}
        self.valuation_results[asset_id]["timestamp"] = datetime.now().isoformat()
        self.valuation_results[asset_id].update(valuation)
    
    def get_valuation(self, asset_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve valuation results"""
        return self.valuation_results.get(asset_id)
    
    def add_report(self, asset_id: str, report: str) -> None:
        """Store generated report"""
        self.reports[asset_id] = report
    
    def get_report(self, asset_id: str) -> Optional[str]:
        """Retrieve generated report"""
        return self.reports.get(asset_id)
    
    def get_all_asset_data(self, asset_id: str) -> Dict[str, Any]:
        """Get complete asset profile"""
        return {
            "asset": self.get_asset(asset_id),
            "analysis": self.get_analysis(asset_id),
            "valuation": self.get_valuation(asset_id),
            "report": self.get_report(asset_id),
        }
    
    def clear(self) -> None:
        """Clear all data"""
        self.assets.clear()
        self.analysis_results.clear()
        self.valuation_results.clear()
        self.reports.clear()
