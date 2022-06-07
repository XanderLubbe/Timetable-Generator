

import csv


class TableGenerator:
    def __init__(self, nodes):
        self.nodes = nodes

    def generateTable(self):
        colorArray = ["red","blue","green","yellow","orange","pink","purple","turquoise", "black", "grey", "silver", "lime", "teal", "navy", "salom"]
        resultArray = []

        for colour in colorArray:
            arr = []

            for node in self.nodes:
                if node.colour == colour:
                    arr.append(node)

            if len(arr) > 0:
                resultArray.append(arr)
            print(colour)
            print(len(arr))

        with open('generatedTimetable.csv', 'w', encoding='UTF8', newline='') as f:
            header = ["Group", "Subjects in group"]
            writer = csv.writer(f)

            writer.writerow(header)

            for counter, item in enumerate(resultArray):
                groupName = str("Group " + str(counter))
                dataArr = []
                nameArr = []
                nameArr.append(groupName)

                for node in item:
                    data = node.data.subject
                    dataArr.append(data)
                dataToPush = nameArr + dataArr
                writer.writerow(dataToPush)


        
                

