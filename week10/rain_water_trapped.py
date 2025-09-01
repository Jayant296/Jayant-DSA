class Solution:
	 # @param A : tuple of integers
	 # @return an integer
     def trap(self, A):
        maxInd=0
        for i in range(len(A)):
            if A[i]>A[maxInd]:
                maxInd=i
        rightmax=maxInd
        leftmax=0
        ans=0
        for i in range(rightmax):
            if A[i]>A[leftmax]:
                leftmax=i
            ans+=min(A[leftmax],A[rightmax])-A[i]
        leftmax=maxInd
        rightmax=len(A)-1
        for i in range(rightmax,leftmax,-1):
            if A[i]>A[rightmax]:
                rightmax=i
            ans+=min(A[leftmax],A[rightmax])-A[i]
        return ans