def count_occurrences(grid, word):
    total = 0
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)

    for row_index, row in enumerate(grid):
        row_str = ''.join(row)
        horizontal_matches = row_str.count(word)
        total += horizontal_matches
        print(f"Row {row_index} horizontal: {horizontal_matches}")

    for col in range(cols):
        col_str = ''.join(grid[row][col] for row in range(rows))
        vertical_matches = col_str.count(word)
        total += vertical_matches
        print(f"Column {col} vertical: {vertical_matches}")

    for d in range(-rows + 1, cols):
        diag1 = ''.join(grid[i][i - d] for i in range(max(0, d), min(rows, cols + d)) if 0 <= i - d < cols)
        diag2 = ''.join(grid[i][cols - 1 - (i - d)] for i in range(max(0, d), min(rows, cols + d)) if 0 <= cols - 1 - (i - d) < cols)
        
        diag1_matches = diag1.count(word)
        diag2_matches = diag2.count(word)
        
        total += diag1_matches
        total += diag2_matches

        print(f"Diagonal {d} diag1: {diag1_matches}, diag2: {diag2_matches}")

    return total

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file if line.strip()]

grid = read_grid_from_file('puzzleInput.txt')
total_xmas = count_occurrences(grid, 'XMAS')
total_samx = count_occurrences(grid, 'SAMX')

print(f"Total XMAS: {total_xmas}, Total SAMX: {total_samx}")
print(f"Grand Total: {total_xmas + total_samx}")
