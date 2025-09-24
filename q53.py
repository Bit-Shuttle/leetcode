from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans,tmp = - 100000,0
        for i in range(n):
            num = nums[i]
            if num >= 0:
                tmp += num
                ans = max(ans,tmp)
            else:
                if num >= ans :
                    ans = num
                else:
                    sumt = tmp + num
                    if sumt <= 0:
                        tmp = 0
                    else:
                        tmp += num
        return ans
    
ques = [-2,1,-3,4,-1,2,1,-5,4]
sol  = Solution()
print(sol.maxSubArray(ques))