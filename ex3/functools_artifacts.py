from collections.abc import Callable
from functools import reduce, partial
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) != 0:
        if operation == "add":
            return reduce(lambda x, y: x + y, spells)
        if operation == "multiply":
            return reduce(lambda x, y: x * y, spells)
        if operation == "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        if operation == "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        else:
            raise KeyError("Unknown operation")
    else:
        return 0

nums = [1, 2, 3, 4, 5]
print("Testing spell reducer...")
print(f"Sum: {spell_reducer(nums, "add")}")
print(f"Product: {spell_reducer(nums, "multiply")}")
print(f"Max: {spell_reducer(nums, "max")}")
print(f"Min: {spell_reducer(nums, "min")}")
print()

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    partial_power = partial(base_enchantment, 50)
    partial_element = partial(base_enchantment, element = "Fire")
    partial_target = partial(base_enchantment, target = "Dragone")

    return {"power": partial_power, "element": partial_element, "target": partial_target}


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"The power for {element} {target} is {power}"


part = partial_enchanter(base_enchantment)
print(part["power"]("yes", "no"))
print(part["target"](10, "Fire"))
print(part["element"](10, "one"))





#def base_enchantment(power: int, element: str, target: str) -> str:
