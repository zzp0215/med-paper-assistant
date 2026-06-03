# 基于开源项目的设计说明

本项目严格基于以下 3 个开源 RAG 系统进行二次开发,**不直接 import 它们作为依赖**,而是**借鉴其设计模式 + 自行实现**。这样做的原因:
1. 上游项目大多绑定 OpenAI API / GPU 推理栈
2. 中文支持需要全面改造
3. 直接依赖会引入版本兼容性问题

## 借鉴的开源项目

### 1. [paper-qa](https://github.com/Future-House/paper-qa)(Apache-2.0)

**作者**:FutureHouse  
**借鉴点**:

| 我们模块 | 借鉴内容 | 借鉴方式 |
|---|---|---|
| `services/citation_service.py` | 引用 key 体系(`(ref-XXXXXXXX)`) | 抄约束 prompt + 后处理正则 |
| `services/section_writer.py` | 两阶段 LLM 评估范式 | 抄核心流程,改中文 prompt |
| `prompts/relevance_eval.md` | `summary_prompt` 模板 | 翻译 + 适配医学领域 |

**License 兼容**: ✅ Apache-2.0 可商用

---

### 2. [MedRAG](https://github.com/Teddy-XiongGZ/MedRAG)(MIT)

**作者**:Teddy Xiong  
**借鉴点**:

| 我们模块 | 借鉴内容 | 借鉴方式 |
|---|---|---|
| `services/retriever.py` | RRF 混合检索公式 | **直接抄 8 行核心代码** |
| `services/chunker.py` | jsonl chunk 存储格式 | 抄 `{id, title, content}` 字段定义 |
| `services/llm_router.py` | 多 LLM 路由的 if-elif 分支 | 抄结构,接 DeepSeek/MiniMax |
| `services/section_writer.py` | `title + ". " + content` 拼 embedding | 直接抄 |

**License 兼容**: ✅ MIT 可商用

---

### 3. [OpenScholar](https://github.com/AkariAsai/OpenScholar)(Apache-2.0)

**作者**:Akari Asai et al. (AllenAI)  
**借鉴点**:

| 我们模块 | 借鉴内容 | 借鉴方式 |
|---|---|---|
| `services/reviser.py` | Feedback 改稿循环 | 抄 `Feedback: ...` + `Question: ...` 格式 |
| `services/reviser.py` | Edit-with-feedback prompt | 抄 "只改需要改的部分,其他不变" 约束 |
| `services/attribution.py` | **Post-hoc 引用补全** ⭐ | 抄 "扫描无引用句子 + 补 [N]" |
| `services/reranker.py` | BGE-reranker 调用 | 直接 import FlagReranker |
| `services/section_writer.py` | `[Response_Start]`/`[Response_End]` 解析 | 抄标记规范 |

**License 兼容**: ✅ Apache-2.0 可商用

---

## 我们的自研部分

| 模块 | 说明 |
|---|---|
| `services/survey_pipeline.py` | 长综述 pipeline(大纲→分章→归并→改稿) |
| `services/figure_describer.py` | 图表描述(翻译 paper-qa 70 行 prompt) |
| `routers/chat.py` | 多轮需求澄清(自研对话管理) |
| `routers/outline.py` | 综述大纲生成(自研 prompt) |
| `app/db.py` | SQLite + SQLAlchemy ORM |

---

## 不借鉴的项目(以及原因)

| 项目 | 不借鉴原因 |
|---|---|
| **ChatPaper** | 单篇速读范式,不匹配多篇综述;且已停更 |
| **PDF-Extract-Kit** | 几乎所有模型要 GPU,无 GPU 跑不动 |
| **MinerU** | 同样强 GPU 依赖 |

---

## License 声明

本项目代码部分采用 MIT License。  
使用过程中,所有 prompt 模板、引用规范的原始设计归属于:
- paper-qa (Apache-2.0)
- MedRAG (MIT)
- OpenScholar (Apache-2.0)

如本项目公开发布,需在 README 中保留上述致谢。
