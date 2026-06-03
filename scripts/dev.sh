#!/bin/bash
# 一键启动开发环境
set -e
source "$(dirname "$0")/env.sh"

echo "🚀 启动后端 + 前端 (Docker Compose)..."
docker compose up --build
