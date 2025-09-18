# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        n = len(s)
        res = 0
        left ,right = 0,0
        while right < n:
            if dic.get(s[right]) is None or dic.get(s[right]) == 0:
                dic[s[right]] = 1
                right += 1
                continue
            res = max(res, right - left)
            while s[left] != s[right]:
                dic[s[left]] = 0
                left += 1    
            dic[s[left]] = 0
            left += 1
        res = max(res,right - left)
        return res

st = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(st))

            