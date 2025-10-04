class Solution:
    # @param A : list of integers
    # @return an integer
    def reversePairs(self, A, st, end, pairs_count):
        if st == end:
            return [A[st]]
        mid = (st + end) // 2
        left = self.reversePairs(A, st, mid, pairs_count)
        right = self.reversePairs(A, mid+1, end, pairs_count)
        ans = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] > 2*right[j]:
                pairs_count[0] += len(left) - i
                j += 1
            else: 
                i += 1
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j += 1
        for l in range(i, len(left)):
            ans.append(left[l])
        for r in range(j, len(right)):
            ans.append(right[r])
        return ans
    def solve(self, A):
        pairs_count = [0]
        self.reversePairs(A, 0, len(A)-1, pairs_count)
        return pairs_count[0]
