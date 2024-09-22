# 08.1.py
# 函数


# 关键字实参
# 传递参数时将名称和值进行关联
def f(a, b):
    print("A: " + str(a) + ", B: " + str(b))


f(a=1, b=2)
# 此时参数顺序无关紧要
f(b=2, a=1)


# 形参默认值
def f1(a, b=2):
    print("A: " + str(a) + ", B: " + str(b))


f1(3)  # A: 3, B: 2


# 列表作为参数
def f2(nums):
    for i in range(len(nums)):
        nums[i] *= 2


nums = list(range(1, 5))
f2(nums)
print(nums)  # 函数对列表的修改是永久的

# 传递切片
nums = list(range(1, 5))
f2(nums[:])
print(nums)  # 此时修改的是副本


# 变长参数


# 所有参数都将放入名为 nums 的元组中
def f3(*nums):
    print(nums)


f3(1, 2, 3, 4)


# 参数放入 m 的字典中
def f4(a, b, **m):
    print(a)
    print(b)
    print(m)


# 1
# 2
# {'A': 1, 'B': 2, 'C': 3}
f4(1, 2, A=1, B=2, C=3)
