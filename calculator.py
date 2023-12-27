import tkinter as tk


def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)


def on_clear_click():
    entry.delete(0, tk.END)


def on_calc_click():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# 创建主窗口
root = tk.Tk()
root.title("简易计算器")

# 创建显示结果的文本框
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# 创建按钮
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=10, command=on_calc_click).grid(row=row, column=col, columnspan=2)
    elif button == 'C':
        tk.Button(root, text=button, width=10, command=on_clear_click).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, command=lambda val=button: on_button_click(val)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 运行主循环
root.mainloop()
