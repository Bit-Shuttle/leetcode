from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 从先修->后修 构造有向图，然后判断这个有向图是否有环
        # inDict 记录节点的入度
        # map dic 记录每个课程的后修课程
        prelen = len(prerequisites)
        inDict = [0] * numCourses
        book = {}
        # 记一下处理的课程数量
        count = 0
        for i in range(prelen):
            pre ,tail = prerequisites[i][1],prerequisites[i][0]
            inDict[tail] = inDict[tail] + 1
            if book.get(pre) is not None:
                book.get(pre).append(tail)
            else:
                book[pre] = [tail]
        queue = deque()
        for i in range(numCourses):
            if inDict[i] == 0:
                queue.append(i)
        count = 0
        while len(queue)!= 0:
            courepre = queue.popleft()
            count += 1
            if book.get(courepre) is None:
                continue
            for item in book.get(courepre):
                if inDict[item] <= 0:
                    return False
                inDict[item] = inDict[item] - 1
                if inDict[item] == 0:
                    queue.append(item)
        return count == numCourses
    
    
numCourses = 2
prerequisites = [[1,0]]
sol = Solution()
print(sol.canFinish(numCourses,prerequisites))

