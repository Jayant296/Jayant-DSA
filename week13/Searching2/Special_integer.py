class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def BinSearch(self, prefix_sum_array, B, st, end, ans):
        if st > end: 
            return ans
        mid = (st + end) // 2
        feasible = True
        for i in range(mid-1, len(prefix_sum_array)):
            if i == mid-1:
                curr_sum = prefix_sum_array[i]
            else:
                curr_sum = prefix_sum_array[i] - prefix_sum_array[i-mid]
            if curr_sum > B:
                feasible = False
                break
        if feasible:
            ans = max(ans, mid)
            return self.BinSearch(prefix_sum_array, B, mid+1, end, ans)
        else:
            return self.BinSearch(prefix_sum_array, B, st, mid-1, ans)
    def solve(self, A, B):
        n = len(A)
        prefix_A=[]
        Sum=0
        for i in range(n):
            Sum += A[i]
            prefix_A.append(Sum)
        return self.BinSearch(prefix_A, B, 1, len(A), 0)