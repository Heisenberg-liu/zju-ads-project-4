# ADS Project 4 — Beautiful Subsequences

统计给定整数序列中的 beautiful 子序列，答案对 1000000007 取模。子序列只需存在一对相邻元素之差的绝对值不超过 m；相邻指选出的子序列中的相邻位置。不同下标选择分别计数，输入允许重复数字。

## 项目状态

当前 `main.c` 为提交实现，测试结果见 [实验报告](docs/report/Report.md)。开发过程中的问题与修复见 [纠错清单](docs/纠错清单.md)。测试期望值由独立穷举生成。

## 目录

```text
main.c                  当前程序入口（保留原位置）
main/README.md          编译、运行与源码维护说明
docs/分工文件.md         两人分工及交付流程
docs/算法设计.md         状态定义、转移及复杂度
docs/测试说明.md         测试方法与覆盖范围
docs/纠错清单.md         开发中的问题、修复与复核结论
data/*.in, *.out         独立测试输入与期望输出
scripts/gen.py           单独生成测试输入和答案并保存
scripts/ref.py           小数据穷举参照答案
scripts/run_tests.py     编译运行、答案比较和耗时表格
```

## 快速开始

需要 GCC 和 Python 3。在仓库根目录执行：

```sh
python scripts/gen.py
python scripts/run_tests.py
python scripts/run_tests.py --random 200 --seed 42
```

脚本编译根目录 `main.c`，打印结果，失败返回非零退出码。随机测试使用 n ≤ 12 的独立穷举判定。大规模性能测试需另行计时；不能由小数据测试推断是否满足评测时限。

单独编译运行见 [main 使用说明](main/README.md)。

## 团队

- 刘钰栋：编写代码、修复实现、执行测试并记录结果。
- 郭其安：撰写报告、核对算法与代码、发现问题并复核修复。

详细安排见 [分工文件](docs/分工文件.md)。


