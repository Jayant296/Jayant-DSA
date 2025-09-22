class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # first we'll calculate the mod of all no. with B. 
        n=len(A)
        for i in range(n):
            A[i]=A[i]%B

        # then we'll calculate the count of every remainder (in range [0,B-1]) and store in hashmap.
        hash_count=dict()
        for i in A:
            if i in hash_count:
                hash_count[i]+=1
            else:
                hash_count[i]=1
        # then simply calculate the sum of all possible pairs which are divisible by B .
        pair_count=0
        for i in range(B):
            if i in hash_count:
                if i==0 :
                    n= hash_count[0]
                    pair_count= (pair_count % (10**9+7) + ((n*(n-1))//2) % (10**9+7)) % (10**9+7)
                else:
                    if B-i in hash_count:
                        if B-i==i:
                            n= hash_count[i]
                            pair_count= (pair_count % (10**9+7) + ((n*(n-1))//2) % (10**9+7)) % (10**9+7)
                        else:
                            pair_count= (pair_count % (10**9+7) + (hash_count[i]*hash_count[B-i]) % (10**9+7)) % (10**9+7)
            hash_count.pop(i, None)
        return pair_count
    