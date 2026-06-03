# 医学论文智能助手 (Med Paper Assistant)

> 基于开源项目的医学综述写作助手:用户上传 PDF(英文为主),通过 AI 对话 + 自动检索,生成中文医学综述初稿。

## 🌟 功能特性

- 📤 **PDF 上传与解析**:支持多 PDF 上传,自动抽取文本和图表
- 💬 **AI 对话澄清需求**:用户给标题或对话式澄清论文方向
- 📝 **自动生成中文综述**:基于参考库 + RAG + DeepSeek/MiniMax 生成大纲和正文
- 🔬 **图表理解**:用 VLM 自动描述参考论文中的图表
- 📚 **引用追踪**:每条事实可追溯到参考原文,带位置锚点

## 🏗️ 技术栈

| 层 | 选型 | 来源 |
|---|---|---|
| 前端 | Next.js 14 + TypeScript + Tailwind | 开源 |
| 后端 | FastAPI (Python 3.11) | 开源 |
| 数据库 | SQLite + ChromaDB | 开源 |
| PDF 解析 | PyMuPDF + pymupdf4llm | 开源 |
| Embedding | BGE-M3 | 开源(本地 CPU) |
| 大模型 | DeepSeek-V3 + MiniMax | API |

## 🧬 借鉴的开源项目

本项目设计与实现参考了 3 个优秀的开源 RAG 系统(均 Apache-2.0 / MIT 协议):

| 项目 | 借鉴点 |
|---|---|
| [paper-qa](https://github.com/Future-House/paper-qa) | 引用追踪 + 两阶段 LLM 评估 |
| [MedRAG](https://github.com/Teddy-XiongGZ/MedRAG) | RRF 混合检索 + iBKP 迭代循环 |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar) | Feedback 改稿 + Post-hoc 引用补全 |

详见 [`docs/based_on_opensource.md`](docs/based_on_opensource.md)。

## 🚀 快速开始

```bash
# 1. 复制环境配置
cp .env.example .env
# 编辑 .env 填入 DeepSeek/MiniMax API key

# 2. 启动所有服务
docker compose up -d

# 3. 访问
# 前端:http://localhost:3000
# 后端 API:http://localhost:8000
# API 文档:http://localhost:8000/docs
```

## 📂 目录结构

```
med-paper-assistant/
├── backend/        # FastAPI 后端
├── frontend/       # Next.js 前端
├── prompts/        # 所有 prompt 集中存放
├── docs/           # 架构和借鉴说明
└── docker-compose.yml
```

## 🛣️ 开发路线

- [x] **P0 骨架**:项目初始化、仓库搭建
- [ ] **P1 PDF 解析**:上传 → 抽文+图 → 入库
- [ ] **P2 检索**:Hybrid(BM25+dense)→ Rerank → 问答
- [ ] **P3 单段写作**:大纲 + 检索参考 + 写一节中文
- [ ] **P4 改稿 loop**:整体改稿 + 引用补全
- [ ] **P5 图表 + 编辑器**:VLM 描述 + Tiptap/MD 编辑器
- [ ] **P6 优化**:医学 embedding、引用校验、内网映射

## 💰 成本估算

- DeepSeek-V3: ~¥10-30/月(按每天 10 篇综述)
- MiniMax API: Coding Plan 内基本不额外花钱
- 总计: **¥30/月以内**

## 📄 License

本项目以学术与个人使用为目的。代码部分开源,但请遵守上游开源项目(paper-qa、MedRAG、OpenScholar)的 License。
