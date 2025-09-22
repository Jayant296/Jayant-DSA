class Solution:
    # @param A : integer
    # @return an integer
    def power(self,a,n):
        if n==0:
            return 1
        return a*self.power(a,n-1)
    def solve(self, A):
        if A==1:
            return 0
        start=0
        end=A
        mid=(start+end)//2
        while start < end:
            power1=self.power(2,mid)
            power2=self.power(2,mid+1)
            if power1 <= A and power2>A:
                return 2**mid
            elif power1<A:
                start=mid+1
            else:
                end=mid-1
        