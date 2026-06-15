"""Report Generation Agent - Creates professional valuation reports"""

from typing import Dict, Any
import logging
from datetime import datetime

from src.agents.base_agent import BaseAgent
from src.core.knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


class ReportGeneratorAgent(BaseAgent):
    """Generates professional asset valuation reports"""
    
    def __init__(self, knowledge_base: KnowledgeBase):
        super().__init__(knowledge_base, "ReportGenerator")
    
    async def generate(
        self,
        asset_id: str,
        asset_data: Dict[str, Any],
        analysis: Dict[str, Any],
        valuation: Dict[str, Any]
    ) -> str:
        """Generate valuation report"""
        self.log_action("Generating report", {"asset_id": asset_id})
        
        # Build report sections
        report = self._build_report(
            asset_id,
            asset_data,
            analysis,
            valuation
        )
        
        # Store report
        self.knowledge_base.add_report(asset_id, report)
        
        self.log_action("Report generated", {"asset_id": asset_id})
        
        return report
    
    async def execute(
        self,
        asset_id: str,
        asset_data: Dict[str, Any],
        analysis: Dict[str, Any],
        valuation: Dict[str, Any]
    ) -> str:
        """Execute agent task"""
        return await self.generate(asset_id, asset_data, analysis, valuation)
    
    def _build_report(self, asset_id: str, asset_data: Dict[str, Any], analysis: Dict[str, Any], valuation: Dict[str, Any]) -> str:
        """Build comprehensive report"""
        report = f"""# 资产评估报告

## 报告基本信息
- 资产ID: {asset_id}
- 资产名称: {asset_data.get('name', 'N/A')}
- 资产类型: {asset_data.get('type', 'N/A')}
- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 一、资产基本情况

### 资产概况
- 名称: {asset_data.get('name', 'N/A')}
- 类型: {asset_data.get('type', 'N/A')}
- 地点: {asset_data.get('location', 'N/A')}
- 状况: {asset_data.get('condition', 'N/A')}
- 年龄: {asset_data.get('age', 'N/A')} 年

## 二、资产分析

### 资产特征
"""
        
        if "characteristics" in analysis:
            chars = analysis["characteristics"]
            report += f"""- 类型: {chars.get('type', 'N/A')}
- 状况: {chars.get('condition', 'N/A')}
- 地点: {chars.get('location', 'N/A')}
"""
        
        report += f"""\n### 市场分析
- 市场趋势: {analysis.get('market_analysis', {}).get('market_trend', 'N/A')}
- 价格指数: {analysis.get('market_analysis', {}).get('price_index', 'N/A')}

### 风险评估
"""
        
        if "risk_assessment" in analysis:
            risks = analysis["risk_assessment"]
            report += f"""- 市场风险: {risks.get('market_risk', 'N/A')}
- 运营风险: {risks.get('operational_risk', 'N/A')}
- 法律风险: {risks.get('legal_risk', 'N/A')}
- 流动性风险: {risks.get('liquidity_risk', 'N/A')}
"""
        
        report += f"""\n### 优势
"""
        if "strengths" in analysis:
            for strength in analysis["strengths"]:
                report += f"- {strength}\n"
        
        report += f"""\n### 劣势
"""
        if "weaknesses" in analysis:
            for weakness in analysis["weaknesses"]:
                report += f"- {weakness}\n"
        
        report += f"""\n## 三、估值结论

### 估值方法
"""
        
        if "market_method" in valuation:
            market = valuation["market_method"]
            report += f"""\n#### 市场法
- 估值值: ¥{market.get('value', 0):,.2f}
- 调整因子: {market.get('adjustment_factor', 'N/A')}
"""
        
        if "income_method" in valuation:
            income = valuation["income_method"]
            report += f"""\n#### 收益法
- 估值值: ¥{income.get('value', 0):,.2f}
- 年收益: ¥{income.get('annual_income', 0):,.2f}
- 资本化率: {income.get('cap_rate', 'N/A')}
"""
        
        if "cost_method" in valuation:
            cost = valuation["cost_method"]
            report += f"""\n#### 成本法
- 估值值: ¥{cost.get('value', 0):,.2f}
- 重置成本: ¥{cost.get('replacement_cost', 0):,.2f}
- 折旧率: {cost.get('depreciation_rate', 'N/A')}
"""
        
        report += f"""\n### 最终估值
- 估值范围: ¥{valuation['value_range']['min']:,.2f} ~ ¥{valuation['value_range']['max']:,.2f}
- 平均估值: ¥{valuation['estimated_value']:,.2f}
- 评估值: ¥{valuation['estimated_value']:,.2f}

## 报告说明

本报告基于客户提供的信息和现场勘查结果，采用多种估值方法综合分析得出。
估值结论仅供参考，不构成法律建议。

---
报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return report
