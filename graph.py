
from node import Node


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def listDifference(list1, list2):
        newList = list(set(list1) - set(list2)) + list(set(list2) -set(list1))
        print(newList)
        return newList

    def listRemoveDuplicates(originalList):
        newList = list( dict.fromkeys(originalList))
        print(newList)
        return newList


    def graphColouring(self):

        availableColours = ["red","blue","green","yellow","orange","pink","purple","turquoise"]
        nodesLength =  len(self.nodes)
        
        self.nodes[0].colour = availableColours[0]
        
        usedColours = []

        for node in self.nodes:
           
            if node == self.nodes[0]:
                continue
            
            for edgeNode in node.edges:
                
                if edgeNode.colour == "none":
                    continue
                else:
                    usedColours.append(edgeNode.colour)
                   
            usedColours = Graph.listRemoveDuplicates(usedColours)
            for colours in usedColours:
                availableColours.remove(colours)

            node.colour = availableColours[0]
            availableColours = ["red","blue","green","yellow","orange","pink","purple","turquoise"]
            usedColours = []
        
        

            



        
    


    def getAllNodes():
        print()
    
    def getAllEdges():
        print()
    
    def findShortestPath():
        print()
    
   

        # Need to set to rules given
        maxColours = 10
        
            # Go to first node and set to anything
            # Go to the next node and check if any of its edges are conected to a coloured node
                # If yes add the coloured node's ID to a nodeWithColor array
                # Go to next edge neighbour and see if is coloured
                    # If yes add it to nodeWithColor array and so on
                    # If no go to next edge and so on
                # After all edges are visted, their node's colours recorded, set node's colour to one that isn't in the array and reset array
            # Go to next node and continue pattern till all nodes are visited and their colours set
            # Check at the end that all colours chosen do not violate rules

