def transpose_matrix(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  transpose = [[0] * rows for _ in range(cols)]

  for i in range(rows):
    for j in range(cols):
      transpose[j][i] = matrix[i][j]

  return transpose

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)

print("Original matrix:")
for row in matrix:
  print(row)

print("\nTransposed matrix:")
for row in transposed_matrix:
  print(row)