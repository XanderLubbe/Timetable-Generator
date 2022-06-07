from platform import node
from node import Node
from pyvis.network import Network
import networkx as nx



class GraphDrawer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.nt = Network('500px', '500px')

    def generateNodes(self):
        for item in self.nodes:
            self.nt.add_node(item.nodeID, size=20, color=item.colour, label = item.label, title = item.title)

    def generateEdges(self):
        for node in self.nodes:
            for edgeNode in node.edges:
                self.nt.add_edge(node.nodeID, edgeNode.nodeID)
    
    def draw(self):
        self.generateNodes()
        self.generateEdges()
        self.nt.toggle_physics(True)
        self.nt.show('mygraph.html')




    