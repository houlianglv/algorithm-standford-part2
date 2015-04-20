class Edge(object):
    """Edge class. Edge maintains the tail Node and head Node, and the cost"""
    def __init__(self, tail, head, cost):
        self.tail = tail
        self.head = head
        self.cost = cost
