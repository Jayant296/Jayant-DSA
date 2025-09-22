class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        m=len(A[0])
        i,j=0,m-1
        ans=1000000000000
        while i<n and j>=0:
            if A[i][j]==B:
                ans=min(ans,((i+1) * 1009 + (j+1)))
                j-=1
            elif A[i][j]<B:
                i+=1
            else:
                j-=1
        if ans!=1000000000000:
            return ans
        else:
            return -1