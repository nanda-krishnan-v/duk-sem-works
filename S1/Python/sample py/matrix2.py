matrix = [
    [2,3,1,4],
    [5,14,11,8],
    [9,22,26,3],
    [4,5,6,7]
]
def add_borders(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[1 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            new_matrix[i + 1][j + 1] = matrix[i][j]
    return new_matrix
new_matrix = add_borders(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nMatrix with Borders of 1:")
for row in new_matrix:
    print(row)