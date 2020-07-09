from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # [num for i in range(n)] will create a list with 'n' number of 'num' .
        # This line generates a n x n matrix.
        matrix = [[0 for i in range(n)] for i in range(n)]
        u, d, l, r = 0, n-1, 0, n-1
        m = 1
        while m <= n**2:
            # Left to right. (->)
            for i in range(l, r+1):
                matrix[u][i] = m
                m += 1
            u += 1 # Update up limit.

            # Up to down. (⬇)
            for i in range(u, d+1):
                matrix[i][r] = m
                m += 1
            r -= 1 # Update right limit.

            # Right to left. (<-)
            for i in range(r, l-1, -1):
                matrix[d][i] = m
                m += 1
            d -= 1 # Update down limit.

            # Down to up. (⬆)
            for i in range(d, u-1, -1):
                matrix[i][l] = m
                m += 1
            l += 1
        
        return matrix