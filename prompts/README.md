# Prompts 集中管理

所有 LLM 调用的 prompt 模板统一放在这里,按命名空间组织:

```
prompts/
├── outline/             # 大纲生成
├── section_writing/     # 章节写作
├── revision/            # 改稿
├── attribution/         # 引用归因
└── figure/              # 图表理解
```

## 设计原则

1. **每个 prompt 单独一个 .md 文件** - 便于版本管理、对比实验
2. **顶部 metadata 注释** - 标明借鉴自哪个开源项目、改动历史
3. **变量用 `{{var_name}}` 占位** - 后端代码用 Jinja2 渲染

## Prompt 来源

| Prompt | 借鉴自 | 状态 |
|---|---|---|
| `outline/system.md` | 自研 | P3 阶段编写 |
| `section_writing/system.md` | paper-qa `qa_prompt` | P3 阶段编写 |
| `revision/feedback.md` | OpenScholar `instruction_feedback` | P4 阶段编写 |
| `attribution/posthoc.md` | OpenScholar `posthoc_attributions_paragraph_all` | P4 阶段编写 |
| `figure/description.md` | paper-qa `individual_media_enrichment_prompt_template` | P5 阶段编写 |

## 模板

```markdown
<!--
Source: paper-qa (Apache-2.0)
Modified: 2026-06-03 - 翻译为中文,适配医学领域
-->

你是一名{{specialty}}领域的医学专家,...

任务: {{task}}
输入: {{input}}
输出: {{output_format}}
```

## 版本管理

- 修改 prompt 后,提交 git 时**必须**在 commit message 写明效果
- 重要的 prompt 调整同时记录到 `docs/prompt_changelog.md`
