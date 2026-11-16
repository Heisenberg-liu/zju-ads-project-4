# 程序入口与运行

当前提交入口为仓库根目录 `main.c`；`main/main.c` 为同内容副本，修改时需同步。本目录用于源码维护说明，测试时也可通过 `--source main/main.c` 指定该副本。

在仓库根目录编译（先创建 build 目录）：

```sh
gcc -std=c11 -O2 -Wall -Wextra main.c -o build/main -lm
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force build | Out-Null
gcc -std=c11 -O2 -Wall -Wextra main.c -o build/main.exe -lm
Get-Content data/01_boundary.in | & .\build\main.exe
```

Linux/macOS：

```sh
mkdir -p build
gcc -std=c11 -O2 -Wall -Wextra main.c -o build/main -lm
./build/main < data/01_boundary.in
```

每次运行读取一个测试用例：第一行 n、m，第二行 n 个正整数。只输出答案并换行。问题与修复记录见仓库 `docs/纠错清单.md`。
