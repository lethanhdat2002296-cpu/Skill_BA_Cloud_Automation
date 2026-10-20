#!/usr/bin/env bash
# Dán nội dung file này vào "Setup script" của cloud environment trên claude.ai/code.
# Ngoại lệ duy nhất dùng .sh trong repo (vì cloud environment yêu cầu shell script).
# Nếu bước tải Chromium/npm bị chặn mạng: thêm domain vào Network access của environment
#   (pypi.org, files.pythonhosted.org, registry.npmjs.org, playwright.azureedge.net,
#    playwright.download.prss.microsoft.com, cdn.playwright.dev, storage.googleapis.com, deb.debian.org / archive.ubuntu.com).
set -e

apt-get update && apt-get install -y pandoc fonts-dejavu-core
pip install --break-system-packages playwright
python -m playwright install --with-deps chromium
npm install -g @mermaid-js/mermaid-cli
