sudoku_matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Extract all 3x3 blocks into a list of 3x3 matrices
all_blocks = []
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        block_matrix = [row[j:j+3] for row in sudoku_matrix[i:i+3]]
        all_blocks.append(block_matrix)

# Print the resulting list of 3x3 block matrices
for block_matrix in all_blocks:
    for row in block_matrix:
        print(row)
    print()