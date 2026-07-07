from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        return (
                spell1(target, power),
                spell2(target, power)
                )
    return combined_spell


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))
    print()


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplied_power(target: str, power: int) -> str:
        mult = power * multiplier

        return (
                f"Original {base_spell(target, power)} "
                f", Amplified {base_spell(target, mult)}"
                )
    return multiplied_power


if __name__ == "__main__":
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 9)
    print(mega_fireball("Dragon", 3))
    print()


def spell(target: str, power: int) -> str:
    return f"spell target hits {target} for {power} HP"


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def whatisthecondition(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return whatisthecondition


def condition_status(target: str, power: int) -> int:
    return power > 10


if __name__ == "__main__":
    print()
    print("Testing conditional caster...")
    conditional = conditional_caster(condition_status, spell)
    print(conditional("Dragon", 2))
    print()

spells = [fireball, spell, heal]


def spell_sequence(spells: list[Callable]) -> Callable:
    def all_spells(target: str, power: int) -> list[str]:
        results = []
        for i in spells:
            results.append(i(target, power))
        return results
    return all_spells


if __name__ == "__main__":
    print("Testing spell sequence...")
    call_spell = spell_sequence(spells)
    listofcaste = call_spell("Orginal", 10)
    x = 1
    for i in listofcaste:
        print(f"Function {x}: {i}")
        x += 1
