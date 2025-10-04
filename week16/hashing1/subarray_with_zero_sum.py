# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        prefix_A = []
        Sum = 0
        for i in A:
            Sum += i
            prefix_A.append(Sum)
        frequency = dict()
        for i in prefix_A:
            if i == 0:
                return 1
            if i in frequency:
                return 1
            else:
                frequency[i] = 1
        return 0
