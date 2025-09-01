class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum=-10000000000
        current_sum=0
        n= len(A)
        for i in range(n):
            if A[i]>=0:
                if current_sum<=0:
                    current_sum=A[i]
                else:
                    current_sum+=A[i]
            else:
                if current_sum==0:
                    current_sum=A[i]
                elif current_sum+A[i]>0:
                    max_sum=max(current_sum,max_sum)
                    current_sum+=A[i]
                else:
                    max_sum=max(current_sum,max_sum)
                    current_sum=A[i]
        if current_sum>max_sum:
            max_sum=current_sum
        return max_sum