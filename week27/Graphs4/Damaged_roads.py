'''
Docstring for Damaged_roads
Problem Description

You are the Prime Minister of a country and once you went for a world tour.
After 5 years, when you returned to your country, you were shocked to see the condition of the roads between the cities. So, you plan to repair them, but you cannot afford to spend a lot of money.

The country can be represented as a (N+1) x (M+1) grid, where Country(i, j) is a city.

The cost of repairing a road between (i, j) and (i + 1, j) is A[i]. The cost of repairing a road between (i, j) and (i, j + 1) is B[j].

Return the minimum cost of repairing the roads such that all cities can be visited from city indexed (0, 0).

As the cost can be large, return the cost modulo 109+7.

'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        '''
        # applying the prim's algo
        
        # percolate down
        def percolate_down(curr,arr):
            left = 2*curr + 1
            right = 2*curr + 2
            small = curr

            while True:
                if left < len(arr) and arr[small][1] > arr[left][1]:
                    small = left
                if right < len(arr) and arr[small][1] > arr[right][1]:
                    small = right
                if small != curr:
                    arr[small], arr[curr] = arr[curr], arr[small]
                    curr = small
                    left = 2*curr + 1
                    right = 2*curr + 2
                else:
                    break
        
        # percolate up
        def percolate_up(curr,arr):
            while curr > 0:
                parent = (curr - 1)//2
                if arr[curr][1] < arr[parent][1]:
                    arr[curr], arr[parent] = arr[parent], arr[curr]
                    curr = parent
                else:
                    break

        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        country = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        visited = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        min_heap = [((0,0),0)] # ((indices of node),weight)
        min_cost = 0
        while min_heap:
            node = min_heap[0]
            min_heap[0], min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1], min_heap[0]
            del min_heap[len(min_heap)-1]
            if min_heap:
                percolate_down(0,min_heap)

            if visited[node[0][0]][node[0][1]] :
                continue
            min_cost += node[1]
            visited[node[0][0]][node[0][1]] = 1
            
            # exploring neighbours
            for i,j in neighbours:
                x = node[0][0] + i
                y = node[0][1] + j

                if 0 <= x <= len(A) and 0 <= y <= len(B) and not visited[x][y]:
                    if i == 0 : # horizontal movement
                        cost = B[min(y,node[0][1])]
                    elif j == 0 : # vertical movement
                        cost = A[min(x,node[0][0])]
                    min_heap.append(((x,y),cost))
                    percolate_up(len(min_heap)-1,min_heap)

        return min_cost % (10**9 + 7)

        Too slow with prims for large test cases
        so using kruskals algo

        '''
        # as we want to move from (0,0) to all the cities so,
        # applying greedy Kruskal's algo
        '''
        what we do here is we use the compressed kruskal algo,
        in which we won't connect cities one by one but we sort
        the cost of rows and cols and then simply connect all cities present in either
        two rows or columns.
        '''
        # def quick_sort(st,end,arr):
        #     if st >= end:
        #         return 
        #     pivot = end
        #     left = st - 1

        #     for i in range(st,end):
        #         if arr[i] <= arr[pivot]:
        #             left += 1
        #             arr[left], arr[i] = arr[i], arr[left]
                
        #     left += 1
        #     arr[left], arr[pivot] = arr[pivot], arr[left]
        #     quick_sort(st,left-1,arr)
        #     quick_sort(left+1,end,arr)
    
        # quick_sort(0,len(A)-1,A)
        # quick_sort(0,len(B)-1,B)
        A.sort()
        B.sort()

        rows = len(A) + 1
        cols = len(B) + 1
        mod = (10**9) + 7

        i = j = 0 # pointers for using costs in sorted order
        min_cost = 0

        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                min_cost += A[i]*cols
                rows -= 1
                i += 1
            else:
                min_cost += B[j]*rows
                cols -= 1
                j += 1

        while i < len(A):
            min_cost += A[i] * cols
            rows -= 1
            i += 1
        
        while j < len(B):
            min_cost += B[j] * rows
            cols -= 1
            j += 1 

        return min_cost % mod
