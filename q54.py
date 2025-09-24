from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        count = m * n
        zeros = [0] * n
        book = [[0] * n for _ in range(m)]
        i, j = 0, 0
        ans = []
        while count >  0:
            while count > 0 and j < n and book[i][j] == 0:
                count -= 1
                ans.append(matrix[i][j])
                book[i][j] = 1
                j += 1
            j = j - 1
            i += 1
            while count > 0 and i < m and book[i][j] == 0:
                count -= 1
                ans.append(matrix[i][j])
                book[i][j] = 1
                i += 1
            i = i - 1
            j = j - 1
            while count > 0 and j >= 0 and book[i][j] == 0:
                count -= 1
                ans.append(matrix[i][j])
                book[i][j] = 1
                j -= 1
            j = j + 1
            i = i - 1
            while count > 0 and i >= 0 and book[i][j] == 0:
                count -= 1
                ans.append(matrix[i][j])
                book[i][j] = 1
                i -= 1
            i = i + 1
            j = j + 1
        return ans
ques = [[1,2,3],[4,5,6],[7,8,9]]
sol  = Solution()
print(sol.spiralOrder(ques))