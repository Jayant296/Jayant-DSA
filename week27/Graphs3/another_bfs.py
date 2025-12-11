'''
Problem Description

Given a weighted undirected graph having A nodes, a source node C and destination node D.

Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.

You are expected to do it in Time Complexity of O(A + M).

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
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        adj_list = {i:[] for i in range(A)}
        new_node = A
        visited = [[0,float('inf')] for _ in range(A)]
        for i in range(len(B)):
            if B[i][2] == 2:
                adj_list[new_node] = []
                visited.append([0,float('inf')])
                adj_list[B[i][0]].append((new_node,1))
                adj_list[new_node].append((B[i][0],1))
                adj_list[new_node].append((B[i][1],1))
                adj_list[B[i][1]].append((new_node,1))
                new_node += 1
            
            else:
                adj_list[B[i][0]].append((B[i][1],1))
                adj_list[B[i][1]].append((B[i][0],1))

        queue = deque()
        queue.append((C,0))

        while queue:
            node = queue.popleft()
            visited[node[0]][1] = node[1]

            if node[0] == D:
                return node[1]
            for i in adj_list[node[0]]:
                if visited[i[0]][0] == 1:
                    continue
                queue.append((i[0],node[1]+i[1]))
                visited[i[0]][0] = 1

        return -1

