import re

def calculate_total_with_conditions():
    total = 0
    mul_enabled = True
    pattern = r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)'

    with open('puzzleInput.txt', 'r') as file:
        content = file.read()
        matches = re.finditer(pattern, content)

        for match in matches:
            if match.group(0) == "do()":
                mul_enabled = True
            elif match.group(0) == "don't()":
                mul_enabled = False
            elif "mul(" in match.group(0):
                if mul_enabled:
                    num1, num2 = map(int, match.groups())
                    total += num1 * num2
    return total

total = calculate_total_with_conditions()
print(total)
