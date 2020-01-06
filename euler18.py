def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    # base case
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    # recursive case
    else: return recSumAtRow(rowData, rowNum-1)
	
rows = []
with open('triangle.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
result = recSumAtRow(rows, len(rows)-2)

print(result)