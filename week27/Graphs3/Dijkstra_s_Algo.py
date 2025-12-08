'''
Problem Description

Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.

You have to find an integer array D of size A such that:

D[i]: Shortest distance from the C node to node i.
If node i is not reachable from C then -1.
Note:

There are no self-loops in the graph.
There are no multiple edges between two pairs of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.


'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        # percolate down for maintaining th emin heap 
        def percolate_down(curr):
            left = 2*curr + 1
            right = 2*curr + 2

            while curr < len(min_heap):
                swapped = False
                if left < len(min_heap) and right < len(min_heap):
                    if min_heap[left][1] < min_heap[curr][1] or min_heap[right][1] < min_heap[curr][1]:
                        if min_heap[left][1] < min_heap[right][1]:
                            min_heap[curr],min_heap[left] = min_heap[left],min_heap[curr]
                            swapped = True
                            curr = left
                        else:
                            min_heap[curr],min_heap[right] = min_heap[right],min_heap[curr]
                            swapped = True
                            curr = right
                        left = 2*curr + 1
                        right = 2*curr + 2
                elif left < len(min_heap):
                    if min_heap[left][1] < min_heap[curr][1]:
                        min_heap[curr],min_heap[left] = min_heap[left],min_heap[curr]
                        swapped = True 
                        curr = left
                        left = 2*curr + 1
                        right = 2*curr + 2
                if not swapped :
                    break
        
        # percolste up for adding a new node
        def percolate_up(node_index):
            parent = (node_index-1)//2
            while parent >= 0:
                if min_heap[parent][1] > min_heap[node_index][1]:
                    min_heap[parent], min_heap[node_index] = min_heap[node_index], min_heap[parent]
                    node_index = parent
                    parent = (node_index-1)//2
                else:
                    break
        
        # applying the Dijkstra's algorithm
        adj_list = {i:[] for i in range(A)}
        for i in range(len(B)):
            adj_list[B[i][0]].append((B[i][1],B[i][2]))
            adj_list[B[i][1]].append((B[i][0],B[i][2]))
        
        shortest_dist = [[float('inf'),0] for _ in range(A)] # shortest_path array [distance, visit_check]
        shortest_dist[C][0], shortest_dist[C][1] = 0, 1
        min_heap = []
        # just initialising the priority queue or min heap with the source's connected edges
        for i in adj_list[C]:
            min_heap.append((i[0],i[1]))
            percolate_up(len(min_heap)-1)
        
        while min_heap:
            # minimum weight edge deletion
            n = len(min_heap)
            node = min_heap[0]
            min_heap[0], min_heap[n-1] = min_heap[n-1], min_heap[0]
            del min_heap[n-1]
            percolate_down(0)

            # update the edge's shortest path array
            shortest_dist[node[0]][0] = min(shortest_dist[node[0]][0], node[1])  
            shortest_dist[node[0]][1] = 1 
            
            # neighbours edges of the deleted node addition
            if node[1] > shortest_dist[node[0]][0]:
                continue
            for i in adj_list[node[0]]:
                if shortest_dist[i[0]][1] == 1:
                    continue
                min_heap.append((i[0],i[1]+node[1])) # adding the new path (node,sum of previous path and the current edge)
                n = len(min_heap)
                percolate_up(n-1)
            

        for i in range(len(shortest_dist)):
            if shortest_dist[i][0] == float('inf'):
                shortest_dist[i][0] = -1
        
        ans = [shortest_dist[i][0] for i in range(A)]
        return ans

