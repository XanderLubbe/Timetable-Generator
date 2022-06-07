# create edges for the nodes 


class EdgeHandler:
    def __init__(self, nodes):
        self.nodes = nodes
    
    def createEdges(self):

        for node in self.nodes:

            currentProfName = node.data.profName
            currentProf = node
            currentNodeId = node.nodeID

            for counter, profs in enumerate(self.nodes):

                if counter == int(currentNodeId):
                    continue
                
                if profs.data.profName == currentProfName:
                    currentProf.edges.add(profs)
                    profs.edges.add(currentProf)

        



