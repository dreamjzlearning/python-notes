# 05.1.py
# if

a = 1
b = 2

if a < b:
    print("a < b")

# and
print(1 < 2 and 2 < 3) # True

# or 
print(1 > 2 or 2 < 3) # True

# 判断值是否在列表中
# in
nums = list(range(1,5))
print(1 in nums) # True
print(100 in nums) # False

# not in
print(100 not in nums) # True


# if-elif-else 结构
a = 14
if a < 4:
    p = 0
elif a < 18:
    p = 5
elif a < 60:
    p = 10
else:
    p = 12