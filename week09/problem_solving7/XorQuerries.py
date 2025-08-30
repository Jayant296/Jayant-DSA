class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        cumulative_xor=dict()
        count_store=dict()
        for i in range(len(A)):
            if i==0:
                cumulative_xor[i+1]=A[i]
            else:
                cumulative_xor[i+1]=(A[i]^cumulative_xor[i])
        count0=0
        count1=1
        for i in range(len(A)): 
            if A[i]==1:
                count1+=1
                count_store[i+1]=(count0,count1)
            else:
                count0+=1
                count_store[i+1]=(count0,count1)
        result=[]
        for i in range(len(B)):
            ans=[]
            left=B[i][0]
            right=B[i][1]
            if left<=1:
                ans.append(cumulative_xor[right])
                ans.append(count_store[right][0])
            else:
                ans.append(cumulative_xor[right]^cumulative_xor[left-1])
                ans.append(count_store[right][0]-count_store[left-1][0])
            result.append(ans)
        return result