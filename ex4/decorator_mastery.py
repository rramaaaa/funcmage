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
        print(f"Spell completed in {result: .3f} seconds")
        print(f"Result: {run}")
    return wrapper


def fireball() -> str:
    time.sleep(0.200)
    return "Fireball cast!"


if __name__ == "__main__":
    print("Testing spell timer...")
    timer = spell_timer(fireball)
    timer()
    print()


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = None
            for arg in args:
                if isinstance(arg, int) and not isinstance(arg, bool):
                    power = arg
            if power is None:
                power = kwargs["power"]
            if power >= min_power:
                res = func(*args, **kwargs)
                return res
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(10)
def power_spell(power: int) -> str:
    return "Waaaaaaagh spelled !"


if __name__ == "__main__":
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
                        return (
                                f"Spell casting faild after "
                                f"{max_attempts} times"
                                )
                    else:
                        print(
                                f"Spell failed, retrying... "
                                f"(atteempt {counter}/{max_attempts})"
                                )
        return wrapper
    return decorator


@retry_spell(3)
def spell_casting(power: int) -> str:
    if power > 10:
        return "Waaaaaaagh spell !"
    else:
        raise Exception("The power level is low")


if __name__ == "__main__":
    print("Testing retrying spell...")
    print(spell_casting(5))
    print(spell_casting(30))
    print()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Phoenix"))
    print(guild.validate_mage_name("Jo"))
    print(guild.cast_spell(spell_name = "Fire Ball", power = 50))
    print(guild.cast_spell("flash", 5))
