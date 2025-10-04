class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        i, j = 0, 0 
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(B[j])
                j+=1 
        for l in range(i, len(A)):
            ans.append(A[l])
        for r in range(j, len(B)):
            ans.append(B[r])
        return ans