'''

Problem Description

Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.

You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.

Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X.

NOTE:

Level and Depth of the root is considered as 0.
It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
Please read the input format for more clarification.
'''
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):
        '''
        the logic we are using here is first we make a dictionary which
        stores the values of nodes of each level.
        and then we run a loop of the querries to find ans of each querry efficiently.
        '''
        # using dfs here
        adj_list = {i:[] for i in range(1,A+1)}
        for i in range(len(B)):
            adj_list[B[i]].append(C[i])
            adj_list[C[i]].append(B[i])
        visited1 = [0 for _ in range(A)]
        visited2 = [0 for _ in range(A)]

        # dfs for max_depth 
        def dfs_maxdepth(curr):
            depth = 0
            visited1[curr-1] = 1
            for i in adj_list[curr]:
                if visited1[i-1]:
                    continue
                depth = max(depth, 1 + dfs_maxdepth(i))
            return depth

        # dfs for filling values in dict
        max_depth = dfs_maxdepth(1)
        level_elements = {i:[] for i in range(max_depth+1)}
        def dfs(node,curr_level):
            level_elements[curr_level].append(D[node-1])
            visited2[node-1] = 1
            for i in adj_list[node]:
                if not visited2[i-1]:
                    dfs(i,curr_level+1)

        # bin search
        def bin_search(L,X): # lower bound
            arr = level_elements[L]
            st, end = 0, len(arr)-1
            ans = -1
            while st <= end:
                mid = (st + end)//2
                if arr[mid] >= X:
                    ans = arr[mid]
                    end = mid -1
                else:
                    st = mid + 1
            return ans
        
        dfs(1,0)
        for i in level_elements.values():
            i.sort()
        
        ans = []
        for i in range(len(E)):
            L = E[i] % (max_depth+1)
            X = F[i]
            val = bin_search(L,X)
            ans.append(val)

        return ans