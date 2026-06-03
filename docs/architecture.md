# 架构总览

## 系统框图

```
┌──────────────────────────────────────────────────────────┐
│  前端 (Next.js)                                          │
│  - 项目列表 / PDF 上传 / 对话 / 大纲 / 编辑器            │
└──────────────────┬───────────────────────────────────────┘
                   │ HTTP/JSON
┌──────────────────▼───────────────────────────────────────┐
│  后端 (FastAPI)                                          │
│  - /papers  /library  /chat  /outline  /generate        │
└──────────────────┬───────────────────────────────────────┘
                   │
       ┌───────────┼───────────┬──────────────┐
       ▼           ▼           ▼              ▼
    PyMuPDF     BGE-M3      Hybrid 检索     LLM 路由
   (PDF 解析)  (Embedding)  (BM25+dense)   (DS+MiniMax)
       │           │           │              │
       ▼           ▼           ▼              ▼
    本地文件    ChromaDB    BGE-Reranker   DeepSeek/MiniMax
                  │              │            (云 API)
                  ▼              ▼
              参考库 chunks  精排后 chunks
```

## 数据流

### 上传阶段
1. 用户上传 PDF → 后端存到 `data/papers/`
2. 后台任务:PyMuPDF 解析 → 抽文+图 → 文本分块(jsonl)
3. BGE-M3 embedding → ChromaDB

### 生成阶段
1. 用户输入标题 → 多轮对话澄清
2. DeepSeek 生成大纲(章节列表)
3. 逐节:Hybrid 检索 → BGE Rerank → 写初稿
4. 改稿 loop:Feedback → Edit → 跑 1-2 轮
5. Post-hoc 引用补全
6. 输出 Markdown → 前端展示

## 借鉴开源项目

详见 [based_on_opensource.md](based_on_opensource.md)

- **paper-qa**: 引用追踪 + 两阶段 LLM
- **MedRAG**: RRF 检索 + iBKP 循环
- **OpenScholar**: Feedback 改稿 + Post-hoc 归因
