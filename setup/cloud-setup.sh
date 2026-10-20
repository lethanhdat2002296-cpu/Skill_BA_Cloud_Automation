#!/usr/bin/env bash
# Dán nội dung file này vào "Setup script" của cloud environment trên claude.ai/code.
# Ngoại lệ duy nhất dùng .sh trong repo (vì cloud environment yêu cầu shell script).
# Nếu bước tải Chromium/npm bị chặn mạng: thêm domain vào Network access của environment
#   (pypi.org, files.pythonhosted.org, registry.npmjs.org, playwright.azureedge.net,
#    playwright.download.prss.microsoft.com, cdn.playwright.dev, storage.googleapis.com, deb.debian.org / archive.ubuntu.com).
# Image cloud đã có sẵn pandoc, font và Chromium (PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers)
# → chỉ cài phần còn thiếu, không tải lại Chromium.
set -e

if ! command -v pandoc >/dev/null || ! fc-list | grep -qi dejavu; then
  apt-get update && apt-get install -y pandoc fonts-dejavu-core
fi

pip install --break-system-packages playwright
if ! python3 -c "from playwright.sync_api import sync_playwright as s; p = s().start(); p.chromium.launch().close(); p.stop()" 2>/dev/null; then
  python3 -m playwright install --with-deps chromium
fi

command -v mmdc >/dev/null || npm install -g @mermaid-js/mermaid-cli
