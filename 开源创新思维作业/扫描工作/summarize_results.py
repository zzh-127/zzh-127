# -*- coding: utf-8 -*-
"""ScanCode 扫描结果 JSON 快速分析工具。

用法:
    python summarize_results.py <scancode-json-path>

输出: 文件总数、许可证分布、版权声明统计、包信息等要点。
"""
import json
import collections
import sys

def main():
    if len(sys.argv) < 2:
        print("用法: python summarize_results.py <scancode-json-path>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        d = json.load(f)

    files = d.get("files") or []
    print("scanned files:", len(files))

    expr_counts = collections.Counter()
    for x in files:
        e = x.get("detected_license_expression_spdx") or "NOASSERTION"
        expr_counts[e] += 1
    print("== per-file detected license expression (SPDX) ==")
    for k, v in expr_counts.most_common(15):
        print(f"  {v:4d}  {k}")

    cpr_total = sum(1 for x in files if x.get("copyrights"))
    print("files with copyrights:", cpr_total)

    pkgs = d.get("packages") or []
    print("packages:", len(pkgs))
    for p in pkgs:
        print("  pkg:", p.get("type"), p.get("name"), p.get("version"),
              "| declared license:", p.get("declared_license_expression"))

    h = (d.get("headers") or [{}])[0]
    print("scancode version:", h.get("tool_version"), "| duration:", h.get("duration"))

if __name__ == "__main__":
    main()
