'''
Docstring for distance_of_nearest_cell
Problem Description

Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.

'''
from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        '''
        ones = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    ones.append((i,j))
        
        ans = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                val = float("inf")
                for x,y in ones:
                    val = min(val,abs(i-x) + abs(j-y))
                ans[i][j] = val

        return ans
        
        WORKS, BUT ITS BRUTEFORCE WHICH TAKES O(N*M*k)
        '''

        # this can be done through the concept of multi-source bfs
        # that means we start our bfs from more than 1 similar points.
        
        queue = deque()
        ans = [[float('inf') for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    queue.append(((i,j),0)) # appending (co-ordinates,distance)
                    ans[i][j] = 0
        
        neighbors = [(0,-1),(0,1),(-1,0),(1,0)]
        while queue:
            coordinates, dist = queue.popleft()
            x,y = coordinates

            for dx,dy in neighbors:
                m = x + dx
                n = y + dy
                if 0 <= m < len(A) and 0 <= n < len(A[0]) and A[m][n] == 0:
                    A[m][n] = 1
                    ans[m][n] = min(ans[m][n],dist+1)
                    queue.append(((m,n),ans[m][n]))
        
        return ans
