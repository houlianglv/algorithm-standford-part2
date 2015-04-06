# The answer is -3612829
# In this programming problem you'll code up Prim's minimum spanning tree algorithm.
# Download the text file here. This file describes an undirected graph with integer edge costs.
# It has the format
# [number_of_nodes] [number_of_edges]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
# ...
# For example, the third line of the file is "2 3 -8874",
# indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.
# You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

# Your task is to run Prim's minimum spanning tree algorithm on this graph.
# You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine.
# OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version.
# The simpler approach, which should already give you a healthy speed-up,
# is to maintain relevant edges in a heap (with keys = edge costs).
# The superior approach stores the unprocessed vertices in the heap,
# as described in lecture. Note this requires a heap that supports deletions,
# and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
import pandas as pd
import sys
from Graph import *

def loadGraph():
    number_of_nodes = 500
    data = pd.read_csv('edges.txt', sep=' ', header=0)
    graph = []
    edges = []
    for i in range(number_of_nodes):
        graph.append(Node(i+1))
    for iter in data.iterrows():
        row = iter[1]
        cost = row['cost']
        one_node_id = row['one_node']
        other_node_id = row['other_node']
        edge = Edge(cost, graph[one_node_id-1], graph[other_node_id-1])
        edges.append(edge)
        graph[one_node_id-1].addEdge(edge)
        graph[other_node_id-1].addEdge(edge)
    return graph, edges

def generateMST(graph):
    MST = []
    nodeInMST = []
    edgeToAdd = []
    startNode = graph[0]
    startNode.processed()
    edges = startNode.getEdges()
    edgeToAdd.extend(edges)
    nodeInMST.append(startNode)
    while(len(nodeInMST)<len(graph)):
        minCost = sys.maxint
        minEdge = None
        for edge in edgeToAdd:
            if edge.getCost() < minCost and not edge.isInvalid():
                # print edge.getCost()
                minCost = edge.getCost()
                minEdge = edge
        MST.append(minEdge)
        vertex = minEdge.getVertexs()
        for id in vertex:
            if not graph[id-1].isProcessed():
                nodeInMST.append(graph[id-1])
                graph[id-1].processed()
                edges = graph[id-1].getEdges()
                for edge in edges:
                    if not edge.isInvalid():
                        edgeToAdd.append(edge)
    return MST

def sum(mst):
    sum = 0
    for edge in mst:
        sum += edge.getCost()
    return sum

