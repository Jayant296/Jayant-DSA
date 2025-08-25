# sum of all sub-matrices solution
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        total_sum=0
        for i in range(n):
             for j in range(n):
                 top_left=(i+1)*(j+1)
                 bottom_right=(n-i)*(n-j)
                 total_sum+=((top_left*bottom_right)*A[i][j])
        return total_sum