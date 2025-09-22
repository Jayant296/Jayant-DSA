class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def pivot(self,A,st,end):
        if st>=end:
            return st
        mid=(st+end)//2
        if A[mid]<A[mid-1]:
            return mid
        if A[mid]>A[mid+1]:
            return mid+1
        if A[mid]>=A[st]:
            return self.pivot(A,mid+1,end)
        else:
            return self.pivot(A,st,mid-1)
    def BinSearch(self,A,st,end,t):
        if st>end:
            return -1
        mid=(st+end)//2
        if A[mid]==t:
            return mid
        if A[mid]>t:
            return self.BinSearch(A,st,mid-1,t)
        else:
            return self.BinSearch(A,mid+1,end,t)
    def search(self,A,B):
        if len(A)==1:
            if A[0]==B:
                return 0
            else:
                return -1
        if A[0]<A[len(A)-1]:
            return self.BinSearch(A,0,len(A)-1,B)
        else:
            pivot=self.pivot(A,0,len(A)-1)
            if B>=A[0]:
                return self.BinSearch(A,0,pivot-1,B)
            else:
                return self.BinSearch(A,pivot,len(A)-1,B)