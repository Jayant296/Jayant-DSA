class Solution:
    # @param A : list of integers
    # @return an integer
    def BinSearch(self,A,st,end):
        if st>end:
            return st
        mid=(st+end)//2
        if mid==0:
            if A[mid]>=A[mid+1]:
                return A[mid]
            else:
                return self.BinSearch(A,mid+1,end)
        if mid==len(A)-1:
            if A[mid]>=A[mid-1]:
                return A[mid]
            else:
                return self.BinSearch(A,st,mid-1)
        else:
            if A[mid]>=A[mid+1] and A[mid]>=A[mid-1]:
                return A[mid]
            if A[mid]<A[mid+1]:
                return self.BinSearch(A,mid+1,end)
            if A[mid]<A[mid-1]:
                return self.BinSearch(A,st,mid-1)
    def solve(self, A):
        n=len(A)
        if n==1:
            return A[0]
        return self.BinSearch(A,0,n-1)
