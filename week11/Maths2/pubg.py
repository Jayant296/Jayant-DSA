class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def solve(self, A):
        min_health=0
        for i in A:
            min_health=self.gcd(i,min_health)
        return min_health