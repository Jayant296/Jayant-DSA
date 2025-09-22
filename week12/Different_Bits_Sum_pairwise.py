class Solution:
	# @param A : list of integers
	# @return an integer
	def dectobin(self,n):
		ans=[]
		for i in range(32):
			if i<32 and n==0:
				ans.append(0)
			else:
				rem=n%2
				n//=2
				ans.append(rem)
		return ans
	def cntBits(self, A):
		newA=[]
		for i in A:
			newA.append(self.dectobin(i))
		unique_bits=0
		for j in range(32):
			count0,count1=0,0
			for i in range(len(newA)):
				if newA[i][j]==1:
					count1+=1
				else:
					count0+=1
			unique_bits=(unique_bits%(10**9+7) + (2*count0*count1)%(10**9+7)) %(10**9+7)

		return unique_bits	
	