from collections.abc import Callable


test_values = [7, 13, 8]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"

def heal(target: str, power: int) -> int:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell() -> str:
        return (
                f"Combined spell result: {spell1(test_targets[0], test_values[0])},"
                f"{spell2(test_targets[1],test_values[1])}"
                )
    return combined_spell

combined = spell_combiner(fireball, heal)
#print(combined())



def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplied_power(x: int) -> int:
        return multiplier * x
    return multiplied_power



mega_fireball = power_amplifier(fireball, 3)
#print(mega_fireball(2))


def spell(target: str, power: int) -> str:
    return f"spell target hits {target} for {power} HP"

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if condition:
        return spell
    else:
        return "Spell fizzled"


def condition_status():
    return true
print("\n")
cond = conditional_caster(condition_status, spell)
#print(cond("Original", 10))



print("\n")

spells = [fireball, spell, heal]

def spell_sequence(spells: list[Callable]) -> Callable:
    def all_spells(target: str, power: int) -> list[str]:
        results = []
        for i in spells:
            results.append(i(target, power))
        return results
    return all_spells

call_spell = spell_sequence(spells)
#print(call_spell("Orginal", 10))
