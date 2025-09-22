class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def solve(self, A):
        count_even=0
        count_odd=0
        for i in A:
            if i==1:
                return 0
            if i%2==0:
                count_even+=1
            else:
                count_odd+=1
        if count_even==0 or count_odd==0:
            return -1
        else:
            odd_gcd=0
            for i in A:
                if i%2!=0:
                    odd_gcd=self.gcd(i,odd_gcd)
                if odd_gcd==1:
                    return 0
            for i in A:
                if i%2==0 and i%odd_gcd!=0:
                    return 0
            return -1
