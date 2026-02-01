'''
Docstring for poisonous_graph
Problem Description

You are given an undirected unweighted graph consisting of A vertices and M edges given in a form of 2D Matrix B of size M x 2 where (B[i][0], B][i][1]) denotes two nodes connected by an edge.

You have to write a number on each vertex of the graph. Each number should be 1, 2 or 3. The graph becomes Poisonous if for each edge the sum of numbers on vertices connected by this edge is odd.

Calculate the number of possible ways to write numbers 1, 2 or 3 on vertices so the graph becomes poisonous. Since this number may be large, return it modulo 998244353.

NOTE:

Note that you have to write exactly one number on each vertex.
The graph does not have any self-loops or multiple edges.
Nodes are labelled from 1 to A.
'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # checking whether the graph is bipartite or not
        adj_list = {i : [] for i in range(1,A+1)}
        for i,j in B:
            adj_list[i].append(j)
            adj_list[j].append(i)

        
        visited = [0 for _ in range(A+1)]
        color = [None for _ in range(A+1)]
        connected_components = dict()
        count = 1

        for j in range(1,A+1):

            if visited[j]:
                continue

            queue = deque()
            queue.append(j)
            countc1 = 0
            countc2 = 0
            color[j] = 'c1'
            countc1 += 1

            while queue:
                node = queue.popleft()
                if visited[node]:
                    continue

                visited[node] = 1

                for i in adj_list[node]:
                    if color[i] and color[i] == color[node]:
                        return 0
                    if not color[i]:
                        if color[node] == 'c1':
                            color[i] = 'c2'
                            countc2 += 1
                        else:
                            color[i] = 'c1'
                            countc1 += 1
                        queue.append(i)

            connected_components[count] = (countc1,countc2)
            count += 1
            
        ways = 1
        mod = 998244353
        
        for i in connected_components.values():
            ways = (ways * (pow(2,i[0],mod) + pow(2,i[1],mod))) % 998244353

        return ways % 998244353