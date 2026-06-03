"""
应用配置 - 从环境变量加载
"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # === 大模型 API ===
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com/v1"
    deepseek_model: str = "deepseek-chat"

    MiniMax_api_key: str = ""
    MiniMax_base_url: str = "https://api.MiniMax.com/v1"
    MiniMax_model: str = "MiniMax-sonnet-4-6"

    # === 服务配置 ===
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    debug: bool = True

    # === 数据存储 ===
    data_dir: Path = Path("./data")
    chroma_db_dir: Path = Path("./chroma_db")
    sqlite_db_path: Path = Path("./data/app.db")

    # === Embedding ===
    embedding_model: str = "BAAI/bge-m3"
    embedding_device: str = "cpu"
    embedding_batch_size: int = 8

    # === Reranker ===
    reranker_model: str = "BAAI/bge-reranker-large"
    reranker_device: str = "cpu"

    # === 检索 ===
    retrieval_top_k: int = 20
    rerank_top_k: int = 8


settings = Settings()
