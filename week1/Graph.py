class Node(object):

    def __init__(self, id, *edges):
        self.id = id
        self.edges = []
        for edge in edges:
            self.__edges.append(edge)
        self.__isProcessed = False

    def addEdge(self, edge):
        self.edges.append(edge)
        return self

    def getEdges(self):
        return self.edges

    def processed(self):
        self.__isProcessed = True
        return self

    def isProcessed(self):
        return self.__isProcessed

class Edge(object):

    def __init__(self, cost, one_node, other_node):
        self.__cost = cost
        self.__endPoints = (one_node, other_node)

    def isInvalid(self):
        return self.__endPoints[0].isProcessed() and self.__endPoints[1].isProcessed()

    def getCost(self):
        return self.__cost

    def getVertexs(self):
        vertex = []
        for node in self.__endPoints:
            vertex.append(node.id)
        return vertex

    def processed(self):
        self.__endPoints[0].processed()
        self.__endPoints[1].processed()
