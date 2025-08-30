class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def merge(self,left,right):
        l=0
        r=0
        ans=[]
        while l<len(left) and r<len(right):
            if left[l]<=right[r]:
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
    def sort(self,A,start,end):
        if start==end:
            return [A[start]]
        else:
            mid = (start+end)//2
            left = self.sort(A,start,mid)
            right = self.sort(A,mid+1,end)
        return self.merge(left,right)
    def hotel(self, arrive, depart, K):
        arrive=self.sort(arrive,0,len(arrive)-1)
        depart=self.sort(depart,0,len(depart)-1)
        p1=0
        p2=0
        guest=0
        while(p1<len(arrive) and p2<len(depart)):
            if arrive[p1]<=depart[p2]:
                guest+=1
                if guest>K:
                    return False
                p1+=1
            else:
                guest-=1
                p2+=1
        return True
