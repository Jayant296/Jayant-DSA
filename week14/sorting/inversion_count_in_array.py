class Solution:
    # @param A : list of integers
    # @return an integer
    def inversions(self, A, st, end, inversion_count):
        if st == end:
            return [A[st]]
        mid = (st + end) // 2
        left = self.inversions(A, st, mid, inversion_count)
        right = self.inversions(A, mid+1, end, inversion_count)
        ans = []
        i, j = 0, 0
        while i < len(left) and j< len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
                inversion_count[0] += 1 * (len(left)-i)
        for l in range(i, len(left)):
            ans.append(left[l])
        for r in range(j, len(right)):
            ans.append(right[r])
        return ans
    def solve(self, A):
        inversion_count = [0]
        self.inversions(A, 0, len(A)-1, inversion_count)
        return inversion_count[0] % (10**9 + 7)