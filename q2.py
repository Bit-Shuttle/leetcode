from typing import List
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         #method1 排序 nlog(n) 遍历 n 二分log(n) 
#         #method2 三指针 n**3 
#         res = []
#         nums = sorted(nums)
#         n = len(nums)
#         left = 0
#         right = n - 1
#         if nums[left] > 0 or nums[right] < 0:
#             return res
#         # 添加标记
#         book = {}
#         for i in range(n):
#             book[nums[i]] = 1
#         while nums[left] < 0:
#             # 左边小于0
#             right = n - 1
#             while nums[right] > 0:
#                 target = 0 - (nums[left] + nums[right])
#                 begin = left + 1
#                 end = right - 1
#                 if target > nums[end]:
#                     break
#                 if target >= nums[begin] and book.get(target) is not None :
#                     tmp_arr = [nums[left],target,nums[right]]
#                     res.append(tmp_arr)
#                 # right 找到左边第一个和它不同的
#                 while nums[right -  1] == nums[right]:
#                     right = right - 1
#                 right = right - 1
#             # left找到右边第一个和它不同的
#             while nums[left + 1] == nums[left]:
#                 left = left + 1
#             left = left + 1
#         # 判断左边是否等于零
#         if nums[left] == 0:
#             if left + 2 < n and nums[left + 2] == 0:
#                 tmp_arr = [0,0,0]
#                 res.append(tmp_arr)
#         return res
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复i
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # 跳过重复left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # 跳过重复right
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res
    
ans = [-100,-70,-60,110,120,130,160]
sol = Solution()
print(sol.threeSum(ans))
        
# -4 -1 -1 0 1 2