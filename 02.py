from collections import Counter

with open("02.txt") as f:
    raw_data = f.read()
counter = Counter(raw_data)
data = raw_data.split("\n")

wins = draws = looses = 0

for row in data:
    match row:
        case "A X":
            draws += 1
        case "A Y":
            wins += 1
        case "A Z":
            looses += 1
        case "B X":
            looses += 1
        case "B Y":
            draws += 1
        case "B Z":
            wins += 1
        case "C X":
            wins += 1
        case "C Y":
            looses += 1
        case "C Z":
            draws += 1

points_from_figures = counter["X"] + 2 * counter["Y"] + 3 * counter["Z"]
points_from_games = 6 * wins + 3 * draws

# Part A - final result
print(points_from_games + points_from_figures)

# Part B
convert = {
    "A X": 3 + 0,  # Scissors + lost
    "A Y": 1 + 3,  # Rock + draw
    "A Z": 2 + 6,  # Paper + win
    "B X": 1 + 0,  # Rock + lost
    "B Y": 2 + 3,  # Paper + draw
    "B Z": 3 + 6,  # Scissors + win
    "C X": 2 + 0,  # Paper + lost
    "C Y": 3 + 3,  # Scissors + draw
    "C Z": 1 + 6,  # Rock + win
}
results = [convert[pair] for pair in data]
print(sum(results))
