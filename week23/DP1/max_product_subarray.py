'''
Problem Description

Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

Return an integer corresponding to the maximum product possible.

NOTE: Answer will fit in 32-bit integer value.


'''
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
        '''
        dp = [[float('inf') for _ in range(len(A))] for _ in range(len(A))]
        i = 0
        for j in range(len(A)):
            dp[i][j] = A[j]
            i += 1
        i = 0
        for j in range(1,len(A)):
            dp[i][j] = max(A[i],A[j],A[i]*A[j])
            i += 1
        def max_prod(i,j):
            if i == j :
                return A[i]
            if dp[i][j] != float('inf'):
                return dp[i][j]
            dp[i][j] = max(max_prod(i,j-1),A[j],max_prod(i,j-1)*A[j])
            return dp[i][j]
        
        return max_prod(0,len(A)-1)
        '''
        # Kadane style DP
        curr_max = curr_min = A[0]
        global_max = A[0]
        for i in range(1,len(A)):
            if A[i] > 0:
                curr_max = max(curr_max*A[i],A[i])
                curr_min = min(curr_min*A[i],A[i])
                global_max = max(global_max,curr_max)
            elif A[i] < 0:
                temp = curr_max
                curr_max = max(curr_min * A[i], A[i])
                curr_min = min(temp*A[i],A[i])
                global_max = max(global_max,curr_max)
            else:
                global_max = max(global_max,0)
                curr_max = 1
                curr_min = 1
            
        return global_max

