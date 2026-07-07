from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    time = 0

    def counting() -> int:
        nonlocal time
        time += 1
        return time
    return counting


if __name__ == "__main__":
    counter_a = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print()


def spell_accumulator(initial_power: int) -> Callable:
    power_tot = initial_power

    def power_over_time(num: int) -> str:
        nonlocal power_tot
        power_tot += num
        return f"Base {initial_power}, add {num}: {power_tot}"
    return power_over_time


if __name__ == "__main__":
    accumntment = spell_accumulator(100)
    print("Testing spell accumulator...")
    print(accumntment(20))
    print(accumntment(30))
    print()


def enchantment_factory(enchantment_type: str) -> Callable:
    items = {
            "Frozen": "Shield",
            "Flaming": "Sword",
            "Earthen": "Cloak"
            }

    def enchanted_description() -> str:
        return f"{enchantment_type} {items[enchantment_type]}"
    return enchanted_description


if __name__ == "__main__":
    print("Testing enchantment factory...")
    enchanted = enchantment_factory("Flaming")
    print(enchanted())
    ench = enchantment_factory("Frozen")
    print(ench())
    print()


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> str:
        memory[key] = value
        return f"Store '{key}' = {value}"

    def recall(key: str) -> str:
        if key in memory:
            return f"Recall '{key}': {memory[key]}"
        else:
            return f"Recall '{key}': Memory not found"
    return {
            "store": store,
            "recall": recall
            }


if __name__ == "__main__":
    print("Testing memory vault...")
    memory = memory_vault()
    print(memory["store"]("secret", 42))
    print(memory["recall"]("secret"))
    print(memory["recall"]("unknown"))
    print()
