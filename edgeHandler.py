# create edges for the nodes 


class EdgeHandler:
    def __init__(self, nodes):
        self.nodes = nodes
    
    def createEdges(self):
        # Checking professors here to create edges
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
        # Checking degrees here to create edges        
        for node in self.nodes:

            currentDegreeName = node.data.degree
            currentDegree = node
            currentNodeId = node.nodeID

            for counter, degree in enumerate(self.nodes):

                if counter == int(currentNodeId):
                    continue
                
                if degree.data.degree == currentDegreeName:
                    currentDegree.edges.add(degree)
                    degree.edges.add(currentDegree)

        



