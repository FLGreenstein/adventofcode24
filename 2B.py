def is_safe(levels):
    is_increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return is_increasing or is_decreasing

def is_safe_with_dampener(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    return False

with open("puzzleInput.txt", "r") as file:
    lines = file.readlines()

total_valid = 0

for line in lines:
    levels = list(map(int, line.split()))
    if is_safe(levels) or is_safe_with_dampener(levels):
        total_valid += 1
        print("V")

print(total_valid)
