class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        ele_count=1
        prev=A[0]
        insert_pos=1
        for i in range(1,len(A)):
            if ele_count==2 and A[i]==prev:
                continue
            if A[i]==prev:
                A[insert_pos]=A[i]
                ele_count+=1
                insert_pos+=1
            else:
                prev=A[i]
                ele_count=1
                A[insert_pos]=A[i]
                insert_pos+=1
        return insert_pos