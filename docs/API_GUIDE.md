# API使用指南

## 快速开始

### 基本使用

```python
from src.core.workflow import WorkflowOrchestrator
import asyncio

# 初始化工作流
workflow = WorkflowOrchestrator()

# 准备资产数据
asset_data = {
    "name": "商业办公楼",
    "type": "房地产",
    "value": 5000000,
    "location": "市中心商业区",
    "condition": "良好",
    "age": 8,
    "useful_life": 50,
    "replacement_cost": 5500000,
    "annual_income": 400000,
}

# 执行估值工作流
result = await workflow.execute_valuation_workflow(
    asset_id="ASSET-001",
    asset_data=asset_data
)

# 访问结果
print(f"估值值: {result['valuation']['estimated_value']}")
print(f"报告:\n{result['report']}")
```

## 详细API文档

### WorkflowOrchestrator

#### `execute_valuation_workflow(asset_id, asset_data, config=None)`

执行完整的资产估值工作流。

**参数**：
- `asset_id` (str): 资产唯一标识
- `asset_data` (dict): 资产信息字典，包含以下字段：
  - `name` (str): 资产名称
  - `type` (str): 资产类型
  - `value` (float): 初始价值
  - `location` (str): 地点
  - `condition` (str): 状况
  - `age` (int): 年龄
  - `useful_life` (int): 使用年限
  - `replacement_cost` (float): 重置成本
  - `annual_income` (float): 年收益
- `config` (dict, optional): 配置参数

**返回值**：
```python
{
    "asset_id": str,
    "status": "success" | "failed",
    "collected_data": dict,           # 采集的数据
    "analysis": dict,                 # 分析结果
    "valuation": dict,                # 估值结果
    "report": str,                    # 生成的报告
    "duration_seconds": float,        # 执行时间
    "error": str                      # 错误信息（如果失败）
}
```

#### `get_asset_profile(asset_id)`

获取资产的完整信息，包括原始数据、分析结果和估值结果。

**参数**：
- `asset_id` (str): 资产ID

**返回��**：
```python
{
    "asset": dict,        # 原始资产数据
    "analysis": dict,     # 分析结果
    "valuation": dict,    # 估值结果
    "report": str,        # 生成的报告
}
```

#### `get_workflow_history()`

获取所有工作流执行历史。

**返回值**：
```python
[
    {
        "asset_id": str,
        "timestamp": str (ISO format),
        "status": "completed" | "failed"
    },
    ...
]
```

### 个别Agent

#### DataCollectorAgent

```python
agent = DataCollectorAgent(knowledge_base)
await agent.collect(asset_id, asset_data)
```

#### AssetAnalyzerAgent

```python
agent = AssetAnalyzerAgent(knowledge_base)
await agent.analyze(asset_id, asset_data)
```

#### ValuatorAgent

```python
agent = ValuatorAgent(knowledge_base)
await agent.valuate(asset_id, asset_data, analysis)
```

#### ReportGeneratorAgent

```python
agent = ReportGeneratorAgent(knowledge_base)
await agent.generate(asset_id, asset_data, analysis, valuation)
```

## 使用示例

### 示例1: 不动产评估

```python
real_estate_data = {
    "name": "高级写字楼",
    "type": "房地产 - 商业",
    "value": 3000000,
    "location": "市中心A区",
    "condition": "优秀",
    "age": 5,
    "useful_life": 70,
    "replacement_cost": 3200000,
    "annual_income": 200000,
}

result = await workflow.execute_valuation_workflow(
    asset_id="RE-OFFICE-001",
    asset_data=real_estate_data
)
```

### 示例2: 设备评估

```python
equipment_data = {
    "name": "生产线设备",
    "type": "机械 - 工业设备",
    "value": 800000,
    "location": "生产车间",
    "condition": "良好",
    "age": 4,
    "useful_life": 20,
    "replacement_cost": 900000,
    "annual_income": 150000,
}

result = await workflow.execute_valuation_workflow(
    asset_id="EQ-PROD-001",
    asset_data=equipment_data
)
```

### 示例3: 批量评估

```python
assets = [
    {"id": "ASSET-001", "data": {...}},
    {"id": "ASSET-002", "data": {...}},
    {"id": "ASSET-003", "data": {...}},
]

results = []
for asset in assets:
    result = await workflow.execute_valuation_workflow(
        asset_id=asset["id"],
        asset_data=asset["data"]
    )
    results.append(result)

print(f"完成 {len(results)} 个资产的评估")
```

## 错误处理

```python
result = await workflow.execute_valuation_workflow(
    asset_id="ASSET-001",
    asset_data=asset_data
)

if result["status"] == "success":
    print(f"估值成功: {result['valuation']['estimated_value']}")
else:
    print(f"估值失败: {result['error']}")
```
