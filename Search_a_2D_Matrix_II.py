matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
column = len(matrix[0])
row = len(matrix)
for i in range(len(matrix[0])):
    if matrix[0][i] == target:
        print(True)
    if matrix[0][i] > target:
        column = i
        break
for i in range(len(matrix)):
        if matrix[i][0] == target:
            print(True)
        if matrix[i][0] > target:
            row = i
            break
print(row,column)
for i in reversed(range(row)):
    for j in reversed(range(column)):
            print(matrix[i][j])
            if matrix[i][j] < target:
                break
            if matrix[i][j] == target:
                print(True)
print(False)
