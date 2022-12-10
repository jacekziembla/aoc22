from typing import Optional, List

with open("input/10.txt") as f:
    lines = f.read().split("\n")


class Command:

    def __init__(self, command_type: str, value: str = None):
        self.type = command_type
        self.value = int(value) if value is not None else None


commands: List[Command] = [Command(*line.split()) for line in lines]

X = 1
counter = 1
register: List[int] = []


def add_to_register(c: int, v: int, reg: List[int]):
    if c in [20, 60, 100, 140, 180, 220]:
        reg.append(c * v)


for command in commands:
    if command.type == "addx":
        counter += 1
        add_to_register(counter, X, register)
        counter += 1
        X += command.value
        add_to_register(counter, X, register)
    elif command.type == "noop":
        counter += 1
        add_to_register(counter, X, register)
    else:
        raise ValueError(f"Command not found: {command.type}")

# Part A
print(sum(register))
