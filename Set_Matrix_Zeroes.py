matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
m, n = len(matrix), len(matrix[0])
result = [[1] * n for i in range(m)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            for k in range(len(result[i])):
                result[i][k] = 0
            for k in range(len(matrix)):
                result[k][j] = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if result[i][j] == 0:
            matrix[i][j] = result[i][j]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if 