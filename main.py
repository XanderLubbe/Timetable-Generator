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



testQuantity = 100

dataHandler = DataHandler('mockData.csv')
entryData = dataHandler.createEntries()

entryHandler = EntryHandler(entryData)
nodeData = entryHandler.createNodes()

bestResult = None
leastUsedColours = math.inf

for i in range(testQuantity):
    tempNodes = copy.deepcopy(nodeData)
    random.shuffle(tempNodes)

    edgeHandler = EdgeHandler(tempNodes)
    edgeHandler.createEdges()

    myGraph = Graph(tempNodes)
    colourCount = myGraph.graphColouring()  

    if i == 0 or colourCount < leastUsedColours:
        bestResult = tempNodes
        leastUsedColours = colourCount

myTableGen = TableGenerator(bestResult)
myTableGen.generateTable()

drawGraph = GraphDrawer(bestResult)
drawGraph.draw()

print(leastUsedColours)


