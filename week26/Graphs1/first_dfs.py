'''
Problem Description

You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.

Given 2 towns find whether you can reach the first town from the second without repeating any edge.

B C : query to find whether B is reachable from C.

Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).

There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.

NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.
'''
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def solve(self, A, B, C):
        adj_list = {i : [] for i in range(1,len(A)+1)}
        for i in range(1,len(A)):
            adj_list[A[i]].append(i+1)

        # using Dfs
        def dfs(node):
            if node == B:
                return 1

            for neighbour in adj_list[node]:
                if dfs(neighbour) == 1:
                    return 1
            
            return 0
        
        result = dfs(C)
        return 0 if not result else 1



