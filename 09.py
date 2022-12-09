from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

with open("input/09.txt") as f:
    lines = f.read().split("\n")


@dataclass
class Move:

    def __init__(self, line: str):
        items = line.split()
        self.direction = items[0]
        self.distance = int(items[1])


@dataclass
class Point:
    x: int
    y: int

    def move(self, direction: str):
        if direction == "U":
            self.x += 1
        elif direction == "R":
            self.y += 1
        elif direction == "D":
            self.x -= 1
        elif direction == "L":
            self.y -= 1
        else:
            raise ValueError("Undefined direction")

    def distance(self, other: Point):
        x_distance = abs(self.x - other.x)
        y_distance = abs(self.y - other.y)
        return max(x_distance, y_distance)

    def is_far_from(self, other: Point):
        return self.distance(other) > 1

    def follow(self, other: Point, movement: Move):
        if other.is_far_from(self):
            if movement.direction in ["D", "U"]:
                self.y = other.y
            if movement.direction in ["R", "L"]:
                self.x = other.x
            self.move(direction=movement.direction)

    def to_tuple(self) -> Tuple[int, int]:
        return self.x, self.y


moves: List[Move] = [Move(line) for line in lines]
tail_positions: List[Tuple[int, int]] = []

H = Point(0, 0)
T = Point(0, 0)
tail_positions.append((T.x, T.y))

for move in moves:
    for _ in range(move.distance):
        H.move(move.direction)
        T.follow(H, movement=move)
        tail_positions.append((T.x, T.y))

# Part A
print(len(set(tail_positions)))

# Part B
tail_positions.clear()
Rope = [Point(0, 0) for _ in range(10)]
rope_length = len(Rope) - 1
H = Rope[0]
Tail = Rope[-1]

for move in moves:
    # print(f"Moving to {move.direction} for {move.distance}:")
    for move_index in range(move.distance):
        H.move(direction=move.direction)
        for index in range(rope_length):
            B = Rope[index]
            T = Rope[index + 1]
            T.follow(B, movement=move)
        # print(f"\tMove {move.direction} completed ({move_index + 1}/{move.distance}).")
        if (tail_pos := Tail.to_tuple()) not in tail_positions:
            tail_positions.append(tail_pos)

# print("-"*40)
print(tail_positions)
