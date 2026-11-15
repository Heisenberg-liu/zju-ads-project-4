"""生成测试输入及参照答案：python scripts/gen.py [--random 20 --seed 42]。"""
import argparse
from pathlib import Path
import random
import ref

ROOT = Path(__file__).resolve().parents[1]
# 名称、m、输入序列；以下均为自行设计的测试，不是官方样例。
SUITE = [
    ("01_boundary", 3, [2, 5]),
    ("02_no_pair", 3, [2, 6]),
    ("03_duplicates", 1, [7] * 5),
    ("04_extend", 1, [1, 2, 100]),
    ("05_skip", 1, [1, 100, 2]),
    ("06_overlap", 1, [1, 2, 3, 4]),
    ("07_alternating", 1, [1, 3, 1, 3]),
    ("08_limits", 1000, [1, 1001, 99000, 100000]),
    ("09_all_far", 1, [1, 10, 20, 30, 40]),
    ("10_decreasing", 1, [4, 3, 2, 1]),
]

def generate(count=20, seed=42):
    cases = list(SUITE)
    rng = random.Random(seed)
    for i in range(count):
        n, m = rng.randint(2, 12), rng.randint(1, 5)
        a = [rng.randint(1, 15) for _ in range(n)]
        cases.append((f"random_{i:04d}", m, a))
    folder = ROOT / "data" / "generated"
    folder.mkdir(parents=True, exist_ok=True)
    paths = []
    for name, m, a in cases:
        text = f"{len(a)} {m}\n" + " ".join(map(str, a)) + "\n"
        path = folder / (name + ".in")
        path.write_text(text, encoding="utf-8")
        path.with_suffix(".out").write_text(str(ref.solve(a, m)) + "\n", encoding="utf-8")
        paths.append(path)
    # 只测试本次生成的清单，不受上次遗留文件影响。
    return paths

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--random", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if args.random < 0:
        parser.error("--random 不能为负数")
    paths = generate(args.random, args.seed)
    print(f"已生成 {len(paths)} 组输入与答案：{ROOT / 'data' / 'generated'}")

if __name__ == "__main__":
    main()
