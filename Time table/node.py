class Node:
    def __init__(self, nodeID, edgeID, colour):
        self.nodeID = nodeID
        self.edgeID = edgeID
        self.colour = colour

node1 = Node(1,[(1,2),(1,5)], "none")


print(node1.colour)