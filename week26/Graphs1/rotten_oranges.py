'''
Docstring for rotten_oranges
Problem Description

Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them
'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        time_taken = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
                              
        queue1 = deque()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 2:
                    queue1.append((i,j))
        
        if not queue1:
            return -1
        
        while True:
            neighbours = set()
            while queue1:
                orange = queue1.popleft()

                for i,j in directions:
                    m = i + orange[0]
                    n = j + orange[1]
                    if 0 <= m < len(A) and 0 <= n < len(A[0]) and A[m][n] == 1:
                        neighbours.add((m,n))
                        A[m][n] = 2

            if not neighbours:
                break
            time_taken += 1
            for i in neighbours:
                queue1.append(i)
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    return -1
        else:
            return time_taken
            