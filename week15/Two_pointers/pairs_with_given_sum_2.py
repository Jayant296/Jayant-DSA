class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B): 
        frequencies = dict()
        for i in A:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1   
        count = 0
        i, j = 0, len(A)-1
        while i < j:
            if A[i] + A[j] < B:
                i += frequencies[A[i]]
            elif A[i] + A[j] > B:
                j -= frequencies[A[j]]
            else:
                if A[i] == A[j]:
                    count += frequencies[A[i]] * (frequencies[A[i]] - 1) // 2 # for duplicates at i and j.
                else:
                    count += frequencies[A[i]] * frequencies[A[j]]
                i += frequencies[A[i]]
                j -= frequencies[A[j]]
        return count % (10**9 + 7)