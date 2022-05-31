from node import Node
from graph import Graph


myNode1 = Node(1,[2,4,5],"none")
myNode2 = Node(2,[1,3],"none")
myNode3 = Node(3,[2],"none")
myNode4 = Node(4,[1,5,6],"none")
myNode5 = Node(5,[4,1],"none")
myNode6 = Node(6,[4],"none")
nodeArr = [myNode1, myNode2, myNode3, myNode4, myNode5, myNode6]



myGraph = Graph(nodeArr)

myGraph.graphColouring()