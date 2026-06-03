#!/bin/bash
# 一键 git 提交并推送(自动带 GIT_EXEC_PATH)
set -e
source "$(dirname "$0")/env.sh"

if [ -z "$1" ]; then
    echo "用法: ./scripts/push.sh \"提交信息\""
    exit 1
fi

git add .
git commit -m "$1"
git push
