# In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files describing three graphs: graph #1; graph #2; graph #3.
# number_nodes edges
# 1000 47978
# The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

# Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one

# If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

# OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

# OPTIONAL: If you want a bigger data set to play with, try computing the shortest shortest path for this graph.
import pandas as pd
import numpy as np
from Graph import Edge

def load_data(file_name):
    """load graph data from file"""
    graph = pd.read_csv(file_name, header=0, sep=' ')
    graph_edges = []
    for index, row in graph.iterrows():
        edge = Edge(row["tail"], row["head"], row["cost"])
        graph_edges.append(edge)
    return graph_edges

def floyd_warshall(number_of_nodes, graph_edges):
    """do floyd warshall algorithm"""
    size_of_array = number_of_nodes + 1
    array = np.empty(shape=(size_of_array, size_of_array, 2))
    array.fill(np.PINF)
    for edge in graph_edges:
        array[edge.tail, edge.head, 0] = edge.cost
    for i in range(1, size_of_array):
        array[i, i, 0] = 0
    for k in range(1, size_of_array):
        for i in range(1, size_of_array):
            for j in range(1, size_of_array):
                array[i, j, 1] = min(array[i, j, 0], array[i, k, 0] + array[k, j, 0])
                if i == j and array[i, j, 1] < 0:
                    print "negative circle detected!", "i=", i, "j=", j, "k=", k
                    return np.array([])
        array[:, :, 0] = array[:, :, 1]
    return array[:, :, 0]












