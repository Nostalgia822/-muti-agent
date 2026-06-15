# 架构设计文档

## 系统概述

资产评估全流程Multi-Agent框架采用模块化设计，通过多个专业化Agent协同工作，完成资产从数据采集到评估报告生成的全流程。

## 核心架构

### 1. 工作流编排层 (Orchestrator)

`WorkflowOrchestrator` 是系统的中枢，负责：
- 协调各个Agent的执行顺序
- 管理Agent间的数据流转
- 处理错误和异常
- 记录工作流执行历史

### 2. 知识库 (Knowledge Base)

`KnowledgeBase` 是系统的数据中心，存储：
- 原始资产数据
- 分析结果
- 估值结果
- 生成的报告

结构：
```python
KnowledgeBase
├── assets            # 资产基础信息
├── analysis_results  # 分析结果
├── valuation_results # 估值结果
└── reports          # 生成的报告
```

### 3. 专业Agent系统

#### 3.1 数据采集Agent (DataCollectorAgent)

**职责**：
- 从多个数据源采集资产信息
- 数据验证和清洗
- 数据质量检查

**输入**：原始资产数据
**输出**：验证后的资产数据

#### 3.2 资产分析Agent (AssetAnalyzerAgent)

**职责**：
- 分析资产的核心特征
- 进行市场对标分析
- 评估资产风险
- 识别资产优势和劣势

**输入**：验证后的资产数据
**输出**：综合分析结果

#### 3.3 估值计算Agent (ValuatorAgent)

**职责**：
- 采用多种估值方法
  - 市场法 (Market Approach)
  - 收益法 (Income Approach)
  - 成本法 (Cost Approach)
- 参数优化
- 结果合理性验证

**输入**：资产数据和分析结果
**输出**：估值结果和价值区间

#### 3.4 报告生成Agent (ReportGeneratorAgent)

**职责**：
- 整合分析和估值结果
- 生成专业估值报告
- 支持多种输出格式

**输入**：完整的资产和分析数据
**输出**：专业评估报告

## 数据流转

```
原始资产数据
     ↓
[数据采集Agent] → 验证后的资产数据
     ↓
[资产分析Agent] → 分析结果
     ↓
[估值计算Agent] → 估值结果
     ↓
[报告生成Agent] → 最终报告
```

## 关键接口

### WorkflowOrchestrator

```python
async def execute_valuation_workflow(
    asset_id: str,
    asset_data: Dict[str, Any],
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]
```

执行完整的估值工作流，返回包含所有阶段结果的字典。

## 扩展设计

### 支持新的Agent

继承 `BaseAgent` 类并实现 `execute` 方法：

```python
class MyCustomAgent(BaseAgent):
    def __init__(self, knowledge_base: KnowledgeBase):
        super().__init__(knowledge_base, "CustomAgent")
    
    async def execute(self, *args, **kwargs) -> Dict[str, Any]:
        # 实现你的逻辑
        pass
```

### 支持新的估值方法

在 `ValuatorAgent` 中添加新方法：

```python
def _my_valuation_method(self, base_value: float, ...) -> Dict[str, Any]:
    # 实现新的估值方法
    pass
```

## 性能考虑

- 支持异步执行，提高并发处理能力
- 知识库使用内存存储，支持快速访问
- 支持批量处理多个资产
- 可扩展集成向量数据库用于相似度计算

## 错误处理

工作流包含完整的错误处理机制：
- 数据验证失败时的降级处理
- Agent执行异常的捕获和记录
- 工作流失败时的信息保存
