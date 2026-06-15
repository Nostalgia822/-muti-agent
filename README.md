# 资产评估全流程Multi-Agent框架

一个基于多智能体架构的资产评估全流程自动化系统，支持数据采集、分析、评估、报告生成等完整工作流。

## 项目架构

```
┌─────────────────────────────────────────────────────┐
│          工作流编排层 (Workflow Orchestrator)       │
└────────────────────┬────────────────────────────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
┌───▼───┐      ┌────▼────┐      ┌───▼──────┐
│数据采集│      │资产分析 │      │评估计算  │
│Agent  │      │Agent    │      │Agent     │
└───┬───┘      └────┬────┘      └───┬──────┘
    │                │                │
    │          ┌─────▼─────┐         │
    │          │  内存数据库 │         │
    │          │  (Knowledge)       │
    │          └─────┬─────┘         │
    │                │                │
    └────────────────┼────────────────┘
                     │
        ┌────────────▼───────────┐
        │  报告生成 & 输出Agent   │
        └────────────────────────┘
```

## 核心功能模块

### 1. 数据采集Agent (Data Collection Agent)
- 从各种数据源采集资产信息
- 数据验证和清洗
- 存储到知识库

### 2. 资产分析Agent (Asset Analysis Agent)
- 分析资产特征
- 市场对标分析
- 风险评估

### 3. 评估计算Agent (Valuation Agent)
- 多种评估方法计算（收益法、成本法、市场法）
- 参数优化
- 结果验证

### 4. 报告��成Agent (Report Generation Agent)
- 整合分析结果
- 生成专业评估报告
- 输出可视化图表

## 技术栈

- **框架**: LangChain / AutoGen
- **LLM**: OpenAI GPT-4 / Claude
- **数据库**: 内存 + 向量数据库 (Chroma/Weaviate)
- **API**: FastAPI
- **前端**: Streamlit / React

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件

# 运行演示
python main.py

# 启动Web界面
streamlit run app.py
```

## 项目结构

```
.
├── src/
│   ├── agents/                    # Agent实现
│   │   ├── data_collector.py
│   │   ├── asset_analyzer.py
│   │   ├── valuator.py
│   │   └── report_generator.py
│   ├── core/                      # 核心模块
│   │   ├── workflow.py           # 工作流编排
│   │   ├── knowledge_base.py     # 知识库
│   │   └── config.py             # 配置管理
│   ├── tools/                     # 工具函数
│   │   ├── data_processing.py
│   │   ├── calculations.py
│   │   └── visualization.py
│   └── api/                       # API接口
│       └── routes.py
├── config/                        # 配置文件
├── tests/                         # 测试
├── examples/                      # 示例
└── docs/                          # 文档
```

## 工作流示例

详见 `examples/asset_valuation_workflow.py`

## 贡献指南

欢迎提交Issue和PR！

## 许可证

MIT
