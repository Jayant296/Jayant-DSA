class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def solve(self, A, B, C):
        lcm=(B*C)//(self.gcd(B,C)) #calculating lcm of b and c.
        # while factor>A:
        #     if factor > A:
        #         n//=2
        #     else:
        #         if (n+1)*lcm>A:  (  WASTAGE OF TIME )
        #             return n     (  JUST DIVIDE A BY LCM)
        #         else:
        #             n+=1
        return A//lcm