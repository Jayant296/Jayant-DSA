'''
Docstring for largest_distance_between_any_nodes
Problem Description

Find largest distance Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes.

The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.

'''
from collections import deque
class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        if len(A) <= 1:
            return 0
        if len(A) == 2:
            return 1
        '''
        depths = []
        adj_list = {i:[] for i in range(len(A))}
        root = -1
        for i in range(len(A)):
            if A[i] == -1:
                root = i
                continue
            adj_list[A[i]].append(i)
        
        # now dfs the root 
        def max_depth(node):
            depth = 0
            for i in adj_list[node]:
                depth = max(depth, 1 + max_depth(i))
            return depth
        
        for i in adj_list[root]:
            depths.append(1 + max_depth(i))
              
        depths.sort()
        if len(depths) == 1:
            return depths[0]
        return depths[-1] + depths[-2] 

        not passing all the test cases 
        now applying the standard bfs style diameter technique
        [STANDARD APPROACH]
        the idea is that first pick any node and find the farthest node(x) from it ,
        then pick that node(x) and find the farthest node(y) form it , and that will
        be the ans (from x to y).
        '''
        queue = deque()
        visited = [0 for _ in range(len(A))]
        adj_list = {i:[] for i in range(len(A))}
        for i in range(len(A)):
            if A[i] == -1:
                continue
            adj_list[A[i]].append(i)
            adj_list[i].append(A[i])

        # finding the farthest node(x) from node 0
        queue.append((0,0)) # (node,distance)
        farthest_node = (0,float('-inf'))
        visited[0] = 1
        while queue:
            node = queue.popleft()
            if node[1] > farthest_node[1]:
                farthest_node = (node[0],node[1])
            for i in adj_list[node[0]]:
                if visited[i]:
                    continue
                queue.append((i,node[1]+1)) 
                visited[i] = 1
        x = farthest_node[:]

        # finding farthest node(y) from x
        farthest_node = (0,float('-inf'))
        queue = deque()
        visited = [0 for _ in range(len(A))]
        queue.append((x[0],0))
        visited[x[0]] = 1
        while queue:
            node = queue.popleft()
            if node[1] > farthest_node[1]:
                farthest_node = (node[0], node[1])
            for i in adj_list[node[0]]:
                if visited[i]:
                    continue
                queue.append((i,node[1]+1)) 
                visited[i] = 1
        y = farthest_node[:]

        return y[1]
