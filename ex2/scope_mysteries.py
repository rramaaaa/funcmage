time = 0
def mage_counter() -> Callable:
    def counting() -> int:
        nonlocal time  += 1
        return time
    return counting


power_tot = 0
def spell_accumntment(initial_power: int) -> Callable:
    def power_over_time() -> int:
        nonlocal power_tot += initial_power
        return power_tot
    return power_over_time


#def enchantment_factory(enchantment_type: str) -> Callable:
