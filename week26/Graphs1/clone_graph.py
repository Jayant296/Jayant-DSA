'''
Docstring for clone_graph
Problem Description

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

Note: The test cases are generated in the following format (use the following format to use See Expected Output option):
First integer N is the number of nodes.
Then, N intgers follow denoting the label (or hash) of the N nodes.
Then, N2 integers following denoting the adjacency matrix of a graph, where Adj[i][j] = 1 denotes presence of an undirected edge between the ith and jth node, O otherwise.

'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        # using bfs
        queue = deque()
        queue.append(node)
        clone_map = dict()
        clone_map[node] = UndirectedGraphNode(node.label)

        while queue:
            element = queue.popleft()
            
            for nbr in element.neighbors:

                if nbr not in clone_map:
                    clone_map[nbr] = UndirectedGraphNode(nbr.label)
                    queue.append(nbr)

                clone_map[element].neighbors.append(clone_map[nbr])

        cloned_node = clone_map[node]
        return cloned_node
