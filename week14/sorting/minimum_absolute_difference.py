class Solution:
    # @param A : list of integers
    # @return an integer
    def mergeSort(self, A, st, end):
        if st == end:
            return [A[st]]
        mid = (st + end) // 2
        left = self.mergeSort(A, st, mid)
        right = self.mergeSort(A, mid+1, end)
        ans = []
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
        ans = self.mergeSort(A, 0, len(A)-1)
        min_val = float('inf')
        for i in range(1,len(ans)):
            min_val = min(abs(ans[i]-ans[i-1]),min_val)
        return min_val