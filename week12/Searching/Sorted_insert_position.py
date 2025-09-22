class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def BinSearch(self,A,st,end,t):
        if st>end:
            return st
        mid=(st+end)//2
        if A[mid]!=t:
            if mid==0 and A[mid+1]>t:
                if A[mid]>t:
                    return mid
                else:
                    return mid+1
            if mid==len(A)-1 and A[mid]<t:
                return len(A)
            else:
                if A[mid-1]<t and A[mid+1]>t:
                    if A[mid]>t:
                        return mid
                    else:
                        return mid+1
        if A[mid]==t:
            return mid
        if A[mid]>t:
            return self.BinSearch(A,st,mid-1,t)
        else:
            return self.BinSearch(A,mid+1,end,t)
    def searchInsert(self, A, B):
        if len(A)==0:
            return 0
        if len(A)==1:
            return 0 if A[0]==B else 0 if A[0]>B else 1
        return self.BinSearch(A,0,len(A),B)