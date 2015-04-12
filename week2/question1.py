# In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering. Download the text file clustering1.txt. This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:
# [number_of_nodes] 500
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
# ...

# Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

# The answer for question 1 is 106
import pandas as pd
from Cluster import Node, Edge, UnionFind

def loadData():
    df = pd.read_csv('clustering1.txt', sep=' ', header=0)
    df = df.sort(columns="cost", ascending=False, axis=0)
    nodes = []
    edges = []
    for i in range(500):
        node = Node(i+1)
        nodes.append(node)
        unionfind = UnionFind(node.getNumber(), node)
        node.setUnionfind(unionfind)
    for row in df.iterrows():
        edge = Edge(row[1].cost, nodes[row[1].node1-1], nodes[row[1].node2-1])
        edges.append(edge)
    return nodes, edges

#nods, edges are return values of loadData(), k=4
def doCluster(nodes, edges, k):
    """space is the answer for this question"""
    count = len(nodes)
    while count > k:
        edge = edges.pop()
        node1, node2 = edge.getNodes()
        if node1.getUnionFind().getLabel() != node2.getUnionFind().getLabel():
            node1.getUnionFind().merge(node2.getUnionFind())
            newuf = node1.getUnionFind()
            for node in newuf.getMembers():
                node.setUnionfind(newuf)
            count = count - 1
    while len(edges) > 0:
        edge = edges.pop()
        node1, node2 = edge.getNodes()
        if node1.getUnionFind().getLabel() != node2.getUnionFind().getLabel():
            space = edge.getCost()
            return space

