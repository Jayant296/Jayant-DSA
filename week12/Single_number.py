class Solution:
    # @param A : tuple of integers
    # @return an integer
    def DectoBin(self,n):
        ans=[]
        for i in range(32):
            if i<=31 and n==0:
                ans.append(0)
            else:
                rem=n%2
                n//=2
                ans.append(rem)
        return ans
    def singleNumber(self, A): 
        newA=[]
        for i in A:
            newA.append(self.DectoBin(i))
        result=[]
        for j in range (32):
            count1=0
            for i in range(len(newA)):
                if newA[i][j]==1:
                    count1+=1
            if count1%2==0:
                result.append(0)
            else:
                result.append(1)
        power=0
        num=0
        for i in result:
            num+=(i*(2**power))
            power+=1
        return num
