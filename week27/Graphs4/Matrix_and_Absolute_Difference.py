'''
Docstring for Matrix_and_Absolute_Difference
Problem Description

Given a matrix C of integers, of dimension A x B.

For any given K, you are not allowed to travel between cells that have an absolute difference greater than K.

Return the minimum value of K such that it is possible to travel between any pair of cells in the grid through a path of adjacent cells.

NOTE:

Adjacent cells are those cells that share a side with the current cell.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        '''
        Solution:
        first make the mst to connect all edges,
        then find the maximum weighted edge of that mst and return it as 
        answer.
        '''
        # using prim's algo
        adj_list = {}
        for i in range(A):
            for j in range(B):
                adj_list[(i,j)] = []
        neighbours = [(0,-1),(0,1),(1,0),(-1,0)]
        
        # making adjacency list
        for i in range(A):
            for j in range(B):
                for k in neighbours:
                    x = i + k[0]
                    y = j + k[1]
                    if 0 <= x <= A-1 and 0 <= y <= B-1:
                        adj_list[(i,j)].append([(x,y),abs(C[i][j]-C[x][y])])

        def percolate_down(curr,arr):
            left = 2*curr + 1
            right = 2*curr + 2
            small = curr

            while True:
                if left < len(arr) and arr[left][1] < arr[small][1]:
                    small = left
                if right < len(arr) and arr[right][1] < arr[small][1]:
                    small = right
                if small != curr:
                    arr[small], arr[curr] = arr[curr], arr[small]
                    curr = small
                    left = 2*curr + 1
                    right = 2*curr + 2
                else:
                    break
            
        def percolate_up(curr, arr):
            parent = (curr-1)//2

            while parent >= 0:
                if arr[curr][1] < arr[parent][1]:
                    arr[curr], arr[parent] = arr[parent], arr[curr]
                    curr = parent
                    parent = (curr-1)//2
                else:
                    break
                    
        min_k = float('inf')
    
        min_heap = []
        visited = [[0 for _ in range(B)] for _ in range(A)]
        min_heap.append(((0,0),0))
        edges = []
        while min_heap:
            node = min_heap[0]
            min_heap[0], min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1], min_heap[0]
            del min_heap[len(min_heap)-1]
            percolate_down(0,min_heap)
            
            if visited[node[0][0]][node[0][1]]:
                continue
            visited[node[0][0]][node[0][1]] = 1
            edges.append(node[1])
            
            for j in adj_list[node[0]]:
                if not visited[j[0][0]][j[0][1]] :
                    min_heap.append(j)
                    percolate_up(len(min_heap)-1,min_heap)

        return max(edges)