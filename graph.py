
from node import Node
import copy


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def listRemoveDuplicates(self, originalList):
        newList = list( dict.fromkeys(originalList))
        return newList


    def graphColouring(self):

        allColours = ["red","blue","green","yellow","orange","pink","purple","turquoise", "black", "grey", "silver", "lime", "teal", "navy", "salom"]
        totalUsedColours = set()
        
        self.nodes[0].colour = allColours[0]

        for node in self.nodes:
            usedColours = []
            availableColours = copy.deepcopy(allColours)
           
            if node == self.nodes[0]:
                continue
            
            for edgeNode in node.edges:
                
                if edgeNode.colour == "none":
                    continue
                else:
                    usedColours.append(edgeNode.colour)
                   
            usedColours = self.listRemoveDuplicates(usedColours)
            for colours in usedColours:
                availableColours.remove(colours)

            node.colour = availableColours[0]
            totalUsedColours.add(node.colour)
            totalUsedColours.update(usedColours)
        
        return len(totalUsedColours)
            

        
        

            



        
    


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

