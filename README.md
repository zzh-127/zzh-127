# 藏智慧

藏智慧（学号 f25011301）的课程作业与练习仓库，收录开源微专业课程作业、开源许可证合规扫描报告等。

## 目录结构

| 目录 / 文件 | 内容说明 |
| --- | --- |
| `开源创新思维作业/f25011301-藏智慧-作业1.docx` | 平时作业 1：开源许可证合规扫描报告（Word，含项目介绍、工具安装过程及问题、工具输出检测报告、报告详细分析四部分） |
| `开源创新思维作业/扫描工作/` | ScanCode 扫描 Apache Commons CLI 1.9.0 生成的完整报告：`commons-cli-1.9.0-scan.json`（机器可读）、`commons-cli-1.9.0-scan.html`（浏览器可视化）、`commons-cli-1.9.0-scan.spdx`（SPDX 标准格式），以及扫描脚本 `run_scan.ps1` 与统计脚本 `summarize_results.py` |

## 技术栈

- Python（ScanCode 许可证扫描、结果统计）
- Word / Markdown（作业报告）

## 运行说明

扫描工作目录可执行：

```
run_scan.ps1                                    # 一键扫描（Windows PowerShell）
python summarize_results.py <报告.json>          # 输出扫描统计
```

## 作者

藏智慧 · f25011301
