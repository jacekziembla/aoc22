with open("05.txt") as f:
    data = f.read()

cargo_input, moves_raw_input = data.split("\n\n")
cargo_input_lines = cargo_input.split("\n")
cargo_from_bottom = cargo_input_lines[::-1][1:]
stack_indexes = cargo_input_lines[-1].split()
moves_input = moves_raw_input.split("\n")[:-1]

STACKS_COUNT = len(stack_indexes)
STACKS_LEVELS = len(cargo_input_lines) - 1

# Initial state
stacks = {index: [] for index in stack_indexes}
for level in cargo_from_bottom:
    for i in range(STACKS_COUNT):
        current_stack = stacks[str(i + 1)]
        container: str = level[4 * i + 1]
        if not container.isspace():
            current_stack.append(container)

# Perform moves
for line in moves_input:
    move = line.split()
    how_many = int(move[1])
    from_stack = stacks[move[3]]
    to_stack = stacks[move[5]]
    for _ in range(how_many):
        to_stack.append(from_stack.pop())


# Part A
result = "".join([stacks[index][-1] for index in stack_indexes])
print(result)


# Part B

# restore initial state
stacks = {index: [] for index in stack_indexes}
for level in cargo_from_bottom:
    for i in range(STACKS_COUNT):
        current_stack = stacks[str(i + 1)]
        container: str = level[4 * i + 1]
        if not container.isspace():
            current_stack.append(container)

# perform moves
for line in moves_input:
    move = line.split()
    how_many = int(move[1])
    from_stack = stacks[move[3]]
    to_stack = stacks[move[5]]
    temp_stack = []
    for _ in range(how_many):
        temp_stack.append(from_stack.pop())
    for container in temp_stack[::-1]:
        to_stack.append(container)

result = "".join([stacks[index][-1] for index in stack_indexes])
print(result)