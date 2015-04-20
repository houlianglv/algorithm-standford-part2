class Node(object):
    """Node of Graph, contain an array of edges whose tail is this Node"""
    def __init__(self, node_id):
        self.node_id = node_id
        self.in_edge_array = []
        self.out_edge_array = []
    def add_in_edge(self, edge):
        """get the array contains in-coming edges"""
        self.in_edge_array.append(edge)
    def add_out_edge(self, edge):
        """get the array contains out-going edges"""
        self.out_edge_array.append(edge)

class Edge(object):
    """Edge class. Edge maintains the tail Node and head Node, and the cost"""
    def __init__(self, tail, head, cost):
        self.tail = tail
        self.head = head
        self.cost = cost
