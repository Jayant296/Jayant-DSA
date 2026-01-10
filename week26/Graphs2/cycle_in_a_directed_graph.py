'''
Docstring for cycle_in_a_directed_graph
Problem Description

Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        
        '''
        using topological sort to detect cycles:
        if we are able to process exactly A nodes then we can say there
        are no cycles otherwise cycle exists.
        '''
        adj_list = dict()
        indegree = [0]*(A+1) # no of incoming edges on ith node

        for i,j in B:
            if i in adj_list:
                adj_list[i].append(j)
            else:
                adj_list[i] = [j]
            indegree[j] += 1
        
        queue = deque()
        for i in range(1,A+1):
            if indegree[i] == 0:
                queue.append(i)
        
        processed = 0
        while queue:

            node = queue.popleft()
            processed += 1

            if node in adj_list:
                for neighbour in adj_list[node]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)

        return 0 if processed == A else 1