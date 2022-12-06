from dataclasses import dataclass
from typing import Tuple

with open("04.txt") as f:
    lines = f.read().split()


@dataclass
class CustomRange:
    low: int
    top: int


def convert(r: str) -> CustomRange:
    a, b = r.split("-")
    return CustomRange(int(a), int(b))


def a_fully_in_b(a: CustomRange, b: CustomRange):
    return a.low <= b.low and a.top >= b.top


count = 0
for line in lines:
    first, second = [convert(item) for item in line.split(",")]
    if a_fully_in_b(first, second) or a_fully_in_b(second, first):
        count += 1

# Part A
print(count)


# Part B
def a_partially_in_b(a: CustomRange, b: CustomRange):
    return a.top >= b.low and a.low <= b.top


count = 0
for line in lines:
    first, second = [convert(item) for item in line.split(",")]
    if a_partially_in_b(first, second) or a_partially_in_b(second, first):
        count += 1

print(count)
