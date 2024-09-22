# 04.4.py
# 切片

nums = [1,2,3,4,5]
print(nums[0:3]) # [1,2,3]
print(nums[:3])  # [1,2,3]
print(nums[1:]) # [2,3,4,5]

# 可以反向
# 最后三个元素
print(nums[-3:]) 

# 遍历切片
for val in nums[2:4]:
    print(val)
    
# 复制列表

# 直接赋值，两个变量指向同一个列表
nums1 = nums
print(nums1) 
nums[0] = 10 # 将影响 nums1
print(nums)
print(nums1)

# 生成切片时，会创建一份副本
nums = [1,2,3,4,5]
nums2 = nums[:]
print(nums2) 
nums[0] = 10 # 不会影响
print(nums)
print(nums2)
