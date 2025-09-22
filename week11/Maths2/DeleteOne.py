class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    
    def solve(self, A):
        
        n=len(A)
        if n<=1:
            return A[0]
        
        prefix_gcd=[]
        prev=0
        for i in range(n):
            prev=self.gcd(prev,A[i])
            prefix_gcd.append(prev)
        
        prev=0
        suffix_gcd=[]
        for i in range(n-1,-1,-1):
            prev=self.gcd(prev,A[i])
            suffix_gcd.append(prev)
        
        max_val=0
        j=n-1 
        '''here we are setting the j as an iterator index of suffix gcd as its 
                storing the values in the reverse order'''
        for i in range(n):
            if i==0:
                curr_val=self.gcd(0,suffix_gcd[j-1])
            elif i==n-1:
                curr_val=self.gcd(prefix_gcd[i-1],0)
            else:
                curr_val=self.gcd(prefix_gcd[i-1],suffix_gcd[j-1])
            max_val=max(curr_val,max_val)
            j-=1
        
        return max_val