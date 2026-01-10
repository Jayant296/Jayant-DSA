'''
Docstring for construct_roads
Problem Description

A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

NOTE: All cities can be visited from any city.
'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        '''
        using bfs level by level logic for bipartite coloring :
        putting the cities in red and green boxes such that any two cities
        are in different sets.
        '''
        red = set()
        green = set()
        adj_list = {i:[] for i in range(A+1)}

        for i,j in B:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        queue = deque()
        queue.append((1,'r'))
        visited = [0 for _ in range(A+1)]

        while queue:

            node = queue.popleft()

            if visited[node[0]]:
                continue
            visited[node[0]] = 1
            if node[1] == 'r':
                red.add(node[0])
            else:
                green.add(node[0])
            child_color = 'r' if node[1] == 'g' else 'g'

            for child in adj_list[node[0]]:
                if visited[child]:
                    continue
                queue.append((child,child_color))

        roads = (len(red)*len(green) - (A-1)) % (10**9 + 7)
        return roads 