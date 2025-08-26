# adding a new file
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
    def solve(self, A, B, C):
        a,b,c=len(A)-1,len(B)-1,len(C)-1
        ans = max(A[a],B[b],C[c]) - min(A[a],B[b],C[c])
        while a>=0 and b>=0 and c>=0:
            curr_max=max(A[a],B[b],C[c])
            curr_min=min(A[a],B[b],C[c])
            ans=min(ans,curr_max-curr_min)
            if curr_max==A[a]:
                a-=1
            elif curr_max==B[b]:
                b-=1
            else:
                c-=1
        return ans
