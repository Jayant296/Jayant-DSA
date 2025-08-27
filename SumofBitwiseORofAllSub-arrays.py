class Solution:
    def SumofBitwiseORofAllSub_arrays(self,A):
        def dec_to_bin(n): # conversion of decimal to binary
            count=0
            ans=[]
            while count<32:
                if n==0 and count<32:
                    ans.append(0)
                    count+=1
                else:
                    rem=n%2
                    n=n//2
                    ans.append(rem)
                    count+=1
            return ans[::-1]
        #new array creation
        newA=[]
        for i in A:
            newA.append(dec_to_bin(i))
        total_Sub_arrays= (len(A)*(len(A)+1))//2 #calculating the total no. of sub-arrays for a single column
        pos=0
        total_sum=0
        for j in range(31,-1,-1): # running loop in reverse order 
            total_contribution=total_Sub_arrays*(2**pos) # calculating the contribution of a col by assuming all bits as one
            count0=0
            for i in range(len(newA)):
                if newA[i][j]==1:
                    total_contribution-=(((count0*(count0+1))//2)*(2**pos)) 
                    count0=0
                else:
                    count0+=1
            total_sum+=total_contribution
            pos+=1
        return total_sum