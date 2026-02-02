'''
Docstring for minimum_weighted_cycle
Problem Description

Given an integer A, representing number of vertices in a graph.

Also you are given a matrix of integers B of size N x 3 where N represents number of Edges in a Graph and Triplet (B[i][0], B[i][1], B[i][2]) implies there is an undirected edge between B[i][0] and B[i][1] and weight of that edge is B[i][2].

Find and return the weight of minimum weighted cycle and if there is no cycle return -1 instead.

NOTE: Graph may contain self loops but does not have duplicate edges.

'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        '''
        for each edge:
            remove edge + run dijkstra
            find complete cycle weight = edgeweight + dijkstra's weight
            restore ans
            maintain minimum weight ans.
        '''

        # dijkstra
        
        #percolate up
        def percolate_up(curr,arr):
            while curr > 0:
                parent = (curr-1)//2
                if arr[parent][1] > arr[curr][1]:
                    arr[curr], arr[parent] = arr[parent], arr[curr]
                    curr = parent
                else:
                    break
        
        # percolate down
        def percolate_down(curr,arr):
            small = curr
            while True:
                left = 2*curr + 1
                right = 2*curr + 2
                if left < len(arr) and arr[left][1] < arr[small][1]:
                    small = left
                if right < len(arr) and arr[right][1] < arr[small][1]:
                    small = right
                if small != curr:
                    arr[small], arr[curr] = arr[curr], arr[small]
                    curr = small
                else:
                    break

        def dijkstra(s,d,adj_list):
            min_heap = []
            visited = [0] * (A+1)
            
            min_heap.append((s,0))
            
            while min_heap:
                node,weight = min_heap[0]
                min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
                del min_heap[-1]

                percolate_down(0,min_heap)
                
                if node == d:
                    return weight

                if visited[node]:
                    continue
                
                visited[node] = 1

                for child,child_weight in adj_list[node]:
                    if not visited[child]:
                        min_heap.append((child,weight + child_weight))
                        percolate_up(len(min_heap)-1,min_heap)

            return -1

        # actual algo

        adj_list = {i:[] for i in range(1,A+1)}
        minimum_weighted_cycle = float('inf')

        for i,j,k in B:
            adj_list[i].append((j,k))
            adj_list[j].append((i,k))

        for i,j,k in B:
            cloned_adj_list = {u:list(v) for u,v in adj_list.items()}
            cloned_adj_list[i] = [(x,y) for x,y in cloned_adj_list[i] if x != j ]
            cloned_adj_list[j] = [(x,y) for x,y in cloned_adj_list[i] if x != i ]

            shortest_path_weight = dijkstra(i,j,cloned_adj_list)
            if shortest_path_weight != -1:
                minimum_weighted_cycle = min(minimum_weighted_cycle, k + shortest_path_weight)
            
        return -1 if minimum_weighted_cycle == float('inf') else minimum_weighted_cycle
