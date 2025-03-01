rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements row by row (space-separated):")
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

print("\nInput Matrix:")
for row in matrix:
    print(row)
print()
print()    
    
transpose = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]
        
        
for i in transpose:
    print(i)