class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self,a,b,m):
        if b==0:
            return 1
        elif b%2==0:
            return self.power(a**2 % m, b//2, m)
        else:
            return (a*self.power(a**2 % m, b//2, m) % m)         
    def solve(self, A, B):
        '''
        first we'll calculate the mod factorial of B wrt (p-1) as it's the 'r' which we'll
        use to apply the fermat's theorm
        '''
        r=1
        for i in range(1,B+1):
            r=((r%(10**9+7-1))*(i%(10**9+7-1)))%(10**9+7-1) # here p=(10**9+7) and p-1=(10**9+7-1) and doing x%(p-1) continuously.
        # r=r%(10**9+7-1)
        '''
        now we'll simply calculate the a^r.
        '''
        return self.power(A,r,10**9+7)