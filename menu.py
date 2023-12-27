import tkinter as tk


def file_new():
    print("执行新建操作")


def file_open():
    print("执行打开操作")


def file_save():
    print("执行保存操作")


def edit_cut():
    print("执行剪切操作")


def edit_copy():
    print("执行复制操作")


def edit_paste():
    print("执行粘贴操作")


root = tk.Tk()
root.title("菜单示例")

# 创建菜单栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 创建文件菜单
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="新建", command=file_new)
file_menu.add_command(label="打开", command=file_open)
file_menu.add_command(label="保存", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)

# 创建编辑菜单
edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="编辑", menu=edit_menu)
edit_menu.add_command(label="剪切", command=edit_cut)
edit_menu.add_command(label="复制", command=edit_copy)
edit_menu.add_command(label="粘贴", command=edit_paste)

root.mainloop()
