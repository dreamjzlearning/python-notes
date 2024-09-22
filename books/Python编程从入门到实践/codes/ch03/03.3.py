# 03.3.py
# 排序

# sort()

nums = [1,5,6,2]
nums.sort() # 改变了原列表
print(nums)

# sorted()

nums = [1,5,6,2]
print(sorted(nums)) # 不影响原列表
print(nums)

# 反转列表
nums = [1,5,6,2]
nums.reverse()
print(nums) # [2,6,5,1]

# 获取长度
n = len(nums) # 4