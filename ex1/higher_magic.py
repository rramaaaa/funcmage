from typing import Callable


test_values = [7, 13, 8]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> int:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell() -> str:
        return (
                f"Combined spell result: "
                f"{spell1(test_targets[0], test_values[0])}, \n"
                f"{spell2(test_targets[1], test_values[1])}"
                )
    return combined_spell


print("Testing spell combiner...")
combined = spell_combiner(fireball, heal)
print(combined())
print()


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplied_power(target: str, power: int) -> str:
        mult = power * multiplier
        print("oraginal ", end="")
        print(base_spell(target, power), end=", ")

        def new_spell(target: str, power: int) -> str:
            return f"Amplified: {power}"
        return new_spell("Dragon", mult)
    return multiplied_power


print("Testing power amplifier...")
mega_fireball = power_amplifier(fireball, 9)
print(mega_fireball("Dragon", 3))
print()


def spell(target: str, power: int) -> str:
    return f"spell target hits {target} for {power} HP"


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        return spell(target, power)

    def whatisthecondition() -> str:
        whatisit = condition()
        if whatisit:
            return new_spell("oraginal", 10)
        else:
            return "Spell fizzled"
    return whatisthecondition


def condition_status() -> int:
    return 1


print()

print("Testing conditional caster...")
cond = conditional_caster(condition_status, spell)
print(cond())


print()

spells = [fireball, spell, heal]


def spell_sequence(spells: list[Callable]) -> Callable:
    def all_spells(target: str, power: int) -> list[str]:
        results = []
        for i in spells:
            results.append(i(target, power))
        return results
    return all_spells


print("Testing spell sequence...")
call_spell = spell_sequence(spells)
listofcaste = call_spell("Orginal", 10)
x = 1
for i in listofcaste:
    print(f"Function {x}: {i}")
    x += 1
