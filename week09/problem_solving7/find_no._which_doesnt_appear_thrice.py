class Solution:
    def number_appear_only_once(self,A):
        def dec_to__bin(n):
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
        newA=[]
        for i in range(len(A)):
            Bin=dec_to__bin(A[i])
            newA.append(Bin)
        ans=[]
        for j in range(32):
            count0=0
            count1=0
            for i in range(len(newA)):
                if newA[i][j]==0:
                    count0+=1
                else:
                    count1+=1
            if count1%3 != 0:
                ans.append(1)
            else:
                ans.append(0)
        Sum=0
        for i,num in enumerate(ans[::-1]):
            Sum+=(2**i)*num
        return Sum