from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # BFS
        queue = deque()
        visited = [0 for _ in range(A)]
   
        # making adjacency list
        adj_list = {i:[] for i in range(1,A+1)}
        for i in range(len(B)):
            adj_list[B[i][0]].append(B[i][1])

        queue.append(1)
        while queue:
            node = queue.popleft()
            if node == A:
                return 1
            visited[node-1] = 1
            
            for i in range(len(adj_list[node])):
                if visited[adj_list[node][i]-1] != 1:
                    visited[adj_list[node][i]-1] = 1
                    queue.append(adj_list[node][i])
        
        return 1 if visited[A-1] == 1 else 0