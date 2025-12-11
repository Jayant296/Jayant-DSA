'''
Problem Description

Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge from i to j (i ---> j).

If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.

Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.

If there is no possible path from vertex i to vertex j , B[i][j] = -1

Note: Rows are numbered from top to bottom and columns are numbered from left to right.
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        B = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    continue
                elif A[i][j] == -1:
                    B[i][j] = float('inf')
                else:
                    B[i][j] = A[i][j]
        
        for k in range(len(A)):
            for i in range(len(A)):
                for j in range(len(A)):
                    if i == j:
                        continue
                    B[i][j] = min(B[i][j],B[i][k] + B[k][j])
        
        for i in range(len(A)):
            for j in range(len(A)):
                if B[i][j] == float('inf'):
                    B[i][j] = -1

        return B
