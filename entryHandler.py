#  takes the entries and makes them nodes
from node import Node

class EntryHandler():
    def __init__(self, entries):
        self.entries = entries
    
    def createNodes(self):
        nodeList = []



        for counter, entry in enumerate(self.entries):
            node = Node(counter)
            node.data = entry
            node.label = node.data.subject
            node.title = node.data.profName
            nodeList.append(node)

        return nodeList
