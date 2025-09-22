class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self, a, b, m):
        if b==0:
            return 1
        elif b%2==0:
            return self.power(a*a % m, b//2, m)
        else:
            return (a * self.power(a*a % m, b//2, m)) % m
    def solve(self, A, B):
        '''
        as we know, from MULTIPLICATION PROPERTY we can say that ((a%m)*(x%m))%m=1
        wrt mod m, where x is inverse mod of a wrt m.
        and x would be in range of [1,m-1],
        so we can say that the value of x in range [1,m-1] gives 1 on operated with this  
        equation ((a%m)*(x%m))%m=1 , is the ans.
        
        for i in range(1,B):
            if ((A%B)*(i%B))%B==1:
                return i%B
        THIS THING WORKS FOR SMALL NUMBERS BUT FOR LARGE NUMBERS WE GET ERROR ,
        SO WE USE (A**(P-2)=A**-1) 
        '''
        return self.power(A,B-2,B)