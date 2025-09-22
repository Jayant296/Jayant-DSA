class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def BinSearch(self,A,st,end,t):
        if st[0]>end[0] and st[1]>end[1]:
            return A[st[0]][st[1]]
        mid=[(st[0]+end[0])//2,(st[1]+end[1])//2]
        if mid[0]==0:
            if mid==[0,0]:
                if A[mid[0]][mid[1]]==t:
                    return True
                if A[mid[0]][mid[1]]<t:
                    return self.BinSearch(A,[0,1],end,t)
                else:
                    return -1
            if A[mid[0]][mid[1]]==t:
                return True
            if A[mid[0]][mid[1]]<t:
                return self.BinSearch(A,[mid[0],mid[1]+1],end,t)
            else:
                return self.BinSearch(A,st,[mid[0]-1,len(A[0])-1],t)
        if mid[1]==len(A[0])-1:
            if mid==[len(A)-1,len(A[0])-1]:
                if A[mid[0]][mid[1]]==t:
                    return True
                if A[mid[0]][mid[1]]<t:
                    return self.BinSearch(A,st,[len(A)-1,len(A[0])-1],t)
                else:
                    return False
            if A[mid[0]][mid[1]]==t:
                return True
            if A[mid[0]][mid[1]]>t:
                return self.BinSearch(A,st,[mid[0],mid[1]-1],t)
            else:
                return self.BinSearch(A,[mid[0]+1,0],end,t)
        else:
            if A[mid[0]][mid[1]]==t:
                return True
            if A[mid[0]][mid[1]]>t:
                return self.BinSearch(A,st,[mid[0],mid[1]-1],t)
            else:
                return self.BinSearch(A,[mid[0],mid[1]+1],end,t)
    def searchMatrix(self, A, B):
        return self.BinSearch(A,[0,0],[len(A)-1,len(A[0])-1],B)