class Solution:
    def Hamming_distance(self,A):
        def decimal_to_binary(n):
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
            return ans[::-1] # returns reversed list
        newA=[]
        for i in range(len(A)):
            Bin=decimal_to_binary(A[i])
            newA.append(Bin)
        hamming_distance=0
        for j in range(32):
            count0=0
            count1=0
            for i in range(len(newA)):
                if newA[i][j]==1:
                    count1+=1
                else:
                    count0+=1
            hamming_distance+=2*count0*count1
        return hamming_distance