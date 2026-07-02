from collections.abc import Callable
from functools import wraps
import time

def spell_timer(func: Callable) -> Callable:
    print(f"Casting {func.__name__}")
    start = time.time()
    func()
    func()
    func()
    end = time.time()
    print(f"Spell completed in {end - start} seconds")
    @wraps(func)
    def function() -> str:
        print(f"Result: {func()}")
    return function

def func() -> str:
    return "Fireball cast!"

objec = spell_timer(func)
objec()
print()

def power_validator(min_power: int) -> Callable:
