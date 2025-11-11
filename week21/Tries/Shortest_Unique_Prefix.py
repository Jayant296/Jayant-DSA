'''
Problem Description

Given a list of N words, find the shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.is_end = False

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def __init__(self):
        self.root = TrieNode()

    # insert
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.is_end = True
    
    # unique prefix of words
    def UniquePrefix(self, word):
        node = self.root
        pre_string = ''
        for ch in word:
            node = node.children[ch]
            if node.prefix_count == 1:
                pre_string += ch
                return pre_string
            pre_string += ch
        return pre_string

    def prefix(self, A):
        ans = []
        for word in A:
            self.insert(word)
        for word in A:
            ans.append(self.UniquePrefix(word))
        return ans