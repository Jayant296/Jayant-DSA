class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        frequency = dict()
        ans = float('inf')
        for i in range(len(A)):
            if A[i] in frequency:
                if i - frequency[A[i]] < ans:
                    ans = i - frequency[A[i]]
                frequency[A[i]] = i
            else:
                frequency[A[i]] = i
        if ans == float('inf'):
            return -1
        else:
            return ans
