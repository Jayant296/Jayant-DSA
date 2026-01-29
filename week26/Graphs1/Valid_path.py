'''
Problem Description

There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.

'''
from collections import deque
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @param E : list of integers
	# @param F : list of integers
	# @return a strings
	def solve(self, A, B, C, D, E, F):
        rectangle_matrix = [[1 for _ in range(B+1)] for _ in range(A+1)]
        
        # filling the circle points as -1 by using circle equation
        # (x-h)**2 + (y-k)**2 <= k**2, for points inside or on the circle
        for h,k in zip(E,F):
            for x in range(A+1):
                for y in range(B+1):
                    if ((x-h)**2 + (y-k)**2) <= D*D:
                        rectangle_matrix[x][y] = -1
        
        neighbours = [(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
        
        '''
        # dfs
        def dfs(i,j):
            if rectangle_matrix[i][j] == -1 or rectangle_matrix[i][j] == 0: # inside circle or already visited
                return False
            

            if i == A and j == B :
                return True

            rectangle_matrix[i][j] = 0 # marked visited

            for x,y in neighbours:
                m = i + x
                n = j + y
                if 0 <= m <= A and 0 <= n <= B and rectangle_matrix[m][n] == 1:
                    if dfs(m,n):
                        return True

            return False
        
        if rectangle_matrix[0][0] == -1 or rectangle_matrix[A][B] == -1:
            return "NO"

        return 'YES' if dfs(0,0) else 'NO'
        causing stack overflow issues
        '''

        if rectangle_matrix[0][0] == -1 or rectangle_matrix[A][B] == -1:
            return "NO"

        # using bfs
        queue = deque()
        queue.append((0,0))

        while queue:
            x,y = queue.popleft()
            
            if x == A and y == B:
                return 'YES'

            if rectangle_matrix[x][y] == 0:
                continue
            
            rectangle_matrix[x][y] = 0

            for i,j in neighbours:
                m = x + i
                n = y + j
                
                if 0 <= m <= A and 0 <= n <= B and rectangle_matrix[m][n] == 1:
                    queue.append((m,n))
        
        return 'NO'