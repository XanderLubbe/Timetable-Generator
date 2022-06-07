from cProfile import label
from turtle import title


class Node:
    def __init__(self, nodeID):
        self.nodeID = nodeID
        self.label = label
        self.title = title
        self.edges = set()
        self.colour = "none"
        self.data = []

    def __str__(self):
        return str(self.nodeID)

    def __repr__(self):
        return str(self.nodeID)







