class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        Amax1=A[0]
        Amax2=A[0]
        for i,num in enumerate(A):
            if num+i>Amax1:
                Amax1=num+i
            if num-i>Amax2:
                Amax2=num-i
        Amin1=A[0]
        Amin2=A[0]
        for j,num in enumerate(A):
            if num+j<Amin1:
                Amin1=num+j 
            if num-j<Amin2:
                Amin2=num-j  
        C1=(Amax1)-(Amin1) 
        C2=(Amax2)-(Amin2)
        return max(C1,C2)