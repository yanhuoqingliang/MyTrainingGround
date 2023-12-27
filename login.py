import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


def submit_action():
    input_text = input_var.get()
    file_path = file_var.get()
    print("Input:", input_text)
    print("File path:", file_path)


def on_radio_select():
    selected_option = radio_var.get()
    print("选中的选项是:", selected_option)


def on_combobox_select(event):
    selected_value = combo_var.get()
    print("选择的值是:", selected_value)


# 创建主窗口
root = tk.Tk()
root.title("居中显示界面")

# 获取屏幕尺寸以计算窗口居中的位置
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口居中
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# 创建输入框
input_var = tk.StringVar()
input_entry = tk.Entry(root, textvariable=input_var)
input_entry.pack(pady=10)

# 创建文件选择框和按钮
file_var = tk.StringVar()
file_label = tk.Label(root, text="文件路径:")
file_label.pack()
file_frame = tk.Frame(root)
file_frame.pack()
file_entry = tk.Entry(file_frame, textvariable=file_var)
file_entry.pack(side=tk.LEFT)
file_button = tk.Button(file_frame, text="选择文件", command=lambda: file_var.set(filedialog.askopenfilename()))
file_button.pack(side=tk.RIGHT)

# 创建单选按钮
radio_var = tk.StringVar()
radio_var.set("x")  # 设置默认选中的选项
x_radio = tk.Radiobutton(root, text="X", variable=radio_var, value="x", command=on_radio_select)
x_radio.pack()
y_radio = tk.Radiobutton(root, text="Y", variable=radio_var, value="y", command=on_radio_select)
y_radio.pack()

# 创建下拉选择框
combo_var = tk.StringVar()
combo_box = ttk.Combobox(root, textvariable=combo_var, values=["Option 1", "Option 2", "Option 3"])
combo_box.bind("<<ComboboxSelected>>", on_combobox_select)  # 绑定选择事件
combo_box.pack()

# 创建提交按钮
submit_button = tk.Button(root, text="提交", command=submit_action)
submit_button.pack(pady=10)

# 运行主循环
root.mainloop()

