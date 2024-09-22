# 06.2.py
# 遍历字典

m = {"A": 1, "B": 2, "C": 3}

# 遍历键值对
# item 为元组
for item in m.items():
    print(item)

# 赋值给两个变量
for k, v in m.items():
    print("K: " + k + ", V: " + str(v))

# 遍历所有的 key
for k in m.keys():
    print(k)

# 默认遍历 key
for k in m:
    print(k)

# 遍历所有的 value
for v in m.values():
    print(v)

# 使用集合去重
m["D"] = 1
for v in set(m.values()):
    print(v)
