'''
Docstring for commutable_islands
Problem Description

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.


'''
class Solution:
	# @param A : integer
	# @param B : list of list of integers
	# @return an integer
	def solve(self, A, B):
        # applying the kruskal algo 
        def quick_sort(st, end):
            if st >= end:
                return 
            pivot = end
            left = st - 1
            for i in range(st,end):
                if B[i][2] <= B[pivot][2]:
                    left += 1
                    B[left], B[i] = B[i], B[left]
            left += 1
            B[left], B[pivot] = B[pivot], B[left]

            quick_sort(st,left-1)
            quick_sort(left+1, end)

        def union_by_height(a,b):
            if parent[a] == parent[b]:
                return

            if rank[parent[a]] > rank[parent[b]]:
                parent[parent[b]] = parent[a]
            elif rank[parent[a]] < rank[parent[b]]:
                parent[parent[a]] = parent[b]
            else:
                parent[parent[b]] = parent[a]
                rank[parent[a]] += 1

        def find_root_by_compression(a):
            if parent[a] == a:
                return parent[a]
            else:
                parent[a] = find_root_by_compression(parent[a])
            
            return parent[a]

        
        quick_sort(0,len(B)-1) # sorted edges

        parent = [i for i in range(A)]
        rank = [0]*A
        
        min_cost = 0
        for i in range(len(B)):
            u = B[i][0]
            v = B[i][1]

            ru = find_root_by_compression(u-1)
            rv = find_root_by_compression(v-1)

            if ru != rv:
                union_by_height(u-1,v-1)
                min_cost += B[i][2]
        
        return min_cost