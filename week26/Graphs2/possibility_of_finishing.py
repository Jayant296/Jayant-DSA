'''
Docstring for possibility_of_finishing
Problem Description

There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.

'''
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
        # its the cycle detection concept
        # using dfs
        adj_list = {i:[] for i in range(1,A+1)}
        for i,j in zip(B,C):
            adj_list[i].append(j)

        visited = [0 for _ in range(A+1)]
        def dfs(node,rec_stack):
            if rec_stack[node]: # cycle detected
                return True

            if visited[node]:
                return False
            
            visited[node] = 1
            rec_stack[node] = 1
            
            for i in adj_list[node]:
                if visited[i] and not rec_stack[i]:
                    continue

                if dfs(i,rec_stack): # only check that whether we a node is in recursion_stack or not, no need to check for visited as cycle can exist in the visited nodes as well
                    return True
                    
            rec_stack[node] = 0 # releasing the node

            return False # No Cycle detected
        
        rec_stack = [0] * (A+1)
        for i in range(1,A+1):
            if not visited[i]:
                if dfs(i,rec_stack):
                    return 0
        
        return 1
