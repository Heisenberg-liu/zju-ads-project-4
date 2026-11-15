"""小数据参照答案：直接枚举所有下标选择，不使用被测程序的 DP。"""

def solve(a, m):
    if len(a) > 20:
        raise ValueError("穷举仅用于 n <= 20 的小数据")
    answer = 0
    for mask in range(1 << len(a)):
        selected = [a[i] for i in range(len(a)) if mask & (1 << i)]
        if any(abs(x - y) <= m for x, y in zip(selected, selected[1:])):
            answer += 1
    return answer % 1000000007
