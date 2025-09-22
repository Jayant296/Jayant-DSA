class Solution:
    # @param A : list of integers
    # @return an integer
    def SingleElement(self,A,st,end):
        mid=(st+end)//2
        if mid==0 :
            if A[mid]!=A[mid+1]:
                return A[mid]
        if mid==len(A)-1:
            if A[mid]!=A[mid-1]:
                return A[mid] 
        else:       
            if A[mid]!=A[mid+1] and A[mid]!=A[mid-1]:
                return A[mid]
        if mid%2==0: #for 0 based indexing its odd.
            if A[mid]!=A[mid+1]:
                return self.SingleElement(A,st,mid-1)
            else:
                return self.SingleElement(A,mid+1,end)
        else: #even for 0 based indexing.
            if A[mid]!=A[mid+1]:
                return self.SingleElement(A,mid+1,end)
            else:
                return self.SingleElement(A,st,mid-1)
    def solve(self, A):
        if len(A)==1:
            return A[0]
        return self.SingleElement(A,0,len(A)-1)
    