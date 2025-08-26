class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        countA,countB=0,0
        i,j=0,0
        final_merged_array=[]
        while i<len(A) and j<len(B):
            if countA==len(A):
                final_merged_array.append(B[j])
                j+=1
                countB+=1
            elif countB==len(B):
                final_merged_array.append(A[i])
                i+=1
                countA+=1
            elif A[i]<=B[j]:
                final_merged_array.append(A[i])
                countA+=1
                i+=1
            else:# B[j]<=A[i]
                final_merged_array.append(B[j])
                countB+=1
                j+=1
        while i<len(A):
            final_merged_array.append(A[i])
            i+=1
        while j<len(B):
            final_merged_array.append(B[j])
            j+=1
        return final_merged_array