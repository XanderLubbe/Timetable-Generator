from tableGenerator import TableGenerator
from edgeHandler import EdgeHandler
from entryHandler import EntryHandler
from dataHandler import DataHandler
from graphDrawer import GraphDrawer
from node import Node
from graph import Graph


myNode1 = Node(1)
myNode2 = Node(2)
myNode3 = Node(3)
myNode4 = Node(4)
myNode5 = Node(5)
myNode6 = Node(6)

myNode1.edges = [myNode2,myNode4,myNode5]
myNode2.edges = [myNode1,myNode3]
myNode3.edges = [myNode2]
myNode4.edges = [myNode1,myNode5,myNode6]
myNode5.edges = [myNode4,myNode1]
myNode6.edges = [myNode4]

nodeArr = [myNode1, myNode2, myNode3, myNode4, myNode5, myNode6]

# myGraph = Graph(nodeArr)
# myGraph.graphColouring()

# drawGraph = GraphDrawer(nodeArr)
# drawGraph.draw()

dataHandler = DataHandler('mockData.csv')
entryData = dataHandler.createEntries()

entryHandler = EntryHandler(entryData)
nodeData = entryHandler.createNodes()

edgeHandler = EdgeHandler(nodeData)
edgeHandler.createEdges()

myGraph = Graph(nodeData)
myGraph.graphColouring()

myTableGen = TableGenerator(nodeData)
myTableGen.generateTable()

drawGraph = GraphDrawer(nodeData)
drawGraph.draw()



