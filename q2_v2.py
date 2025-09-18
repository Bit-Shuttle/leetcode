from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #method1 排序 nlog(n) 遍历 n 二分log(n) 
        #method2 三指针 n**3 
        # 排序 字典 
        nums = sorted(nums)
        n = len(nums)
        dict = {}
        for i in range(n):
            tmp_arr = [i]
            dict.setdefault(nums[i],tmp_arr).append(i)
        
        

        left = 0
        right = n - 1
        
        
        
ans = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(ans))
        
