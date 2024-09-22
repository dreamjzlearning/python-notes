# 10.1.py
# 读取文件

import os

# 获取源文件绝对路径
source_file_path = os.path.realpath(__file__)
# 获取文件夹路径
dir_path = os.path.dirname(source_file_path)
fp = os.path.join(dir_path, "text.txt")

# with 将在文件使用完毕后自动关闭
with open(fp) as file_object:
    contents = file_object.read()  # read 读取全部内容
    print(contents)

# 逐行读取
with open(fp) as fo:
    for line in fo:
        print(line.rstrip())

# 读取到列表中
with open(fp) as fo:
    lines = fo.readlines()

print(lines)
