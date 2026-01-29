'''
Docstring for black_shapes
Problem Description

Given character matrix A of dimensions N×M consisting of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

'''
from collections import deque
class Solution:
	# @param A : list of strings
	# @return an integer
	def black(self, A):
        # question of connected components 
        # applying bfs
        
        new_A = [list(i) for i in A]
        shapes_count = 0
        neighbors = [(0,-1),(0,1),(-1,0),(1,0)]

        for i in range(len(new_A)):
            for j in range(len(new_A[0])):

                if new_A[i][j] == 'O':
                    continue

                queue = deque()
                queue.append((i,j))
                new_A[i][j] = 'O'

                while queue:
                    x,y = queue.popleft()

                    for h,k in neighbors:
                        m = h + x
                        n = k + y

                        if 0 <= m < len(new_A) and 0 <= n < len(new_A[0]) and new_A[m][n] == 'X':
                            queue.append((m,n))
                            new_A[m][n] = 'O'
                
                shapes_count += 1

        return shapes_count