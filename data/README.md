# 测试数据

每对同名 .in/.out 为独立测试。期望值通过枚举下标子集生成。文件名对应边界相等、无合格对、重复值、已有 beautiful 扩展、跳选、重叠数对、交错重复、值域边界、全部远离及递减序列。

| 用例 | 期望输出 |
| --- | --- |
| 01_boundary | 1 |
| 02_no_pair | 0 |
| 03_duplicates | 26 |
| 04_extend | 2 |
| 05_skip | 1 |
| 06_overlap | 8 |
| 07_alternating | 4 |
| 08_limits | 7 |
| 09_all_far | 0 |
| 10_decreasing | 8 |
