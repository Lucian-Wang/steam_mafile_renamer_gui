import os
import json
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def rename_mafiles(src_dir, dst_dir, log_func):
    count = 0
    for filename in os.listdir(src_dir):
        if filename.endswith('.maFile') and filename[:-7].isdigit():
            src_path = os.path.join(src_dir, filename)
            try:
                with open(src_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                account_name = data.get('account_name')
                if account_name:
                    new_filename = f"{account_name}.maFile"
                    dst_path = os.path.join(dst_dir, new_filename)
                    if not os.path.exists(dst_path):
                        shutil.copy2(src_path, dst_path)
                        log_func(f"复制: {filename} -> {new_filename}")
                        count += 1
                    else:
                        log_func(f"跳过(目标已存在): {new_filename}")
                else:
                    log_func(f"跳过(无account_name): {filename}")
            except Exception as e:
                log_func(f"处理{filename}出错: {e}")
    log_func(f"\n处理完成，共成功复制并重命名 {count} 个文件。")

def select_src():
    folder = filedialog.askdirectory(title="选择源文件夹(A)")
    if folder:
        src_entry.delete(0, tk.END)
        src_entry.insert(0, folder)

def select_dst():
    folder = filedialog.askdirectory(title="选择目标文件夹(B)")
    if folder:
        dst_entry.delete(0, tk.END)
        dst_entry.insert(0, folder)

def start():
    src = src_entry.get()
    dst = dst_entry.get()
    log_area.delete(1.0, tk.END)
    if not src or not dst:
        messagebox.showerror("错误", "请选择源文件夹和目标文件夹！")
        return
    if src == dst:
        messagebox.showerror("错误", "源文件夹和目标文件夹不能相同！")
        return
    rename_mafiles(src, dst, lambda msg: log_area.insert(tk.END, msg + '\n'))

# GUI设置
root = tk.Tk()
root.title("Steam maFile 批量重命名工具")
root.geometry("600x400")

tk.Label(root, text="源文件夹(A):").pack(anchor='w', padx=10, pady=5)
src_frame = tk.Frame(root)
src_entry = tk.Entry(src_frame, width=60)
src_entry.pack(side=tk.LEFT, padx=5)
tk.Button(src_frame, text="选择", command=select_src).pack(side=tk.LEFT)
src_frame.pack(padx=10, fill='x')

tk.Label(root, text="目标文件夹(B):").pack(anchor='w', padx=10, pady=5)
dst_frame = tk.Frame(root)
dst_entry = tk.Entry(dst_frame, width=60)
dst_entry.pack(side=tk.LEFT, padx=5)
tk.Button(dst_frame, text="选择", command=select_dst).pack(side=tk.LEFT)
dst_frame.pack(padx=10, fill='x')

tk.Button(root, text="开始批量处理", command=start, height=2, bg='green', fg='white').pack(pady=15)

log_area = scrolledtext.ScrolledText(root, width=70, height=12)
log_area.pack(padx=10, pady=5, fill='both', expand=True)

tk.Label(root, text="灯火通明（济宁）网络有限公司").pack(side='right', padx=10, pady=5)

root.mainloop()