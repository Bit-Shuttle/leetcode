#给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count,slen = len(p),len(s)
        left ,right = 0,0
        book = {}
        res = []
        for i in range(slen):
            if book.get(s[i]) is None:
                book[s[i]] = 1
            else:
                book[s[i]] = book[s[i]] + 1
        while right < slen:
            # count == 0 


            if book.get(s[right]) is None:
                # 左指针直接跑到下一个字符
                while left < right:
                    count += 1
                    book[s[left]] = book[s[left]] + 1
                # left == right
                left = right + 1
                right = left
            elif book[s[right]] == 0:
                while s[left] != s[right]:
                    book[s[left]] = book[s[left]] + 1
                    count += 1
                # s[left] == s[right]
                book[s[left]] = book[s[left]] + 1
                count += 1
                left += 1
            elif book[s[right]] > 0:
                count -= 1
                book[s[right]] = book[s[right]] - 1
            # count == 0 找到了f'w 
            res.append(left)
            right += 1
        



        


        