class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def merge_sort(self, A, st, end):
        if st == end:
            return [A[st]]
        mid = (st + end)//2
        left = self.merge_sort(A, st, mid)
        right = self.merge_sort(A, mid+1, end)
        ans = []
        i, j = 0, 0
        while i< len(left) and j< len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        for l in range(i, len(left)):
            ans.append(left[l])
        for r in range(j, len(right)):
            ans.append(right[r])
        return ans
	def kthsmallest(self, A, B):
        ans = self.merge_sort(A, 0, len(A)-1)
        for i in range(len(ans)):
            if i == B-1:
                return ans[i]