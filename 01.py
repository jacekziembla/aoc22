with open("01.txt") as f:
    data = f.read().split("\n\n")

elves = [list(map(int, item.split())) for item in data]
sums = [sum(items) for items in elves]

# Max
print(max(sums))

# Sum of top free
print(sum(sorted(sums)[-3:]))
