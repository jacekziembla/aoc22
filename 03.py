from collections import Counter

with open("input/03.txt") as f:
    lines = f.read().split()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = {char: index + 1 for index, char in enumerate(letters)}

duplicates = []
for line in lines:
    duplicates.append((set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop())

results = [values[letter] for letter in duplicates]

# Part A
print(sum(results))

# Part B
duplicates = []
for index in range(int(len(lines) / 3)):
    duplicate = set(lines[3 * index]) & set(lines[3 * index + 1]) & set(lines[3 * index + 2])
    duplicates.append(duplicate.pop())

results = [values[letter] for letter in duplicates]
print(sum(results))
