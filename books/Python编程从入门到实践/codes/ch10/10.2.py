# 10.2.py
# 写入文件

from os import path

filename = "write_test.txt"
filepath = path.join(path.dirname(path.realpath(__file__)), filename)

# 写入模式打开文件
with open(filepath, "w") as file_object:
    file_object.write("Hello World!\n")

# 追加模式
with open(filepath, "a") as file_object:
    file_object.write("new content\n")
