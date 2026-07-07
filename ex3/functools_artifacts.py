from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) != 0:
        if operation == "add":
            return reduce(add, spells)
        if operation == "multiply":
            return reduce(mul, spells)
        if operation == "max":
            return max(spells)
        if operation == "min":
            return min(spells)
        else:
            raise KeyError("Unknown operation")
    else:
        return 0


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(nums, "add")}")
    print(f"Product: {spell_reducer(nums, "multiply")}")
    print(f"Max: {spell_reducer(nums, "max")}")
    print(f"Min: {spell_reducer(nums, "min")}")
    print()


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    first_partial = partial(base_enchantment, 50, "Ice")
    second_partial = partial(base_enchantment, 50, "Fire")
    third_partial = partial(base_enchantment, 50, "Wind")

    return {
            "ice": first_partial,
            "fire": second_partial,
            "wind": third_partial
            }


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"The power for {element} {target} is {power}"


if __name__ == "__main__":
    print("Testing partial enchanter...")
    part = partial_enchanter(base_enchantment)
    print(part["ice"](target="Dgagon"))
    print(part["fire"](target="Dragon"))
    print(part["wind"](target="Dragon"))
    print()


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise Exception("Negative value")
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


if __name__ == "__main__":
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())
    print()


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(something: int) -> str:
        return f"Damage spell: {something} damage"

    @dispatcher.register
    def _(something: str) -> str:
        return f"Enchantment: {something}"

    @dispatcher.register
    def _(something: list) -> str:
        return f"Multi-cast: {len(something)} spells"
    return dispatcher


if __name__ == "__main__":
    print("Testing spell dispatcher...")
    dis = spell_dispatcher()
    print(dis(42))
    print(dis("fireball"))
    print(dis([1, 2, 3]))
    print(dis({"tech": 42}))
