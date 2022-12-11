from __future__ import annotations
from typing import List

with open("input/11.txt") as f:
    lines = f.read().replace("* old", "^ 2").split("\n")

PART_B = True  #

if PART_B:
    modifier = lambda x: x % Monkey.product
    ROUNDS = 10000
else:
    modifier = lambda x: int(x / 3)
    ROUNDS = 20


class Monkey:
    product = 1

    def __init__(self, items: List[int], operator: str, value: int, test_value: int, if_true: int, if_false: int):
        self.items = items
        self.operator = operator
        self.operator_value = value
        self.test_value = test_value
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0

    def operation(self, item: int) -> int:
        if self.operator == "+":
            new_item = item + self.operator_value
        elif self.operator == "*":
            new_item = item * self.operator_value
        elif self.operator == "^":
            new_item = item * item
        else:
            raise ValueError
        return modifier(new_item)

    def test(self, item: int) -> bool:
        return item % self.test_value == 0

    def inspect_and_throw(self, targets: List[Monkey]):
        item = self.operation(item=self.items.pop(0))
        if self.test(item):
            target = targets[self.if_true]
        else:
            target = targets[self.if_false]
        target.items.append(item)
        self.counter += 1


number_of_monkeys = int(len(lines) / 7)
monkeys: List[Monkey] = []
for monkey_index in range(number_of_monkeys):
    monkeys.append(Monkey(
        items=[int(item) for item in lines[7 * monkey_index + 1].split(": ")[1].split(", ")],
        operator=lines[7 * monkey_index + 2].split("old ")[1][0],
        value=int(lines[7 * monkey_index + 2].split()[-1]),
        test_value=int(lines[7 * monkey_index + 3].split()[-1]),
        if_true=int(lines[7 * monkey_index + 4].split()[-1]),
        if_false=int(lines[7 * monkey_index + 5].split()[-1])
    ))
    Monkey.product *= int(lines[7 * monkey_index + 3].split()[-1])

for _ in range(ROUNDS):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey.inspect_and_throw(monkeys)

# Result
counters = sorted([i.counter for i in monkeys])
print(counters.pop() * counters.pop())
