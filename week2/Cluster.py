class Node(object):
    """docstring for Node"""
    def __init__(self, number):
        self.__number = number
        self.__unionfind = None

    def getNumber(self):
        return self.__number

    def getUnionFind(self):
        return self.__unionfind

    def setUnionfind(self, unionfind):
        self.__unionfind = unionfind

class UnionFind(object):
    """docstring for UnionFind"""
    def __init__(self, label, node):
        self.__label = label
        self.__members = []
        self.__members.append(node)

    def getLabel(self):
        return self.__label

    def addMember(self, node):
        self.__members.append(node)

    def getMembers(self):
        return self.__members

    def merge(self, unionfind):
        members_to_merge = unionfind.getMembers()
        self_members = self.getMembers()
        self_members.extend(members_to_merge)
        members_to_merge = None
        unionfind = None

class Edge(object):
    """docstring for Edge"""
    def __init__(self, cost, *node):
        self.__cost = cost
        self.__nodes = node

    def getCost(self):
        return self.__cost

    def getNodes(self):
        return self.__nodes
