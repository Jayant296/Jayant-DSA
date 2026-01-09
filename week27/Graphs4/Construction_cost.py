'''
Docstring for Construction_cost
Problem Description

Flipkart has ‘A’ local distribution centers located across a large metropolitan city. Each distribution center needs to be interconnected through roads to facilitate efficient movement of goods. The cost of constructing a road between any two distribution centers is represented by the weight of the edge connecting them.

Given a graph with ‘A’ nodes representing the distribution centers and C weighted edges representing the possible roads between them, your task is to find the minimum total cost of constructing roads such that every distribution center can be reached from the first distribution center.

Cost Calculation:
The cost of constructing the roads is the sum of the weights of the edges selected for the construction.

NOTE: Return the answer modulo 10^9+7 as the answer can be large.

'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        if A <= 1:
            return 0
            
        '''
        using DSU and Kruskal's algo
        '''
        def quick_sort(st,end,arr):
            if st >= end:
                return
            pivot = end 
            left = st - 1

            for i in range(st,end):
                if arr[i][2] < arr[pivot][2]:
                    left += 1
                    arr[i], arr[left] = arr[left], arr[i]
            
            left += 1
            arr[left], arr[pivot] = arr[pivot], arr[left]
            quick_sort(st,left-1,arr)
            quick_sort(left+1,end,arr)

            return

        prev = B[0][2]
        for i in range(1,len(B)):
            if prev > B[i][2]:
                quick_sort(0,len(B)-1,B)
                break
            else:
                prev = B[i][2]

        def find_root(x): # finds root(x) by compression logic
            if parent[x] == x:
                return x
            parent[x] = find_root(parent[x])
            return parent[x]

        def union_by_height(a,b):
            ra = find_root(a)
            rb = find_root(b)
            
            if ra == rb :
                return False
            
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            elif rank[rb] > rank[ra]:
                parent[ra] = rb
            else:
                parent[ra] = rb
                rank[rb] += 1
            
            return True

        parent = [i for i in range(A)]
        rank = [0 for _ in range(A)]
        cost = 0
        mod = (10**9 + 7)

        for i in range(len(B)):
            u = B[i][0] - 1
            v = B[i][1] - 1

            if union_by_height(u,v):
                cost = (cost + B[i][2]) % mod

        return cost 