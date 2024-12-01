with open("puzzleInput.txt", "r") as file:
    lines = file.readlines()

column1 = []
column2 = []

for line in lines:
    numbers = list(map(int, line.split()))
    column1.append(numbers[0])
    column2.append(numbers[1])

column1.sort()
column2.sort()

similarityScore = 0

for id in column1:
    similarityScore += (column2.count(id)*id)
    
print(similarityScore)
