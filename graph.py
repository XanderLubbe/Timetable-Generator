# Given nodeList (1,2,3,4,5,6)
# Given edgeList [(1,2),(2,3),(2,4),(2,5),(4,6)]

# Graph([1, 2, 3, 4, 5])

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes



    def graphColouring():
   

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

    