class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def merge(self,left,right):
        l=0
        r=0
        ans=[]
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                ans.append(left[l])
                l+=1
            else:
                ans.append(right[r])
                r+=1
        for i in range(l,len(left)):
            ans.append(left[i])
        for j in range(r,len(right)):
            ans.append(right[j])
        return ans
    def sort(self,List,start,end):
        if start==end:
            return [List[start]]
        else:
            mid=(start+end)//2
            left=self.sort(List,start,mid)
            right=self.sort(List,mid+1,end)
            return self.merge(left,right)
    def BintoDec(self,Bin):
        ans=0
        pos=0
        for i in range(len(Bin)-1,-1,-1):
            ans+=Bin[i]*(2**pos)
            pos+=1
        return ans
    def solve(self, A):
        #convert bin to dec and store in hashmap with indexes
        #thenjust return indexes of a no. which are more than 1,except the starting index
        hashA=dict()
        for i in range(len(A)):
            dec=self.BintoDec(A[i])
            if dec in hashA.keys():
                hashA[dec].append(i)
            else:
                hashA[dec]=[i]
        ans=[]
        for key,val in hashA.items():
            if len(val)>1:
                for i in range(1,len(val)):
                    ans.append(val[i]+1)
        return self.sort(ans,0,len(ans)-1)