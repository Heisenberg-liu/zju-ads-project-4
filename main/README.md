# 程序入口与运行

当前唯一程序入口为仓库根目录 `main.c`。本目录用于源码维护说明，避免复制两份程序导致修改不同步。若后续迁移到 `main/main.c`，须同步更新测试脚本默认路径与 README；也可以通过 `--source main/main.c` 指定测试源码。

在仓库根目录编译（先创建 build 目录）：

```sh
gcc -std=c11 -O2 -Wall -Wextra main.c -o build/main -lm
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force build | Out-Null
gcc -std=c11 -O2 -Wall -Wextra main.c -o build/main.exe -lm
Get-Content data/01_boundary.in | & .uild\main.exe
```

Linux/macOS：

```sh
mkdir -p build
gcc -std=c11 -O2 -Wall -Wextra main.c -o build/main -lm
./build/main < data/01_boundary.in
```

每次运行读取一个测试用例：第一行 n、m，第二行 n 个正整数。只输出答案并换行。当前代码问题见 `docs/纠错清单.md`。
