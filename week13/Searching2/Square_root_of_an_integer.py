class Solution:
    # @param A : integer
    # @return an integer
    def BinSearch(self,n,st,end):
        if st > end:
            return end
        mid=(st+end) // 2
        if mid*mid == n:
            return mid
        if mid * mid > n:
            return self.BinSearch(n, st, mid - 1)
        else:
            return self.BinSearch(n, mid + 1, end)
    def sqrt(self, A):
        if A < 2:
            return A
        return int(self.BinSearch(A,1,A))