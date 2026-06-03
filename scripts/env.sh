#!/bin/bash
# 项目环境设置脚本
# 用法:source scripts/env.sh

# 修复 Synology 精简版 git 的 remote-https 问题
export GIT_EXEC_PATH=/var/apps/git/target/libexec/git-core

# 切到项目根目录
cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "✅ 环境已设置,当前目录: $(pwd)"
echo "   GIT_EXEC_PATH=$GIT_EXEC_PATH"
