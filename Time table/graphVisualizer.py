from platform import node
from pyvis.network import Network
import networkx as nx


    


nt = Network('500px', '500px')


nodeList = [1,2,3,4,5,6]
edgeList = [(1,2),(1,3),(1,4)]
labelList = ["Node 1","Node 2","Node 3","Node 4","Node 5","Node 6"]

myDict = [
    {
        "nodeID": 1,
        "label": "1",
        "edges": [(1,2),(1,4)],
    },
        {
        "nodeID": 2,
        "label": "2",
        "edges": [(2,1)],
    },
        {
        "nodeID": 3,
        "label": "3",
        "edges": [(1,2),(1,4)],
    },
        {
        "nodeID": 4,
        "label": "4",
        "edges": [(1,2),(1,4)],
    },
]


def generateNodes(listOfNodes):
    for item in listOfNodes:
        nt.add_node(item, size=20)

def generateEdges(listOfEgdes):
    for item in listOfEgdes:
        nt.add_edge(item[0], item[1])

def generateLabels(listOfLabels):
    for item in listOfLabels:
        print()
        

generateNodes(nodeList)
generateEdges(edgeList)

nt.toggle_physics(True)
nt.show('mygraph.html')