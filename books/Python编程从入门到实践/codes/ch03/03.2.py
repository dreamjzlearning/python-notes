# 03.2.py
# 列表操作

# 修改元素
nums = [1,2,3]

nums[1] = 4
print(nums) # [1,4,3]

# 添加元素

# 添加至末尾
nums.append(4)
print(nums) # [1,4,3,4]
# 插入到指定位置
nums.insert(2, 5) # [1,4,5,3,4]

# 删除元素

# 使用 del 语句
del nums[1]
print(nums) # [1,5,3,4]
# 弹出末尾元素
n = nums.pop()
print(n) # 4
print(nums) # [1,5,3]
# 弹出指定位置
n = nums.pop(1) 
print(n) # 5
print(nums) # [1,3]
# 删除指定值
# remove 只会删除第一个
nums.remove(3)
print(nums) # [1]