# In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.
# The data set is here. The format is:
# [# of nodes] [# of bits for each node's label]
# [first bit of node 1] ... [last bit of node 1]
# [first bit of node 2] ... [last bit of node 2]
# ...
# For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

# The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

# The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

# NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?
# 200000 24
# the answer for this question is 6118
# import question2 as q2
# dic = q2.loadDataAsDict()
# count = q2.doCluster(dic)

import pandas as pd
import numpy as np
from Cluster import Node, UnionFind

def loadDataAsDict():
    df = pd.read_csv("clustering_big.txt", sep=" ")
    value = pd.Series(data=np.zeros(shape=len(df)))
    for col, series in df.iteritems():
        value = value*2 + series
    data = np.array(value, dtype=np.int64)
    return buildDict(data)

def buildDict(data):
    dic = {}
    for key in data:
        if not dic.has_key(key):
            dic[key] = Node(key)
            unionfind = UnionFind(dic[key].getNumber(), dic[key])
            dic[key].setUnionfind(unionfind)
    return dic

def doCluster(dic):
    """cluster the nodes with distance less than 3"""
    count = len(dic.keys())
    for key in dic:
        for i in range(24):
            one_bit_res = 1<<i
            target = key^one_bit_res
            if dic.has_key(target) and dic[key].getUnionFind().getLabel() != dic[target].getUnionFind().getLabel():
                uf1 = dic[key].getUnionFind()
                uf2 = dic[target].getUnionFind()
                if len(uf2.getMembers()) > len(uf1.getMembers()):
                    uf1, uf2 = uf2, uf1
                for node in uf2.getMembers():
                    node.setUnionfind(uf1)
                uf1.merge(uf2)
                count = count - 1
    for key in dic:
        for i in range(24):
            for j in range(i):
                two_bit_res = 1<<i|1<<j
                target = key^two_bit_res
                if dic.has_key(target) and dic[key].getUnionFind().getLabel() != dic[target].getUnionFind().getLabel():
                    uf1 = dic[key].getUnionFind()
                    uf2 = dic[target].getUnionFind()
                    if len(uf2.getMembers()) > len(uf1.getMembers()):
                        uf1, uf2 = uf2, uf1
                    for node in uf2.getMembers():
                        node.setUnionfind(uf1)
                    uf1.merge(uf2)
                    count = count - 1
    return count
