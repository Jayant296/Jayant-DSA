'''
Docstring for coloring_a_cyclic_graph
Problem Description

Given the number of vertices A in a Cyclic Graph.
Your task is to determine the minimum number of colors required to color the graph so that no two Adjacent vertices have the same color.
A cyclic graph with A vertices is a graph with A edges, such that it forms a loop. See example test case explanation for more details.

'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        if A % 2 == 0:
            return 2
        else:
            return 3
