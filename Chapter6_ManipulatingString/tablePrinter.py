tableData1 = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(tableData):

    colWidths = [0] * len(tableData)

    # Find the longest string in each of the inner list and Store the maximum width of each column as a list of intergers
    for i in range(len(tableData)):
        for word in tableData[i]:
            colWidthValue = colWidths[i]
            if colWidthValue == i:
                colWidths[i] = len(word)
            else:
                if colWidthValue < len(word):
                    colWidths[i] = len(word)
            
    # Generate Table
    outputTable = []
    outputCol = []
    for i in range(len(tableData)):
        for word in tableData[i]:
            outputCol.append(word.rjust(colWidths[i]))  
        outputTable.append(list(outputCol))
        outputCol.clear()
    
    # Rearrange the content in the table for easy display
    result = [[],[],[],[]]
    for x in range(len(outputTable)): 
        for y in range(len(outputTable[x])):
            result[y].append(outputTable[x][y])
    
    # Print table
    for x in range(len(result)):
        for y in range(len(result[x])):
            print(result[x][y], end=' ')
        print()

printTable(tableData1)