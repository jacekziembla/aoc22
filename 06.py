from collections import Counter

with open("06.txt") as f:
    stream = f.read()

BUFFER_SIZE = 4

# PART A
for index in range(len(stream) - BUFFER_SIZE):
    packet = stream[index:index + BUFFER_SIZE]
    if len(Counter(packet).keys()) == BUFFER_SIZE:
        print(index+BUFFER_SIZE)
        break

# PART B
BUFFER_SIZE = 14
for index in range(len(stream) - BUFFER_SIZE):
    packet = stream[index:index + BUFFER_SIZE]
    if len(Counter(packet).keys()) == BUFFER_SIZE:
        print(index+BUFFER_SIZE)
        break