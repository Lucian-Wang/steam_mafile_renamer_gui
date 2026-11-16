# Steam maFile 批量重命名工具

本项目是一个用于批量重命名 Steam maFile 文件的图形化工具，支持将以数字命名的 `.maFile` 文件批量复制、重命名为对应的 Steam 账号名，便于管理和查找。

## 功能特性

- 批量读取指定文件夹内的 `.maFile` 文件（如 `1234567890.maFile`）。
- 解析每个文件的 JSON 内容，获取 `account_name` 字段。
- 按 `account_name` 重命名并复制到目标文件夹，避免重复。
- 简洁易用的图形界面，无需命令行操作。
- 处理结果实时显示日志，便于追踪每一步。

## 使用方法

1. **安装依赖**  
   需先安装 Python 3 环境，并安装 `tkinter`（通常自带）。

2. **运行程序**  
   直接运行主程序：
   ```bash
   python steam_mafile_renamer_gui.py
   ```

3. **操作步骤**  
   - 点击“选择”按钮，分别选定源文件夹 (A) 和目标文件夹 (B)。
   - 点击“开始批量处理”，程序会自动将所有以数字命名且包含 `account_name` 字段的 `.maFile` 文件，重命名为 `{account_name}.maFile` 并复制到目标文件夹。
   - 日志区会显示详细的处理进度和结果。

4. **注意事项**
   - 源文件夹和目标文件夹不能相同。
   - 若目标文件夹已存在同名文件，则会跳过该文件。
   - 若文件缺少 `account_name` 字段或 JSON 格式错误，会在日志中提示。

## 打包说明

项目包含 `steam_mafile_renamer_gui.spec` 文件，使用 [PyInstaller](https://www.pyinstaller.org/) 可在目标操作系统上打包独立可执行文件（现有 dist 目录提供 Windows EXE）：

```bash
pyinstaller steam_mafile_renamer_gui.spec
```

生成的可执行文件默认无控制台窗口，打包参数可参考 `.spec` 文件。

## 依赖

- Python 3
- 标准库：os、json、shutil、tkinter

## 主要实现说明

- **核心功能**在 `steam_mafile_renamer_gui.py` 文件中实现。
- 使用 `tkinter` 构建 GUI，包括源/目标目录选择、日志显示、批量处理按钮等。
- `rename_mafiles` 函数负责核心的批量重命名与复制逻辑，支持错误处理与日志记录。
- 支持中文界面，操作提示与日志均为中文，便于国内用户使用。

## 作者信息

[Lucian](https://lucian.wang/)

---

如有问题或建议，欢迎提交 Issue 或 PR ！

## 维护与反馈

维护者：[Lucian](https://lucian.wang/) · 邮箱：im@lucian.wang · [问题反馈](https://github.com/Lucian-Wang/steam_mafile_renamer_gui/issues)
