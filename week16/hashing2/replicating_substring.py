class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        frequency = dict()
        for i in B:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        for i in frequency.values():
            if i % A != 0:
                return -1
        return 1