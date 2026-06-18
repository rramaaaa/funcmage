from collection.abc import Callable
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        if operation == "add":
            added = operation.add(spells)
            return added
        elif operation == "multiply":
            multi = operatrion.multiply(spells)
            return multi
        elif operation == "max":
            ma = operatrion.max(spells)
            return ma
        elif operation == "min":
            mi = operation.min(spells)
            return mi
        else:
            reduce = functools.reduce(spells)
            return reduce
    else:
        return 0


#def partial_enchanter(base_enchantment: Callable) -> int:


def spell_dispatcher() -> Callble[[Any], str]:
    def fibonacci(num: int) -> int:
        return num * fibonacci(num - 1)


