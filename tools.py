import os
import ast


def parse_python_file(file_path, file_name):
    # 解析单个 Python 文件
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            source_code = file.read()
            tree = ast.parse(source_code)

            # 遍历解析树，查找函数和方法定义
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    function_name = node.name
                    print(f"{file_name}:", function_name)
    except UnicodeEncodeError as e:
        print(f"Error decoding file: {file_path}")


# 文件夹路径
folder_path = "./my_mitmproxy"

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(".py"):  # 仅处理以 .py 结尾的文件
            file_path = os.path.join(root, file_name)
            parse_python_file(file_path, file_name)