'''
Docstring for edge_in_mst
Problem Description

Given a undirected weighted graph with A nodes labelled from 1 to A with M edges given in a form of 2D-matrix B of size M * 3 where B[i][0] and B[i][1] denotes the two nodes connected by an edge of weight B[i][2].

For each edge check whether it belongs to any of the possible minimum spanning tree or not , return 1 if it belongs else return 0.

Return an one-dimensional binary array of size M denoting answer for each edge.

NOTE:

The graph may be disconnected in that case consider mst for each component.
No self-loops and no multiple edges present.
Answers in output array must be in order with the input array B output[i] must denote the answer of edge B[i][0] to B[i][1].
'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        # percoalte down
        def percolate_down(arr,curr,end):
            left = 2*curr + 1
            right = 2*curr + 2
            while True:
                largest = curr
                if left <= end and arr[left][2] > arr[largest][2]:
                    largest = left
                if right <= end and arr[right][2] > arr[largest][2]:
                    largest = right
                if largest != curr:
                    arr[largest], arr[curr] = arr[curr], arr[largest]
                    curr = largest
                    left = 2*curr + 1
                    right = 2*curr + 2
                else:
                    break
            
        # heap sorting
        def heap_sort(arr):
            start = 0
            end = len(arr)-1
            while end > start:
                arr[start], arr[end] = arr[end], arr[start]
                end -= 1
                percolate_down(arr,0,end)


        # finding parent by path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # union by height or rank
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a] += 1
            
            return True
        
        # sorting the edges
        edges = [(edge[0],edge[1],edge[2],i) for i,edge in enumerate(B)] # for saving the actual order of edges

        for i in range((len(edges)-1)//2,-1,-1): # creating max-heeap
            percolate_down(edges,i,len(edges)-1)

        heap_sort(edges) # actual sorting

        parent = [i for i in range(A+1)]
        rank = [0] * (A+1)
        ans = [0 for _ in range(len(edges))]

        # modified kruskal loop
        
        while i < len(edges):
            
            j = i

            while j < len(edges) and edges[i][2] == edges[j][2]:
                j += 1
            
            # now we iterate in similar weighted edges
            for k in range(i,j):
                u, v, w, idx = edges[k]
                
                # key concept of whole algo:
                # if we take this edge first amongst all same weighted edges then will it be the part of the mst or not.

                if find(u) != find(v):
                    ans[idx] = 1

            # now we do actual union as kruskal as kruskal
            for k in range(i,j):
                u, v, w, idx = edges[k]
                union(u,v)
            
            # extend the i to the actual unprocessed edges.
            i = j
 
        return ans
