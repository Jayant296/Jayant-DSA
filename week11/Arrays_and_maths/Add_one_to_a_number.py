class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        msb=None
        for i in range(len(A)):# finding the index pf most signifincant bit.
            if msb is None and A[i]!=0:
                msb=i
                break
        carry=1
        for i in range(len(A)-1,-1,-1):# adding 1 to the number.
            if A[i]==9:
                A[i]=0
            else:
                A[i]+=1
                carry-=1
                break
        if carry==0:
            return A[msb:]
        else:
            if msb==0:# if msb is at oth index.
                A.append(0)
                i=len(A)-1
                while i>0:
                    A[i]=A[i-1]
                    i-=1
                A[0]=1
                return A
            else:# when msb is not at the 0th index.
                A[msb-1]=1
                msb=msb-1
                return A[msb:]
