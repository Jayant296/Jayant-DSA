'''
Problem Description

Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    # @param A : list of integers
    # @return an integer

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def bit_length(self, n):
        if n == 0:
            return 0
        count = 0
        while n:
            count += 1
            n >>= 1
        return count

    def DectoBin(self, num, length):
        bin_string = ''
        size = 0
        while size < length:
            if num == 0:
                bin_string += '0'
                size += 1
                continue
            rem = num % 2
            num >>= 1
            bin_string += str(rem)
            size += 1
        return bin_string[::-1]
    def XOR(self, num):
        node = self.root
        xor_string = ''
        for digit in num:
            if digit == '0':
                if '1' in node.children:
                    node = node.children['1']
                    xor_string += '1'
                else:
                    node = node.children['0']
                    xor_string += '0'
            else:
                if '0' in node.children:
                    node = node.children['0']
                    xor_string += '1'
                else:
                    node = node.children['1']
                    xor_string += '0'
        if xor_string == '':
            return 0
        '''
        xor = 0
        i = 0
        for val in range(len(xor_string)-1, -1, -1):
            xor += int(xor_string[val]) * (2**i)
            i += 1
        CAN WRITE THIS PART AS SIMPLY
        xor = int(string, base)
        '''
        xor = int(xor_string, 2)
        return xor

    def solve(self, A):
        if not A:
            return 0
        max_ele = max(A)
        length = self.bit_length(max_ele)
        new_list = []
        for num in A:
            new_list.append(self.DectoBin(num, length))
        for digit in new_list:
            self.insert(digit)
        ans = float('-inf')
        for digit in new_list:
            ans = max(ans, self.XOR(digit))
        return ans