class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    '''
    LEARNING => IT'S COMBINATION TYPE, SO USE START INDEX & START CALL NEXT 
    FUNCTION FROM I+1 NOT FROM start_index + 1. 

    ''' 
    
    def gen(self, A, B, curr_arr, curr_index, start_index):
        n = len(A)
        if curr_index == B:
            Sum = 0
            for i in curr_arr:
                Sum += i
            if Sum <= 1000:
                return 1
            return 0
        count = 0
        for i in range(start_index,n):
            curr_arr[curr_index] = A[i]
            count += self.gen(A, B, curr_arr, curr_index+1, i+1)
        return count
    def solve(self, A, B):
        n = len(A)
        curr_arr = [0]*B
        return self.gen(A, B, curr_arr, 0, 0)
        