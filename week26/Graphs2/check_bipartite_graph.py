'''
Docstring for check_bipartite_graph
Problem Description

Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.

A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        visited = [[0,''] for _ in range(A)] # using the combination of visit and color.
        queue = deque()
        adj_list = {i:[] for i in range(A)}

        for i in range(len(B)):
            adj_list[B[i][0]].append(B[i][1])
            adj_list[B[i][1]].append(B[i][0])

        for i in range(A):
            if visited[i] == 1:
                continue
            queue.append(i)

            while queue:

                node = queue.popleft()
                visited[node][0] = 1
                
                if visited[node][1] == '':
                    visited[node][1] = 'color1'

                for j in adj_list[node]:

                    if visited[node][1] == visited[j][1]: #parent and child color overlap
                        return 0
                    
                    elif visited[j][1] == '':
                        if visited[node][1] == 'color1': # if parent's color is color1
                            visited[j][1] = 'color2'
                        else:                           # if parent's color is color2
                            visited[j][1] = 'color1'
                        queue.append(j)

                    else:                           # already visited
                        continue
            
        return 1