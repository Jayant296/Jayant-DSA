'''
Docstring for capture_regions_on_board
Problem Description

Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

'''
from collections import deque

class Solution:
    # @param A : list of strings
    # @return list of strings
    def solve(self, A):

        # convert A to mutable grid
        A[:] = [list(row) for row in A] #A[:] makes changes in the same list of same address

        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        R, C = len(A), len(A[0])

        # 1) push all boundary 'O'
        for i in range(R):
            for j in range(C):
                if i == 0 or i == R-1 or j == 0 or j == C-1:
                    if A[i][j] == 'O':
                        A[i][j] = 'B'
                        queue.append((i, j))

        # 2) BFS to mark safe regions
        while queue:
            x, y = queue.popleft()

            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and A[nx][ny] == 'O':
                    A[nx][ny] = 'B'
                    queue.append((nx, ny))

        # 3) final conversion
        for i in range(R):
            for j in range(C):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == 'B':
                    A[i][j] = 'O'

        # convert back to list of strings
        for i in range(R):
            A[i] = ''.join(A[i])
