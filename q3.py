
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # 左指针找到第一个小于当前位置的index
        # 右指针开始往右走，记录移动时候中间的柱体体积
        # 右指针 往右找到第一个大于等于左边界的
        # 如果right = n，也就是left右边没有高的了，那就需要反过来，从右边开始往左寻找
        # 面积 min(height(left),height(right)) * (right - left) - area
        # left = right 继续循环
        n = len(height)
        left ,right = 0,0
        ans = 0
        while left < n and right < n:
            if height[left] == 0:
                left = left + 1
                continue
            # 左边最高峰
            while left + 1 < n and height[left + 1] >= height[left]:
                left = left + 1
            right = left + 1
            if right == n:
                break
            area = 0
            # 找到大于左边的山峰
            while right < n and height[right] < height[left]:
                area = area + height[right]
                right = right + 1
            if right < n:
                ans = ans + min(height[left],height[right]) * (right - left -1) - area
                left = right
            elif right == n:
                # 需要反向计算
                stop = left 
                ri_begin,le_begin = n - 1,n - 1
                while ri_begin > stop and le_begin > stop:
                    if height[ri_begin] == 0:
                        ri_begin = ri_begin - 1
                        continue
                    # 右数最高峰
                    while ri_begin - 1 > stop and height[ri_begin - 1] >= height[ri_begin]:
                        ri_begin = ri_begin - 1
                    le_begin = ri_begin - 1
                    area = 0
                    while le_begin > stop and height[le_begin] < height[ri_begin]:
                        area =area + height[le_begin]
                        le_begin = le_begin - 1
                    if le_begin > stop:
                        ans = ans + min(height[le_begin],height[ri_begin]) * (ri_begin - le_begin -1) - area
                        ri_begin = le_begin
                    if le_begin == stop:
                        ans = ans + min(height[le_begin],height[ri_begin]) * (ri_begin - le_begin -1) - area
                        return ans
        return ans
        
qus = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(qus))