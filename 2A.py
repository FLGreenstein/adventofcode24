with open("puzzleInput.txt", "r") as file:
    lines = file.readlines()

totalValid = 0

for line in lines:
    levels = list(map(int, line.split()))
    is_increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    
    if is_increasing or is_decreasing:
        totalValid += 1
        print("V")

print(totalValid)
