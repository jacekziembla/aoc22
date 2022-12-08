from typing import List

with open("input/08.txt") as f:
    lines = f.read().split("\n")

rows = []
for line in lines:
    row = [int(i) for i in line]
    rows.append(row)

columns = list(map(list, zip(*rows)))


def check(row: List[int], index):
    element = row[index]
    before = row[:index]
    if index != len(row):
        after = row[index + 1:]
    else:
        after = []
    return all([element > tree for tree in before]) or all([element > tree for tree in after])


pairs = []

for i, row in enumerate(rows):
    for j, column in enumerate(columns):
        if check(row, j) or check(column, i):
            pairs.append((i, j))

# Part A
pairs = list(set(pairs))
print(len(pairs))


# Part B
def calculate(row: List[int], index):
    element = row[index]
    before = row[:index]
    if index != len(row):
        after = row[index + 1:]
    else:
        after = []
    before_score = after_score = 1
    for tree in before[::-1]:
        if tree >= element:
            break
        before_score += 1
    for tree in after:
        if tree >= element:
            break
        after_score += 1
    if all([element > tree for tree in before]):
        before_score -= 1
    if all([element > tree for tree in after]):
        after_score -= 1
    return before_score * after_score


scores = []
for i, row in enumerate(rows):
    for j, column in enumerate(columns):
        scores.append(calculate(row, j) * calculate(column, i))

print(max(scores))
