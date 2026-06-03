"""
医学论文智能助手 - 后端入口
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

app = FastAPI(
    title="医学论文智能助手 API",
    description="基于 RAG 的医学综述写作助手",
    version="0.1.0",
)

# CORS 配置(开发阶段允许所有来源)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "name": "医学论文智能助手",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/v1/info")
def api_info():
    return {
        "deepseek_configured": bool(settings.deepseek_api_key),
        "MiniMax_configured": bool(settings.MiniMax_api_key),
        "embedding_model": settings.embedding_model,
        "data_dir": str(settings.data_dir),
    }


# P1 之后会挂载的路由(暂时注释)
# from app.routers import papers, library, chat, outline, generate
# app.include_router(papers.router, prefix="/api/v1/papers", tags=["papers"])
# app.include_router(library.router, prefix="/api/v1/library", tags=["library"])
# app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])
# app.include_router(outline.router, prefix="/api/v1/outline", tags=["outline"])
# app.include_router(generate.router, prefix="/api/v1/generate", tags=["generate"])
