'''
Problem Description

Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .

Conditions for a string to be balanced :

Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.
'''
class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        mapping = {'(':')','[':']','{':'}'}
        max_length = 0
        stack = [-1]
        for i in range(len(A)):
            if A[i] in mapping:
                stack.append(i)
            else:
                if len(stack) > 1 and A[i] == mapping.get(A[stack[-1]]): # .get for handling the cases like )}] , it will simply return none in place of an error.
                    stack.pop()
                    max_length = max(max_length,i - stack[-1])
                else:
                    stack.append(i)
            
        return max_length  


