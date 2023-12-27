from deepdiff import DeepDiff
from jinja2 import Template

# 假设有两个对象 obj1 和 obj2，进行比较
obj1 = {"name": "John", "age": 30, "city": "New York"}
obj2 = {"name": "John", "age": 25, "city": "Chicago"}

# 比较两个对象的差异
diff = DeepDiff(obj1, obj2)

# 将差异结果转换为HTML格式
template = Template("""
<html>
<head>
<title>DeepDiff Comparison Result</title>
<style>
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    text-align: left;
    padding: 8px;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
}
</style>
</head>
<body>
<h1>DeepDiff Comparison Result</h1>
<table>
    <tr>
        <th>Category</th>
        <th>Difference</th>
    </tr>
    {% for category, difference in diff.items() %}
    <tr>
        <td>{{ category }}</td>
        <td>{{ difference }}</td>
    </tr>
    {% endfor %}
</table>
</body>
</html>
""")

html_output = template.render(diff=diff)

# 将HTML输出保存到文件或进行其他操作
with open("diff_result.html", "w") as f:
    f.write(html_output)



















