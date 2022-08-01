from tableGenerator import TableGenerator
from edgeHandler import EdgeHandler
from entryHandler import EntryHandler
from dataHandler import DataHandler
from graphDrawer import GraphDrawer
from node import Node
from graph import Graph
import copy
import random
import math





dataHandler = DataHandler('mockData.csv')
entryData = dataHandler.createEntries()

entryHandler = EntryHandler(entryData)
nodeData = entryHandler.createNodes()

# For testing purposes, the results were taken form 100 runs to find the most efficient starting point

# testQuantity = 100
# bestResult = None
# leastUsedColours = math.inf

# for i in range(testQuantity):
#     tempNodes = copy.deepcopy(nodeData)
#     random.shuffle(tempNodes)
#
#     edgeHandler = EdgeHandler(tempNodes)
#     edgeHandler.createEdges()
#
#     myGraph = Graph(tempNodes)
#     colourCount = myGraph.graphColouring()
#
#     if i == 0 or colourCount < leastUsedColours:
#         bestResult = tempNodes
#         leastUsedColours = colourCount

edgeHandler = EdgeHandler(nodeData)
edgeHandler.createEdges()

myGraph = Graph(nodeData)
myGraph.graphColouring()

myTableGen = TableGenerator(nodeData)
myTableGen.generateTable()

drawGraph = GraphDrawer(nodeData)
drawGraph.draw()

# print(leastUsedColours)


