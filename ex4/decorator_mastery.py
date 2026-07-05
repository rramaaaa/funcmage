from collections.abc import Callable
from functools import wraps
import time

def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper() -> None:
        print(f"Casting {func.__name__}...")
        start = time.time()
        run = func()
        end = time.time()
        result = end - start
        print(f"Spell completed in {result:.3f} seconds")
        print(f"Result: {run}")
    return wrapper

def fireball() -> str:
    return "Fireball cast!"

print("Testing spell timer...")
objec = spell_timer(fireball)
objec()
print()


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int):
            if power >= min_power:
                res = func(power)
                return res
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(10)
def power_spell(power: int) -> str:
    return "Waaaaaaagh spelled !"


print("Testing power validator...")
print(power_spell(5))
print(power_spell(7))
print(power_spell(9))
print(power_spell(10))
print()


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int) -> str:
            for counter in range(1, max_attempts + 1):
                try:
                    return func(power)
                except Exception:
                    if counter == max_attempts:
                        return f"Spell casting faild after {max_attempts} times"
                    else:
                        print(f"Spell failed, retrying... (atteempt {counter}/{max_attempts})")
        return wrapper
    return decorator

@retry_spell(3)
def spell_casting(power: int) -> str:
    if power > 10:
        return "Waaaaaaagh spell !"
    else:
        raise Exception("The power level is low")

print("Testing retrying spell...")
print(spell_casting(5))
print(spell_casting(30))
print()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
    def cast_spell(self, spell_name: str, power: int) -> str:
