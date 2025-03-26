import getpass
from collections.abc import Iterable
from string import ascii_letters, digits
from math import sqrt
from typing import Any

class QuickMethods:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "QuickMethods()"

    def say_hello(self) -> None:
        try:
            print(f"Hello, {getpass.getuser()}!")
        except:
            print("Hello! Hmm... I wasn't able to guess your name... Hello John Doe!")
    
    def string_is_number(self, string: str) -> bool:
        try:
            complex(string)
            return True
        except ValueError:
            return False

    def join_keys(self, keys: list[str] | tuple[str] = ['hello', 'world'], separator: str = '+') -> str:
        """
        Joins multiple string keys in a single string.
        """
        result = keys
        if not isinstance(keys, Iterable):
            raise ValueError(f"{type(keys).__name__} {keys} is not iterable.")
        if type(keys) is not str:
            string_keys = (str(key) for key in keys)
            result = separator.join(string_keys)
        return str(result)

    def prettify_name(self, string: str, separator: str = " ") -> str:
        #separator: str = custom_separator
        allowed = digits
        
        for l in string:
            if l not in ascii_letters and l not in allowed:
                if not l in separator:
                    string = string.replace(l, " ")
        
        words = [w.capitalize() for w in string.split(separator)]
        words = separator.join(words)
        return words

class QuickMath:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "QuickMath()"

    def solve_bhaskara(self, a: int, b: int, c: int) -> dict[str, Any]:
        delta = b**2 - 4*a*c
        
        if delta >= 0:
            positive_x = (-b + sqrt(delta)) / 2*a
            negative_x = (-b - sqrt(delta)) / 2*a
        
        result = {
            "delta": delta,
            "output": (positive_x, negative_x) if delta >=0 else None
        }
        
        return result

    def solve_hypotenuse(self, a: int | float, b: int | float) -> float:
        step1 = (a**2) + (b**2)
        c = sqrt(step1)
        return float(c)

    def percentage_of(self, value, percentage) -> float:
        return float((percentage / 100) * value)

if __name__ == "__main__":
    qm = QuickMethods()
    print(repr(qm), end="\n\n")
    
    qm.say_hello()
    print(qm.string_is_number("7j"))
    print(qm.prettify_name("Free-REORganiZed-staTES", "-"))