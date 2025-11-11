'''
Problem Description

Given an array of words A (dictionary) and another array B (which contain some words).

You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.

Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if not.

Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.

NOTE: Try to do this in O(n) time complexity.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root # initialize
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return 1 if node.is_end else 0

    def solve(self, A, B):
        ans = []
        for word in A: # trie creation
            self.insert(word) 
        for word in B: # searching for words in trie
            ans.append(self.search(word))
        return ans

