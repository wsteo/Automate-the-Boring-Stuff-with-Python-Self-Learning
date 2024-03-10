def printTable(tableData):

    colWidths = [0] * len(tableData)

    # Find the longest string in each of the inner list and Store the maximum width of each column as a list of intergers
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            longestWordWidth = colWidths[i]
            wordWidth = tableData[i][j]
            if longestWordWidth == i:
                colWidths[i] = len(wordWidth)
            else:
                if longestWordWidth < len(wordWidth):
                    colWidths[i] = len(wordWidth)
            
    # Generate Table
    outputTable = []
    outputCol = []
    for i in range(len(tableData)):
        for word in tableData[i]:
            outputCol.append(word.rjust(colWidths[i]))  
        outputTable.append(list(outputCol))
        outputCol.clear()
    
    # Rearrange the content in the table for easy display
    result = []

    for y in range(len(outputTable[0])):
        result.append([])

    for x in range(len(outputTable)): 
        for y in range(len(outputTable[x])):
            result[y].append(outputTable[x][y])
    
    # Print table
    for x in range(len(result)):
        for y in range(len(result[x])):
            print(result[x][y], end=' ')
        print()

tableData1 = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

tableData2 = [['apple', 'oranges', 'cherries', 'banana', 'grape'],
              ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
              ['dogs', 'cats', 'moose', 'goose', 'sheep'],
              ['elephant', 'giraffe', 'lion', 'tiger', 'zebra']]

printTable(tableData1)
printTable(tableData2)