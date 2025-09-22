class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        matrix_sum=0
        n=len(A)
        for i in range(n):
            for j in range(n):
                top_left=(i+1)*(j+1)
                bottom_right=(n-i)*(n-j)
                matrix_sum+=(top_left*bottom_right)*(A[i][j])
        return matrix_sum