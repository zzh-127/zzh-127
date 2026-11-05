# Apache Commons CLI 1.9.0 开源许可证合规扫描脚本
# 使用 ScanCode Toolkit 扫描，输出 JSON / HTML / SPDX 三种报告
$ErrorActionPreference = 'Stop'

$proj = Split-Path -Parent $MyInvocation.MyCommand.Path
$scancode = Join-Path $proj '.venv\Scripts\scancode.exe'
$src = Join-Path $proj 'src\commons-cli-1.9.0-src'
$reports = Join-Path $proj 'reports'

if (-not (Test-Path $scancode)) {
    Write-Host '未找到 ScanCode，请先执行: python -m venv .venv; .venv\Scripts\pip install scancode-toolkit'
    exit 1
}
if (-not (Test-Path $src)) {
    Write-Host "未找到源码目录: $src"
    exit 1
}
New-Item -ItemType Directory -Force -Path $reports | Out-Null

& $scancode -clipeu `
    --json-pp  (Join-Path $reports 'commons-cli-1.9.0-scan.json') `
    --html-app (Join-Path $reports 'commons-cli-1.9.0-scan.html') `
    --spdx-tv  (Join-Path $reports 'commons-cli-1.9.0-scan.spdx') `
    $src

Write-Host "扫描完成，报告位于: $reports"
