import re

def sum_all_multiplications():
    total = 0
    with open('puzzleInput.txt', 'r') as file:
        content = file.read()
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content)
        for match in matches:
            num1, num2 = map(int, match)
            total += num1 * num2
    return total

total = sum_all_multiplications()
print(total)
