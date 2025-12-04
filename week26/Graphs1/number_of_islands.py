'''
Problem Description

Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.


'''
from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        # using bfs
        islands = 0
        neighbours = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        # BFS
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    queue = deque()
                    queue.append((i,j))
                    
                    while queue:
                        node = queue.popleft()
                        A[node[0]][node[1]] = 0 # marking as visited

                        for k in range(len(neighbours)):
                            x = node[0] + neighbours[k][0]
                            y = node[1] + neighbours[k][1]
                            if 0 <= x < len(A) and 0 <= y < len(A[0]) :
                                if A[x][y] == 1 :
                                    A[x][y] = 0
                                    queue.append((x,y))
                    
                    islands += 1
                                          
        return islands                                                
       
        '''
        # DFS :-> giving recursion depth error 
        def dfs(x,y):
            if A[x][y] == 0:
                return
            A[x][y] =  0
            for k in neighbours:
                m = x + k[0]
                n = y + k[1]
                if 0 <= m < len(A) and 0 <= n < len(A[0]):
                    dfs(m,n)

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    dfs(i,j)
                    islands += 1
        
        return islands
        '''