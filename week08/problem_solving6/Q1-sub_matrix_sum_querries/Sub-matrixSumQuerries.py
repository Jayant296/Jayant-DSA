class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        m=len(A)
        n=len(A[0])
        row_hash_map=dict()
        col_hash_map=dict()#sub-matrix sum
        for i in range(m):
            pre_sum=0
            row_hash_map[i]=[]
            for j in range(n):
                pre_sum+=A[i][j]
                row_hash_map[i].append(pre_sum)
        for j in range(n):
            pre_sum=0
            col_hash_map[j]=[]
            for i in range(m):
                pre_sum+=row_hash_map[i][j]
                col_hash_map[j].append(pre_sum)
        q=len(B)#no. of querries
        ans=[]
        for i in range(q):
            top_row, left_col = B[i]-1, C[i]-1

            bottom_row, right_col = D[i]-1, E[i]-1

            if top_row > 0 and left_col > 0:
                ans.append((col_hash_map[right_col][bottom_row] - 
                          col_hash_map[right_col][top_row-1] - 
                          col_hash_map[left_col-1][bottom_row] + 
                          col_hash_map[left_col-1][top_row-1])%(10**9+7))
            elif top_row == 0 and left_col > 0:
                ans.append((col_hash_map[right_col][bottom_row] - 
                          col_hash_map[left_col-1][bottom_row])%(10**9+7))
            elif left_col == 0 and top_row > 0:
                ans.append((col_hash_map[right_col][bottom_row] - 
                          col_hash_map[right_col][top_row-1])%(10**9+7))
            else:  # both top_row == 0 and left_col == 0
                ans.append((col_hash_map[right_col][bottom_row])%(10**9+7))
        return ans
