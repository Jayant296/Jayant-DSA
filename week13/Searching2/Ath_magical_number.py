class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b, a % b)
    def BinSearch(self, A, B, C, st, end, ans):
        if st>end:
            return ans % (10**9 + 7)
        mid = (st + end) // 2
        L = (B * C) // self.gcd(B, C)
        count = mid//B + mid//C - mid//L
        if count >= A:
            ans = min(ans, mid)
            return self.BinSearch(A, B, C, st, mid-1, ans)
        else:
            return self.BinSearch(A, B, C, mid+1, end, ans)
    def solve(self, A, B, C):
        return self.BinSearch(A, B, C, min(B, C), A * min(B, C), float('inf'))