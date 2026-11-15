"""评测流程：生成数据 -> 编译 main.c -> 运行 -> 比较答案并打印表格。

用法：python scripts/run_tests.py
生成的数据及答案保存在 data/generated/，不会改写手工维护的 data/*.in。
"""
import argparse
from pathlib import Path
import re
import subprocess
import sys
import time
import gen

ROOT = Path(__file__).resolve().parents[1]

def run_case(path, exe, timeout):
    text = path.read_text(encoding="utf-8")
    expected = int(path.with_suffix(".out").read_text(encoding="utf-8"))
    n, m = map(int, text.splitlines()[0].split())
    start = time.perf_counter()
    try:
        result = subprocess.run([str(exe)], input=text, capture_output=True,
                                text=True, errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired:
        return n, m, time.perf_counter() - start, [f"超时（>{timeout}s）"]
    elapsed = time.perf_counter() - start
    errors = []
    if result.returncode != 0:
        errors.append(f"非正常退出：{result.returncode}")
    output = result.stdout.strip()
    if not re.fullmatch(r"[0-9]+", output):
        errors.append(f"应只输出一个非负整数，实际：{output!r}")
    elif int(output) != expected:
        errors.append(f"答案错误：期望 {expected}，实际 {output}")
    if result.returncode != 0 and result.stderr:
        errors.append(result.stderr.strip())
    return n, m, elapsed, errors

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--random", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--source", default="main.c")
    parser.add_argument("--cc", default="gcc")
    parser.add_argument("--timeout", type=float, default=3)
    args = parser.parse_args()
    if args.random < 0 or args.timeout <= 0:
        parser.error("随机用例数不能为负，超时秒数必须大于 0")

    # 1. 生成输入和答案；也纳入 data/ 下已有的固定或手工测试。
    fixed = sorted((ROOT / "data").glob("*.in"))
    generated = gen.generate(args.random, args.seed)
    names = {path.name for path in fixed}
    paths = fixed + [path for path in generated if path.name not in names]
    # 2. 编译当前源码。
    build = ROOT / "build"
    build.mkdir(exist_ok=True)
    exe = build / ("main.exe" if sys.platform == "win32" else "main")
    subprocess.run([args.cc, "-std=c11", "-O2", "-Wall", "-Wextra",
                    str(ROOT / args.source), "-o", str(exe), "-lm"], check=True, timeout=60)
    # 3. 逐个运行并比较，样式参考 Project 3 的 judge.py。
    print(f"{'case':<34}{'N':>5}{'M':>5}  result  time")
    passed, worst = 0, 0.0
    for path in paths:
        n, m, elapsed, errors = run_case(path, exe, args.timeout)
        passed += not errors
        worst = max(worst, elapsed)
        name = path.relative_to(ROOT / "data").as_posix()
        print(f"{name:<34}{n:>5}{m:>5}  {'FAIL' if errors else 'PASS'}  {elapsed:.3f}s")
        for error in errors:
            print(f"    - {error}")
    print(f"[summary] {passed}/{len(paths)} 通过，最慢 {worst:.3f}s")
    print("输入和答案见 data/ 与 data/generated/，失败用例可直接手动复现。")
    return int(passed != len(paths))

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"评测无法完成：{error}", file=sys.stderr)
        sys.exit(1)
