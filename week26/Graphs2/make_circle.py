'''
Docstring for make_circle
Problem Description

Given an array of strings A of size N, find if the given strings can be chained to form a circle.

A string X can be put before another string Y in circle if the last character of X is same as first character of Y.

NOTE: All strings consist of lower case characters.
'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        # To do this question we'll check for 2 conditions:
        # 1.) every character (1st and last of the following strings) should have same indegree and outdegree
        
        indegree = dict()
        outdegree = dict()
        
        for i in A:
            if i[0] not in indegree:
                indegree[i[0]] = 0
                outdegree[i[0]] = 1
            else:
                outdegree[i[0]] += 1
            if i[-1] not in indegree:
                indegree[i[-1]] = 1
                outdegree[i[-1]] = 0
            else:
                indegree[i[-1]] += 1
            
        for i in indegree:
            if indegree[i] != outdegree[i]:
                return 0
        
        # 2.) checking whether the graph is strongly connected or not
        # using dfs
        # if all characters can be visited after 1 iteration then we return true else false.

        visited = dict()
        for ch in indegree:
            visited[ch] = 0

        adj_list = dict()
        for i in A:
            if i[0] not in adj_list:
                adj_list[i[0]] = [i[-1]] # means we can go from i[0] to i[-1]
            else:
                adj_list[i[0]].append(i[-1])
            if i[-1] not in adj_list:
                adj_list[i[-1]] = []
        
        def dfs(ch):
            if visited[ch] == 1:
                return
            visited[ch] = 1

            for i in adj_list[ch]:
                if visited[i] == 0:
                    dfs(i)
            
            for ch in visited:
                if visited[ch] == 0:
                    return 0

            return 1
        
        return dfs(A[0][0])